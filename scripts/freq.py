import os
import warnings

warnings.simplefilter(action='ignore', category=UserWarning)

import pandas as pd
import spacy
from tqdm import tqdm
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

CORPUS_PATH = "../corpus"
DATE_COL = "paivamaara"
TEXTS = ["otsikko", "tiivistelma"]
BATCH_SIZE = 64

# word of interest
TARGET_LEMMAS = ["venäjä", "koronavirus", "yhdysvallat", "trump"]
COLORS = dict(zip(TARGET_LEMMAS, ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]))

nlp = spacy.load("fi_core_news_lg", disable=["parser", "ner"])
monthly_counts = {lemma: {} for lemma in TARGET_LEMMAS}

csv_files = [f for f in os.listdir(CORPUS_PATH) if f.endswith(".csv")]
for file in tqdm(csv_files, desc="Processing files"):
    df = pd.read_csv(os.path.join(CORPUS_PATH, file))
    if set(TEXTS + [DATE_COL]).issubset(df.columns):
        df[DATE_COL] = pd.to_datetime(
            df[DATE_COL], utc=True, errors="coerce")
        df = df.dropna(subset=[DATE_COL])
        df["month"] = df[DATE_COL].dt.to_period("M").astype(str)
        months = df["month"].tolist()
        texts = (df["otsikko"].fillna("") + " " +
                 df["tiivistelma"].fillna("")).tolist()

        for doc, month in zip(nlp.pipe(texts, batch_size=BATCH_SIZE), months):
            for token in doc:
                lemma = token.lemma_.lower()
                if lemma in TARGET_LEMMAS:
                    monthly_counts[lemma][month] = (
                            monthly_counts[lemma].get(month, 0) + 1)
dfs = {}
for lemma, data in monthly_counts.items():
    dfs[lemma] = (
        pd.DataFrame(data.items(), columns=["month", "frequency"])
        .sort_values("month")
        .reset_index(drop=True))

fig, axes = plt.subplots(
    2, 2,
    figsize=(14, 10),
    sharex=True,
    sharey=True
)
axes = axes.flatten()
grid_color = mcolors.to_rgba("gray", alpha=0.3)

for ax, lemma in zip(axes, TARGET_LEMMAS):
    df = dfs[lemma]
    ax.fill_between(df["month"], df["frequency"],
                    color=COLORS[lemma], alpha=0.6)
    ax.set_title(lemma.capitalize())
    ax.grid(True, color=grid_color)
    xticks = range(0, len(df), 4)
    ax.set_xticks(xticks)
    ax.set_xticklabels(df["month"].iloc[list(xticks)], rotation=45)

fig.suptitle('Sanojen kuukausittainen esiintymistiheys')
fig.text(0.5, 0.04, "Kuukausi", ha="center")
fig.text(0.04, 0.5, "Tiheys", va="center", rotation="vertical")
plt.tight_layout(rect=(0.05, 0.05, 1, 1))
plt.show()
