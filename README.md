# Suomenkielinen Tekstikorpus 🇫🇮 

<img src='https://img.shields.io/github/commit-activity/m/nkrusch/fi-news-corpus' /> <img src='https://img.shields.io/github/last-commit/nkrusch/fi-news-corpus' /> <img src="https://img.shields.io/github/issues/nkrusch/fi-news-corpus" /> <img src='https://img.shields.io/github/repo-size/nkrusch/fi-news-corpus' />

**Finnish Language Text Corpus**

*This is a Finnish language news headlines text corpus.* This dataset is a collection of news headlines and short leading snippets of text, organized by date, into csv files. The intended usage of this data is for linguistic research and machine learning.

<img src='https://i.imgur.com/KlXF2d8.png' alt='kuva' />

### Tämä on iltapäivälehtien otsikoista koottu tekstikorpus koneoppimiseen. Tämä aineisto sisältää uutisotsikoista koottuja tekstejä, jotka on tallennettu csv tiedostoihin. Jokaisesta uutisesta on tallennettu otsikko, lyhyt lisäteksti, kuva, sekä julkaisupäivämäärä. Arkisto on järjestetty kronologisesti.

#### Avainsanat / Keywords:

- Suomenkieliset uutisotsikot
- Kootut Lehtiartikkelit
- Iltapäivälehtien otsikot
- Koneoppi, machine learning
- Data science
- Kielen rakenneanalyysi

--- 

### Koodiesimerkit & Käyttö

**[Täältä löydät tietoa ja koodiesimerkkejä](https://korpus.neea.dev/)**

---

### Tiedostojen kuvaus

Tämä arkisto koostuu useasta tiedostosta (shard) joista jokainen sisältä saman verran rivejä (500). Nämä osat on luotu aikajärjestyksessä, eli `shard-0` sisältää vanhimmat julkaistut artikkelit, ja suurin shard numero sisältää uusimmat artikkelit. 
 
Jokainen csv-tiedosto sisältää sarakeotsikot ensimmäisellä rivillä. Tiedostojen yleinen järjestys on seuraava:

| Sarake | Kuvaus | Tyyppi | 
| --- | --- | --- | 
|`paivamaara` | julkaisupäivä | ISO 8601 (UTC) |
|`otsikko` | uutisartikkelin otsikko | string, NOT NULL |
|`tiivistelma` | artikkelia kuvaava lisäteksti | string, NULL |
|`kuva` | artikkelin kuva | string, NULL |


#### Tilastot

| Vuosi | Artikkelien lukumäärä |
| :---: | :---: |
| 2020 |  9091 |
| 2019 |  48692 |
| 2018 |  9061 |
| 2017 |  203 |
| 2016 |  133 |
| 2015 |  64 |
| 2014 |  15 |
| **Yhteensä** | **67259** |

Vanhin artikkeli: `2014-01-21` <br/>
Uusing artikkeli: `2020-03-13` <br/>
Tiedostojen lukumäärä: `135`

Jos haluat enemmän tietoa jokaisesta uutisartikkelista, [kerro minulle](https://github.com/nkrusch/fi-news-corpus/issues). Esimerkiksi jutun kategoria on mahdollista, mutta ei tällä hetkellä ole mukana tässä arkistossa.

Tämä korpus sisältää otsikoita jutuista jotka on julkaistu tai päivitetty 4/11/2018 jälkeen. Osa otsikoista on alun perin huomattavasti vanhempia, mutta kyseisiä artikkeleja on muokattu alkuperäisen julkaisupäivän jälkeen. 


### Projektilista

Nimi | Kuvaus | Linkki
--- | --- | ---
*(tyhjä)* | *(tyhjä)* | *(tyhjä)*


#### Lisäykset projektilistaan 
 
Jos käytät tätä arkistoa jossain tutkimuksessa tai projektissa:

1. Fork this repo
2. Lisää nimesi tähän readme:n projektilistaan 
3. [Submit a PR](https://github.com/nkrusch/fi-news-corpus/pulls)

### Lisenssi

[MIT](/LICENSE)
