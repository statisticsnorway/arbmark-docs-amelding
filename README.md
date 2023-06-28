# Registerbasert lønns- og sysselsettingsstatistikk basert på a-ordningen

Dette repoet inneholder koden som genererer dokumentasjonsnotatet for lønns- og arbeidsmarkedsstatistikk. Boken er skrevet i markdown og bygget med [Quarto](https://quarto.org/) til en nettside. Tabeller er generert med Python-kode i en [Jupyterlab](https://jupyter.org/) Notebook. 

Notatet er en pilot for å vurdere alternativer til de tidligere dokumentasjonsnotatene i pdf-formatet. Derfor vil det kunne forekomme hyppigere endringer her enn i tidligere pdf-versjoner.  

Du finner notatet her: <https://doc.ameld.ssb.no/>

## Bygge boken

Det er bare SSB-ansatte med tilgang til tabellgrunnlaget som kan bygge boken med koden i dette repoet. Da gjør man følgende:

1. Klone repoet: `git clone https://github.com/statisticsnorway/arbmark-docs-amelding.git`
2. Bygg prosjektet med [ssb-project-cli](https://pypi.org/project/ssb-project-cli/): `ssb-project build` når du står i *root* av prosjektet
3. Lag en mappe med navn **Data** i root av prosjektet der du legger grunnlaget for tabellene som skal bygges
4. Stå i *root* av prosjektet og skriv `quarto render arbmark-docs-amelding` for å generere ny versjon av boken

## Om dokumentet

Dette er en dokumentasjon av produksjonsprosessen for data til arbeidsmarkeds- og lønnsstatistikk. Hovedkilden er a-ordningen som Statistisk sentralbyrå (SSB) mottar fra Skatteetaten hver måned, og det blir gjort en rekke statistiske bearbeidinger og påkoblinger av andre kjennemerker i SSB. Den klargjorte filen for arbeidsmarkeds og lønnsstatistikk benyttes av svært mange statistikker, analyser og til forskning i SSB samt til deling av data på microdata.no.


## Bruk av dokumentet

Dokumentet gir en detaljet beskrivelse av produksjonsprosessen. Det anbefales å bruke dokumentet som et oppslagsverk. Benytt kapitteloversikten og leseveiledningen i kapittel 1.6 for å få en oversikt og innholdet i dokumentet. 


## Kontakt

christoffer.berge@ssb.no
Knut.Snellingen.Bye@ssb.no
Stine.bakke@ssb.no
Arbeidsmarked@ssb.no



