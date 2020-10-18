# Suomenkielinen Tekstikorpus 🇫🇮 📰

<img src='https://img.shields.io/github/last-commit/nkrusch/fi-news-corpus?style=flat-square' /> <img src='https://img.shields.io/github/repo-size/nkrusch/fi-news-corpus?style=flat-square' />

**Finnish Language Text Corpus**

*This is a Finnish language news headlines text corpus.* This dataset is a collection of news headlines and short summaries of text, organized by date, into csv files. The intended use of this dataset is for linguistic research and machine learning. The remainder of this document will be in Finnish.

<img src='https://i.imgur.com/KlXF2d8.png' alt='kuva' />

### Tämä on iltapäivälehtien otsikoista koottu tekstikorpus koneoppimiseen. Tämä aineisto sisältää uutisotsikoista koottuja tekstejä, jotka on tallennettu csv tiedostoihin. Jokaisesta uutisesta on tallennettu otsikko, lyhyt lisäteksti, kuva, sekä julkaisupäivämäärä. Arkisto on järjestetty kronologisesti.

#### Avainsanat:

- Suomenkieliset uutisotsikot
- Kootut lehtiartikkelit
- Iltapäivälehtien otsikot
- Uutistrendit
- Koneoppi
- Datatiede
- Kielen rakenneanalyysi

--- 

### Tiedostojen kuvaus

Tämä arkisto koostuu useasta tiedostosta (shard) joista jokainen sisältä saman verran rivejä (500). Nämä osat on luotu aikajärjestyksessä, eli `shard-0` sisältää vanhimmat julkaistut artikkelit, ja suurin shard numero sisältää uusimmat artikkelit. 
 
Jokainen csv-tiedosto sisältää sarakeotsikot ensimmäisellä rivillä. Tiedostojen yleinen järjestys on seuraava:

| Sarake | Kuvaus | Tyyppi | 
| --- | --- | --- | 
|`paivamaara` | alkuperäinen julkaisupäivä | ISO 8601 (UTC) |
|`otsikko` | uutisartikkelin otsikko | string, NOT NULL |
|`tiivistelma` | artikkelia kuvaava lisäteksti | string, NULL |
|`kuva` | artikkelin kuva | string, NULL |
|`id` | uniikki tunniste |

#### Tilastot

| Vuosi | Artikkelien lukumäärä |
| :---: | :---: |
| 2020 | 31827 |
| 2019 | 48696 |
| 2018 | 9104 |
| 2017 | 232 |
| 2016 | 151 |
| 2015 | 66 |
| 2014 | 15 |
| 2013 | 1 |
| 2012 | 1 |
| **Yhteensä** | **90093** |

Vanhin artikkeli: `2012-07-25` <br/>
Uusin artikkeli: `2020-09-27` <br/>
Tiedostojen lukumäärä: `181`

Jos haluat enemmän tietoa jokaisesta uutisartikkelista, [kerro minulle](hello@neea.dev). Esimerkiksi jutun kategoria on mahdollista, mutta ei tällä hetkellä ole mukana tässä arkistossa.

Tämä korpus sisältää otsikoita jutuista jotka on julkaistu tai päivitetty 11.4.2018 jälkeen *sen toisen suositun iltapäivälehden* www-sivuilla. Osa artikkeleista on alun perin huomattavasti vanhempia. Vanhempia artikkeleja on muokattu alkuperäisen julkaisupäivän jälkeen, mistä syystä kyseiset artikkelit ovat ilmestyneet sivustolle uudestaan ja siten päätyneet osaksi tätä korpusta. 

Jokaisella julkaistulla artikkelilla on uniikki tunniste, ja tiedostoja kerätessä on varmistettu että tämä korpus ei sisällä kaksoiskappaleita.

### Lisenssi

[MIT](/LICENSE)
