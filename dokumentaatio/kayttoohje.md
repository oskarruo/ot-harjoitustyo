# Käyttöohje
Lataa uusin [release](https://github.com/oskarruo/ot-harjoitustyo/releases/tag/loppupalautus)

## Ohjelmat käynnistäminen
1. Asenna riippvuudet komennolla:
```bash
poetry install
```
2. Käynnistä sovellus komennolla:
```bash
poetry run invoke start
```
## Pelin aloitus
Sovellus käynnistyy käyttöliittymään, voit aloittaa pelin painamalla "Aloita peli", tai voit pelata yksittäisen tason painamalla "Valitse taso" ja valitsemalla tason.

## Pelin lopetus
Voit poistua pelistä milloin tahansa painamalla ESC-näppäintä. Pelistä poistuminen pitää käyttöliittymän auki. Voit poistua käyttöliittymästä ja koko sovelluksesta painamalla "Poistu"

## Pelin kulku
Pelissä on tavoitteena ohjata nuolinäppäimillä punainen neliö maaliin väistellen vihollisia. Joissain tasoissa pelaajan tulee kerätä esineitä voidaakseen läpäistä tason. Taso nollautuu jos pelaaja osuu viholliseen.
