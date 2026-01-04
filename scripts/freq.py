import os
import warnings

warnings.simplefilter(action='ignore', category=UserWarning)

import pandas as pd
import spacy
from tqdm import tqdm
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

CORPUS_PATH = "../corpus"
OUTPUT_FILE = "../media/freq.png"
DATE_COL = "paivamaara"
TEXTS = ["otsikko", "tiivistelma"]
CACHE_FILE = "monthly_word_counts.csv"
START_YEAR, END_YEAR = (2019, 2025)
BATCH_SIZE = 64
TARGET_LEMMAS = ["venäjä", "koronavirus", "yhdysvallat", "trump"]
COLORS = ["#472A7A", "#256C7F", "#44C070", "#D0E11D"]

if os.path.exists(CACHE_FILE):
    counts_df = pd.read_csv(CACHE_FILE)
else:
    nlp = spacy.load("fi_core_news_lg", disable=["parser", "ner"])
    ALL_MONTHS = dict([(m, 0) for m in [item for sublist in [
        [f'{y}-{m:>02}' for m in list(range(1, 13))] for y
        in range(START_YEAR, END_YEAR + 1)] for item in sublist]])
    monthly_counts = {lemma: ALL_MONTHS.copy() for lemma in TARGET_LEMMAS}
    csv_files = [f for f in os.listdir(CORPUS_PATH) if f.endswith(".csv")]

    for file in tqdm(csv_files, desc="Processing files"):
        df = pd.read_csv(os.path.join(CORPUS_PATH, file))
        if set(TEXTS + [DATE_COL]).issubset(df.columns):
            df[DATE_COL] = pd.to_datetime(
                df[DATE_COL], utc=True, errors="coerce")
            df = df.dropna(subset=[DATE_COL])
            df = df[START_YEAR <= df[DATE_COL].dt.year]
            df = df[df[DATE_COL].dt.year <= END_YEAR]
            if df.empty:
                continue
            df["month"] = df[DATE_COL].dt.to_period("M").astype(str)
            months = df["month"].tolist()
            texts = (df["otsikko"].fillna("") + " " +
                     df["tiivistelma"].fillna("")).tolist()

            for doc, month in zip(
                    nlp.pipe(texts, batch_size=BATCH_SIZE), months):
                for token in doc:
                    lemma = token.lemma_.lower()
                    if lemma in TARGET_LEMMAS:
                        monthly_counts[lemma][month] = (
                                monthly_counts[lemma].get(month, 0) + 1)
    dfs, rows = {}, []
    for lemma, data in monthly_counts.items():
        for month, freq in data.items():
            rows.append({
                "month": month, "word": lemma, "frequency": freq})
    counts_df = (
        pd.DataFrame(rows)
        .sort_values(["word", "month"])
        .reset_index(drop=True))
    counts_df.to_csv(CACHE_FILE, index=False)

dfs = {}
all_months = sorted(counts_df["month"].unique())
for lemma in TARGET_LEMMAS:
    df = (counts_df[counts_df["word"] == lemma]
          .set_index("month")
          .reindex(all_months, fill_value=0)
          .reset_index())
    dfs[lemma] = df

plt.rcParams['font.sans-serif'] = ['Noto Sans', 'Arial']
plt.rcParams["font.family"] = "sans-serif"
fig, axes = plt.subplots(2, 2, figsize=(8, 8), sharex=True, sharey=True)
axes = axes.flatten()
for i, (ax, lemma) in enumerate(zip(axes, TARGET_LEMMAS)):
    df = dfs[lemma]
    ax.margins(x=.0, y=.0)
    ax.grid(True, color='#dddddd')
    ax.fill_between(
        df["month"], df["frequency"],
        color=COLORS[i], alpha=0.7, zorder=2)
    ax.set_title(lemma.capitalize(), x=.03, y=.99, pad=-14,
                 horizontalalignment='left', fontsize=10)
    ax.set_ylim([0, 1024])
    ax.set_yscale('log', base=2)
    ax.yaxis.set_major_formatter(ScalarFormatter())
    xticks = range(0, len(df), 12)
    ax.set_xticks(xticks)
    labels = [str(int(x[5:])) + '/' + x[2:4]
              for x in df["month"].iloc[list(xticks)]]
    ax.set_xticklabels(labels, rotation=30)

fig.suptitle('Sanojen kuukausittainen esiintymistiheys', weight='bold')
fig.text(0.5, 0.04, "Kuukausi", ha="center")
fig.text(0.04, 0.5, "Lukumäärä", va="center", rotation="vertical")
plt.tight_layout(rect=(0.05, 0.05, 1, 1))
plt.savefig(OUTPUT_FILE, bbox_inches="tight", dpi=150)
