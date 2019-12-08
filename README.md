# Finnish Language Text Corpus 🇫🇮 

This is a Finnish language news headlines text corpus. 

This dataset is a collection of news headlines and short leading snippets of text, organized by date, into csv files.
The intended usage of this data is for linguistic research and machine learning.

----

## Ja sama suomeksi

Tämä on iltapäivälehtien ostikoista koottu tekstikorpus koneoppimiseen.

Tämä aineisto sisältää uutisotsikoista koottuja tekstejä, jotka on tallennettu csv tiedostoihin. Jokaisesta uutisesta on tallennettu otsikko, lyhyt lisäteksti sekä julkaisupäivämäärä. Arkisto on järjestetty kronologisesti.


Jokainen tiedostu sisältää sarake otsikot ensimmäisellä rivillä. Tiedostojen yleinen järjestys on seuraava:

| Column | Description |
| --- | --- |
|`id` | uniikki tunniste (guid) | 
|`date` | julkaisupäivä |
|`title` | otsikko |
|`lead` | lisäteksti |


Tämä korpus sisältää otsikoita jotuista jotka on julkaistu tai päivitetty 11/2018 jälkeen. 
Osa otsikoista on huomattavasti vanhempia. Tämä arkisto on koottu robottien avulla ja päivittyy automaattisesti.

Olen käyttänyt tätä dataa mm. henkilökohtaisen suositusjärjestelmän rakentamiseen. Jos käytät tätä arkistoa jossain tutkimuksessa tai projektissa, kerro siitä niin laitan nimesi tähän readme:n. 

Lisenssi

MIT
