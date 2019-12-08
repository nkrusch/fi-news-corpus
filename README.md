<img src='https://img.shields.io/github/commit-activity/m/nkrusch/fi-news-corpus' /> <img src='https://img.shields.io/github/contributors/nkrusch/fi-news-corpus' /> <img src='https://img.shields.io/github/last-commit/nkrusch/fi-news-corpus' /> <img src="https://img.shields.io/github/issues/nkrusch/fi-news-corpus" />

# Finnish Language Text Corpus

> This is a Finnish language news headlines text corpus. 

This dataset is a collection of news headlines and short leading snippets of text, organized by date, into csv files.
The intended usage of this data is for linguistic research and machine learning.


*Ja sama suomeksi*

## Suomenkielinen Tekstikorpus 🇫🇮 

> Tämä on iltapäivälehtien ostikoista koottu tekstikorpus koneoppimiseen.

Tämä aineisto sisältää uutisotsikoista koottuja tekstejä, jotka on tallennettu csv tiedostoihin. Jokaisesta uutisesta on tallennettu otsikko, lyhyt lisäteksti sekä julkaisupäivämäärä. Arkisto on järjestetty kronologisesti.

### Tiedostojen kuvaus

Jokainen tiedostu sisältää sarake-otsikot ensimmäisellä rivillä. Tiedostojen yleinen järjestys on seuraava:

| Sarake | Kuvaus | Tyyppi | 
| --- | --- | --- | 
|`paivamaara` | julkaisupäivä | ISO 8601 (UTC) |
|`otsikko` | uutisartikkelin otsikko | string, NOT NULL |
|`tiivistelma` | artikkelia kuvaava lisäteksti | string, NULL |

Jos haluat enemmän tietoa jokaisesta uutisartikkelista, ilmoita asiasta (create an issue). Esimerkiksi jutun kategoria ja oheinen kuva on mahdollista, mutta ei tällä hetkellä ole mukana tässä arkistossa.

Tämä korpus sisältää otsikoita jotuista jotka on julkaistu tai päivitetty 11/2018 jälkeen. Osa otsikoista on alunperin huomattavasti vanhempia, mutta kyseisiä artikkeleja on muokattu myöhemmin. 

Tämä arkisto on koottu robottien avulla iltapäivälehtiotsikoista ja päivittyy automaattisesti.

Olen käyttänyt tätä dataa mm. henkilökohtaisen suositusjärjestelmän rakentamiseen. Jos käytät tätä arkistoa jossain tutkimuksessa tai projektissa, lisää nimesi tähän readme:n (create a PR). 

## Lisenssi

MIT
