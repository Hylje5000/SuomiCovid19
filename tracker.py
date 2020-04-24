import COVID19Py
import json
import urllib.request
import os
#Main-ohjelman osat
def Titlebar():
    os.system('clear')
              
    print("**********************************************")
    print("   COVID-19 Suomi-Seuranta - By Hylje5000  ")
    print("**********************************************")

def getChoice():
    print("\n")
    print("1 Suomen yleistilanne")
    print("2 Tartunnat iän mukaan")
    print("3 Piirrä kuvaajat")
    print("0 Sulje ohjelma")
    print("\n")
    return input()

#imetään yleistilanne COVID19Py-kirjaston kautta
#Tämä siksi että THL ei tarjoa API:n kautta kuolemien määrää ja en jaksa opetella uuden API:n dimensioita ja toimintaa
def Yleiskatsaus():
    os.system('clear')
    print("\n")
    print("*" * 20)
    print("    Yhteenveto")
    print("*" * 20)
    print("\n")
    covid19 = COVID19Py.COVID19(data_source="jhu")
    data = covid19.getLocationByCountryCode("FI")
    fulldata = data[0]
    latest = fulldata['latest']
    tapaukset = "Vahvistetut COVID-19 tapaukset Suomessa: " + str(latest["confirmed"])
    kuolemat = "Vahvistetut COVID-19 kuolemat Suomessa: " + str(latest["deaths"])
    yhteenveto = tapaukset + "\n" + kuolemat
    print(yhteenveto)


# Rakennetaan requestit caseja varten
tartunnat = ("https://sampo.thl.fi/pivot/prod/fi/epirapo/covid19case/fact_epirapo_covid19case.json?column=ttr10yage-444309")
req = urllib.request.Request(
    tartunnat, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

#Imetään response
response = urllib.request.urlopen(req)
fulldata = json.loads(response.read())
#Aliohjelma jossa käsitellään API:n vastaus
def TapauksetByAge():
    os.system('clear')
    print("\n")
    print("*" * 20)
    print("Tapaukset iän mukaan")
    print("*" * 20)
    print("\n")
    dataset = fulldata['dataset']
    value = dataset['value']
    luvut = value.items()
    categories = ["0-10v","10-20v","20-30v","30-40v","40-50v","50-60v","60-70v","70-80v","80v+", "Tapauksia yhteensä"]
    x=0
    while x < 8:
        for item in luvut:
            print(categories[x] + ": " + item[1])
            x=x+1
            

#Main program
vastaus = ''
Titlebar()
while vastaus != 'q':
    vastaus = getChoice()
    if vastaus == "1":
        Yleiskatsaus()
    elif vastaus == "2":
        TapauksetByAge()
    elif vastaus == "3":
        os.system('clear')
        print("Coming soon... (aka when I learn how matplotlib works)")
    elif vastaus == "0":
        print("Suljetaan ohjelma ...")
        quit()

