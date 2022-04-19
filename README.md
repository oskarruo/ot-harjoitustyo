# World's Hardest Game

Tasohyppelypeli jossa pelaajan tulee liikuttaa kuutio maaliin väistellen esteitä ja keräten esineitä.

[Viikko 5 release](https://github.com/oskarruo/ot-harjoitustyo/releases/tag/viikko5)

## Dokumentaatio

[Vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuurikuvaus](/dokumentaatio/arkkitehtuuri.md)

[Changelog](/dokumentaatio/changelog.md)

[Työaikakirjanpito](/dokumentaatio/tyoaikakirjanpito.md)

## Ohjeet asennukseen

1. Asenna riippvuudet komennolla:
```bash
poetry install
```
2. Käynnistä sovellus komennolla:
```bash
poetry run invoke start
```

## Ohjeet komentorivitoimintoihin

1. Ohjelman voi suorittaa komennolla:
```bash
poetry run invoke start
```
2. Testit voi suorittaa komennolla:
```bash
poetry run invoke test
```
3. Testikattavuusraportin voi generoida komennolla:
```bash
poetry run invoke coverage-report
```
4. Pylint-tarkastukset voi suorittaa komennolla
```bash
poetry run invoke lint
```
