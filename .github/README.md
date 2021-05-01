# Suomenkielinen Tekstikorpus 🇫🇮 📰

**Finnish Language Text Corpus**

This is a Finnish language news headlines text corpus. This dataset is a collection of news headlines and short summaries of text, organized by date, into csv files. The intended use of this dataset is for machine learning or related use case. The remainder of this document will be in Finnish.

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
|`id` | uniikki tunniste | string, NOT NULL |

#### Tilastot

| Vuosi | Artikkelien<br/>lukumäärä |
| :---: | :---: |
| 2021 | 13706 |
| 2020 | 42937 |
| 2019 | 48698 |
| 2018 | 9134 |
| 2017 | 247 |
| 2016 | 155 |
| 2015 | 66 |
| 2014 | 15 |
| 2013 | 1 |
| 2012 | 1 |
| **Yhteensä** | **114960** |

Vanhin artikkeli: `2012-07-25`<br/>
Uusin artikkeli: `2021-04-30`<br/>
Tiedostojen lukumäärä: `230`

Jokaisella julkaistulla artikkelilla on uniikki tunniste, ja tiedostoja kerätessä on varmistettu että tämä korpus ei sisällä kaksoiskappaleita. Jos haluat enemmän tietoa jokaisesta uutisartikkelista, <a href="mailto:hello@neea.dev">kerro minulle</a>. Esimerkiksi jutun kategoria on mahdollista, mutta ei tällä hetkellä ole mukana tässä arkistossa. Päivitän tätä korpusta kuukausittain.

#### Ajanjaksot

Tämä on kronologinen kokoelma artikkeleja. Käytä [git tagejä](https://github.com/nkrusch/fi-news-corpus/releases) jos haluat löytää artikkeleja tiettyyn päivämäärään asti. Vaihtoehtoisesti voit rajata tiedostoja tunnisteiden perusteella.

| Vuosi | Ensimmäinen | Viimeinen |
| --- | --- | --- |
| 2021 | `C8695FAF6FA548A4887678FCC91275CF`	 | - |
| 2020 | `91EC5FB8EC88429588DC33EB1F0AD285` | `E4C877777DAA4F9599CF4600D5EC477A` |
| 2019 | `08B54A39B9B5438B9CB94CE548D5321F` | `DF6A0D528F5F4041BC2AEEE156937EFC` |
| 2018 | `201712282200634312` <sup>*</sup> | `0FF72F755B554FA889147BFBACAAE724` |

<sup>*)</sup> Tämä korpus alkaa virallisesti päivämäärastä 11.4.2018. Osa artikkeleista on alun perin huomattavasti vanhempia. Vanhempia artikkeleja on muokattu alkuperäisen julkaisupäivän jälkeen, mistä syystä kyseiset artikkelit ovat ilmestyneet sivustolle uudestaan ja siten päätyneet osaksi tätä korpusta. Vanhempien artikkelien kokoelma (ja vuoden 2018 ensimmäisen artikkelin tunniste) saattaa muuttua.

### Lisenssi

[MIT](/LICENSE)
