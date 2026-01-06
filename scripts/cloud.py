from collections import Counter
from os.path import join as join

import nltk
import pandas as pd
import spacy
from nltk.corpus import stopwords
from tqdm import tqdm
from wordcloud import WordCloud

from common import *

OUTPUT_FILE = '../media/wordcloud.png'
EXTRA_STOPWORDS = 'ignore.txt'
PLT_TITLE = 'Sanapilvi: Yleisimmät puheenaiheet'
KINDS = {'NOUN', 'PROPN'}

nltk.download('stopwords')
nlp = spacy.load('fi_core_news_lg')
IGNORE = pd.read_csv(EXTRA_STOPWORDS, header=None)
STOPWORDS = set(stopwords.words('finnish')) | set(IGNORE[0])

counts = Counter()
for file in tqdm(files(), desc="Processing files"):
    for doc in nlp.pipe((pd.read_csv(join(CORPUS_PATH, file))[TEXTS]
            .astype(str).agg(' '.join, axis=1).tolist()), batch_size=500):
        for x in [t.lemma_.lower() for t in doc if t.pos_ in KINDS]:
            if x.isalpha() and x not in STOPWORDS:
                counts[x] += 1

wc = WordCloud(width=1600, height=800, max_words=200, margin=10,
               background_color="white", colormap="viridis",
               font_path=FUTURA).generate_from_frequencies(counts)

plt.figure(figsize=(10, 5))
plt.axis("off")
plt.suptitle(PLT_TITLE, fontweight='bold')
plt.imshow(wc, interpolation="bilinear")
plt.tight_layout(rect=(.05, .05, 1, 1))
plt.savefig(OUTPUT_FILE, bbox_inches="tight", dpi=150)
