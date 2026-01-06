from os import listdir

import matplotlib.pyplot as plt

CORPUS_PATH = "../corpus"
DATE, TEXTS = "paivamaara", ["otsikko", "tiivistelma"]

plt.rcParams['font.sans-serif'] = ['Menlo', 'Arial']
plt.rcParams["font.family"] = "sans-serif"
FUTURA = '/System/Library/Fonts/Supplemental/Futura.ttc'


def files() -> list[str]:
    return [f for f in listdir(CORPUS_PATH) if f.endswith(".csv")]
