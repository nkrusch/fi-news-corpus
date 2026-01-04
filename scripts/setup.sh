#!/usr/bin/env bash

python --version && pip --version
pip install pandas spacy nltk wordcloud matplotlib tqdm
python -m spacy download fi_core_news_lg