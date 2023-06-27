# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
import pandas as pd

def stillingspst_grp(still_pst):
    if still_pst <= 0:
        return 0
    elif 0 < still_pst < 100:
        return 1
    elif still_pst == 100:
        return 2
    elif still_pst > 100:
        return 3
    else:
        return 4

def stillingspst(still_pst):
    if 0 < still_pst < 100:
        return 1
    elif still_pst == 100:
        return 2
    elif still_pst > 100:
        return 3
    
def naring(nar):
    if pd.isna(nar) == True:
        nar = 0
    nar = int(nar)
    if 1000 <= nar <= 3999:
        return '01-39. Jordbruk, skogbruk og fiske'
    elif 5000 <= nar <= 9999:
        return '05-09. Bergverksdrift og utvinning'
    elif 10000 <= nar <= 33999:
        return '10-33. Industri'
    elif 35000 <= nar <=39999:
        return '35-39. Elektrisitet, vann og renovasjon'
    elif 41000 <= nar <= 43999:
        return '41-43. Bygge- og anleggsvirksomhet'
    elif 45000 <= nar <= 47999:
        return '45-47. Varehandel, motorvognrep.'
    elif 49000 <= nar <= 53999:
        return '49-53. Transport og lagring'
    elif 55000 <= nar <= 56999:
        return '55-56. Overnattings- og serveringsvirksomhet'
    elif 58000 <= nar <= 63999:
        return '58-63. Informasjon og kommunikasjon'
    elif 64000 <= nar <= 66999:
        return '64-66. Finansiering og forsikringsvirksomhet'
    elif 68000 <= nar <= 75999:
        return '68-75. Teknisk tjenesteyting, eiendomsdrift'
    elif 77000 <= nar <= 82999:
        return '77-82. Forretningsmessig tjenesteyting,utleiev.'
    elif 84000 <= nar <= 84999:
        return '84. Offentlig administrasjon og forsvar, sosialforsikring'
    elif 85000 <= nar <= 85999:
        return '85. Undervisning'
    elif 86000 <= nar <= 88999:
        return '86-88. Helse- og sosialtjenester'
    elif 90000 <= nar <= 99999:
        return '90-99. Personlig tjenesteyting'
    else:
        return 'Uoppgitt'

def kildepst(kilde):
    if pd.isna(kilde) == True:
        kilde = 0
    kilde = int(kilde)   
    if kilde == 1:
        return 0
    elif 15 <= kilde <= 20:
        return 1
    elif 21 <= kilde <= 23:
        return 2
    elif 24 <= kilde <= 26:
        return 3
    else:
        return 4

# -


