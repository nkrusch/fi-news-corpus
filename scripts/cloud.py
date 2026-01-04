import os
from collections import Counter

import matplotlib.pyplot as plt
import nltk
import pandas as pd
import spacy
from tqdm import tqdm
from wordcloud import WordCloud

nlp = spacy.load("fi_core_news_lg")
nltk.download("stopwords")

from nltk.corpus import stopwords

CORPUS_PATH = "../corpus"
OUTPUT_FILE = "../media/wordcloud.png"
COLUMNS = ['otsikko', 'tiivistelma']
IGNORE = set(
    "aika,asia,ei,että,hetki,ihminen,il,iltalehden,iltalehti,ja,jolla,jos,"
    "kausi,kerta,kun,lapsi,maa,mies,miksi,myös,nainen,ne,niin,olen,on,osa,"
    "paikka,poika,päivä,se,syy,taas,tapa,tilanne,tuo,tämä,vaan,video,viikko,"
    "voi,vuosi,yle,äiti,kuva,kyse,apu,iltalehde".split(','))

texts = []
for file in tqdm([f for f in os.listdir(CORPUS_PATH)
                  if f.endswith(".csv")], desc="Reading CSVs"):
    df = pd.read_csv(os.path.join(CORPUS_PATH, file))
    for col in COLUMNS:
        texts.extend(df[col].dropna().astype(str).tolist())

noun_counts = Counter()
STOPWORDS = set(stopwords.words("finnish")) | IGNORE
for text in tqdm(texts, desc="Processing text"):
    for token in nlp(text):
        if token.pos_ in {"NOUN", "PROPN"}:
            lemma = token.lemma_.lower()
            if lemma.isalpha() and lemma not in STOPWORDS:
                noun_counts[lemma] += 1

wc = WordCloud(width=1600, height=800, background_color="white",
               max_words=200, colormap="viridis")
wc.generate_from_frequencies(noun_counts)
plt.figure(figsize=(14, 7))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
wc.to_file(OUTPUT_FILE)
