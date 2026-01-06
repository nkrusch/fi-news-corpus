import os
import warnings
from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd
import spacy
from matplotlib.ticker import ScalarFormatter
from tqdm import tqdm

WORDS = ["venäjä", "koronavirus", "yhdysvallat", "trump"]
COLOR = ["#472A7A", "#256C7F", "#44C070", "#D0E11D"]
START, END = (2019, 2025)
OUTPUT_FILE = "../media/freq.png"
PLT_TITLE = 'Sanojen kuukausittainen esiintymistiheys'
AXY, AXX = 'Lukumäärä', 'Kuukausi'
PLOTS_MN = (2, 2)

CORPUS_PATH = "../corpus"
CACHE_FILE = "monthly_counts.csv"
DATE, TEXTS = "paivamaara", ["otsikko", "tiivistelma"]
MTH, FRQ, WRD = 'month', 'frequency', 'word'
BATCH_SIZE = 64

plt.rcParams['font.sans-serif'] = ['Menlo', 'Arial']
plt.rcParams["font.family"] = "sans-serif"

if os.path.exists(CACHE_FILE):
    cdf = pd.read_csv(CACHE_FILE)
else:
    warnings.simplefilter(action='ignore', category=UserWarning)
    nlp = spacy.load("fi_core_news_lg", disable=["parser", "ner"])
    sub_keys = dict([(m, 0) for m in [item for sublist in [
        [f'{y}-{m:>02}' for m in list(range(1, 13))] for y
        in range(START, END + 1)] for item in sublist]])
    monthly_counts = {lemma: sub_keys.copy() for lemma in WORDS}
    files = [f for f in os.listdir(CORPUS_PATH) if f.endswith(".csv")]

    for file in tqdm(files, desc="Processing files"):
        df = pd.read_csv(os.path.join(CORPUS_PATH, file))
        if set(TEXTS + [DATE]).issubset(df.columns):
            df[DATE] = pd.to_datetime(df[DATE], utc=True, errors="coerce")
            df = df.dropna(subset=[DATE])
            df = df[START <= df[DATE].dt.year]
            df = df[df[DATE].dt.year <= END]
            months = df[DATE].dt.to_period("M").astype(str).tolist()
            texts = df[TEXTS].astype(str).to_numpy().flatten()
            tokens = [map(lambda t: t.lemma_.lower(), doc) for doc
                      in nlp.pipe(texts.tolist(), batch_size=BATCH_SIZE)]
            for doc, mth in zip(tokens, months):
                for w, c in Counter(filter(WORDS.__contains__, doc)).items():
                    monthly_counts[w][mth] += c

    cdf = pd.DataFrame([x for ls in [
        [{MTH: m, WRD: word, FRQ: f} for m, f in data.items()]
        for word, data in monthly_counts.items()] for x in ls]) \
        .sort_values([WRD, MTH]).reset_index(drop=True)
    cdf.to_csv(CACHE_FILE, index=False)

dfs = dict([(word, cdf[cdf[WRD] == word].set_index(MTH)
             .reindex(sorted(cdf[MTH].unique()), fill_value=0)
             .reset_index()) for word in WORDS])

fig, axes = plt.subplots(*PLOTS_MN, figsize=(8, 6), sharex=True, sharey=True)
for ax, (color, word) in zip(axes.flatten(), zip(COLOR, WORDS)):
    data, title = dfs[word], word.capitalize()
    x_ticks = range(5, len(data), 12)
    x_lbl = lambda x: f'{int(x[5:])}/{x[2:4]}'
    ax.margins(x=.0, y=.0)
    ax.grid(True, color='#dddddd')
    ax.set_ylim([1, 1024])
    ax.set_yscale('log', base=2)
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(map(x_lbl, data[MTH].iloc[x_ticks]), fontsize=9)
    ax.set_title(title, x=.03, y=.88, horizontalalignment='left', fontsize=9)
    ax.fill_between(data[MTH], data[FRQ], alpha=0.7, zorder=2, color=color)
    ax.yaxis.set_major_formatter(ScalarFormatter())

fig.suptitle(PLT_TITLE, fontweight='bold')
fig.text(0.5, 0.02, AXX, ha="center")
fig.text(0.02, 0.5, AXY, va="center", rotation="vertical")
plt.tight_layout(rect=(0.05, 0.05, 1, 1))
plt.savefig(OUTPUT_FILE, bbox_inches="tight", dpi=150)
