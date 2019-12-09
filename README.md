# Suomenkielinen Tekstikorpus 🇫🇮 

<img src='https://img.shields.io/github/commit-activity/m/nkrusch/fi-news-corpus' /> <img src='https://img.shields.io/github/last-commit/nkrusch/fi-news-corpus' /> <img src="https://img.shields.io/github/issues/nkrusch/fi-news-corpus" /> <img src='https://img.shields.io/github/repo-size/nkrusch/fi-news-corpus' />

<img src='https://i.imgur.com/DxowZ0i.jpg' alt='kuva' />

Tämä on iltapäivälehtien ostikoista koottu tekstikorpus koneoppimiseen. Tämä aineisto sisältää uutisotsikoista koottuja tekstejä, jotka on tallennettu csv tiedostoihin. Jokaisesta uutisesta on tallennettu otsikko, lyhyt lisäteksti sekä julkaisupäivämäärä. Arkisto on järjestetty kronologisesti.

---
**Finnish Language Text Corpus**

*This is a Finnish language news headlines text corpus.*

This dataset is a collection of news headlines and short leading snippets of text, organized by date, into csv files. The intended usage of this data is for linguistic research and machine learning.

---

### Avainsanat / Keywords:

- Suomenkieliset uutisotsikot
- Kootut Lehtiartikkelit
- Iltapäivälehtien otsikot
- Koneoppi, Machine learning
- Data science
- Kielen rakenneanalyysi

### Tiedostojen kuvaus

Tämä arkisto koostuu useasta osasta (shard) joista jokainen sisältä saman verran rivejä (500). Nämä osat on luotu aikajärjestyksessä, eli `shard-0` sisältää vanhimmat julkaistut artikkelit, ja suurin shard numero sisältää uusimmat julkaistut artikkelit. 
 
Jokainen csv-tiedosto sisältää sarake-otsikot ensimmäisellä rivillä. Tiedostojen yleinen järjestys on seuraava:

| Sarake | Kuvaus | Tyyppi | 
| --- | --- | --- | 
|`paivamaara` | julkaisupäivä | ISO 8601 (UTC) |
|`otsikko` | uutisartikkelin otsikko | string, NOT NULL |
|`tiivistelma` | artikkelia kuvaava lisäteksti | string, NULL |

Jos haluat enemmän tietoa jokaisesta uutisartikkelista, [ilmoita asiasta](https://github.com/nkrusch/fi-news-corpus/issues). Esimerkiksi jutun kategoria ja oheinen kuva on mahdollista, mutta ei tällä hetkellä ole mukana tässä arkistossa.

Tämä korpus sisältää otsikoita jutuista jotka on julkaistu tai päivitetty 4/11/2018 jälkeen. Osa otsikoista on alunperin huomattavasti vanhempia, mutta kyseisiä artikkeleja on muokattu myöhemmin. 

Tämä arkisto on koottu robottien avulla iltapäivälehtiotsikoista ja päivittyy automaattisesti tasaisin väliajoin.


### Projektilista

Nimi | Kuvaus | Linkki
--- | --- | ---
*(tyhjä)* | *(tyhjä)* | *(tyhjä)*


#### Lisäykset projektilistaan 
 
Jos käytät tätä arkistoa jossain tutkimuksessa tai projektissa:

1. Fork this repo
2. Lisää nimesi tähän readme:n projektilistaan 
3. [Submit a PR](https://github.com/nkrusch/fi-news-corpus/pulls)

## Lisenssi

MIT
