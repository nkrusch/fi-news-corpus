import os
from collections import Counter
from os.path import join as join

import matplotlib.pyplot as plt
import nltk
import pandas as pd
import spacy
from nltk.corpus import stopwords
from tqdm import tqdm
from wordcloud import WordCloud

CORPUS_PATH = '../corpus'
OUTPUT_FILE = '../media/wordcloud.png'
COLUMNS = ['otsikko', 'tiivistelma']
KINDS = {'NOUN', 'PROPN'}
EXTRA_STOPWORDS = 'ignore.txt'

futura = '/System/Library/Fonts/Supplemental/Futura.ttc'
plt.rcParams['font.sans-serif'] = ['Menlo', 'Arial']
plt.rcParams['font.family'] = 'sans-serif'
PLT_TITLE = 'Sanapilvi: Yleisimmät puheenaiheet'

files = [f for f in os.listdir(CORPUS_PATH) if f.endswith('.csv')]
col_frt = lambda f: pd.read_csv(join(CORPUS_PATH, f))[COLUMNS].astype(str)
texts = [x for sl in map(col_frt, files) for x in sl.to_numpy().flatten()]

nltk.download('stopwords')
nlp = spacy.load('fi_core_news_lg')
IGNORE = pd.read_csv(EXTRA_STOPWORDS, header=None)
STOPWORDS = set(stopwords.words('finnish')) | set(IGNORE[0])

counts = Counter()
for text in tqdm(texts, desc="Processing text"):
    tokens = filter(lambda t: t.pos_ in KINDS, nlp(text))
    lemmas = map(lambda t: t.lemma_.lower(), tokens)
    keep = filter(lambda x: x.isalpha() and x not in STOPWORDS, lemmas)
    counts += Counter(keep)

wc = WordCloud(width=1600, height=800, max_words=200, margin=10,
               background_color="white", colormap="viridis",
               font_path=futura).generate_from_frequencies(counts)

plt.figure(figsize=(10, 5))
plt.axis("off")
plt.suptitle(PLT_TITLE, fontweight='bold')
plt.imshow(wc, interpolation="bilinear")
plt.tight_layout(rect=(.05, .05, 1, 1))
plt.savefig(OUTPUT_FILE, bbox_inches="tight", dpi=150)
