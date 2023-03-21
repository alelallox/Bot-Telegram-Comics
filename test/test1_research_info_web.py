






"""
import requests
from bs4 import BeautifulSoup
# Effettuiamo una richiesta GET alla pagina contenente l'elenco degli ultimi fumetti in uscita
r = requests.get("https://mangayo.it/10-novita?order=product.date_add.desc&q=Categorie-Manga")

# Utilizziamo BeautifulSoup per analizzare il codice HTML ricevuto dalla richiesta
contenuto = BeautifulSoup(r.text, 'html.parser')

# Ciclo for per cercare ogni fumetto nella lista
fumetti_cercati = ["Tokyo Revengers", "Game Of Familia", "My Hero Academia", "Dr. Stone", "Four Knights Of The Apocalypse"]
trovato = False

for fumetto in fumetti_cercati:
    title_element = contenuto.find("h3", class_="h3 product-title", text=lambda t: fumetto in t)
    if title_element:
        trovato = True
        testoUscita = title_element.text + " è in uscita questa settimana!"
        print(testoUscita)
        
if not trovato:
    testoUscita="Nessun nuovo fumetto in uscita."
    print(testoUscita)"""


import requests
from bs4 import BeautifulSoup

# Creiamo una lista contenente gli url delle pagine
url_pagine = ["https://mangayo.it/10-novita?order=product.date_add.desc&q=Categorie-Manga", "https://mangayo.it/10-novita?order=product.date_add.desc&q=Categorie-Manga&page=2", "https://mangayo.it/10-novita?order=product.date_add.desc&q=Categorie-Manga&page=3"]

# Ciclo for per cercare ogni fumetto nella lista
fumetti_cercati = ["Tokyo Revengers", "Game Of Familia", "My Hero Academia", "Dr. Stone", "Four Knights Of The Apocalypse"]
trovato = False

# Ciclo for per analizzare ogni pagina
for url in url_pagine:
    # Effettuiamo una richiesta GET alla pagina contenente l'elenco degli ultimi fumetti in uscita
    r = requests.get(url)

    # Utilizziamo BeautifulSoup per analizzare il codice HTML ricevuto dalla richiesta
    contenuto = BeautifulSoup(r.text, 'html.parser')

    for fumetto in fumetti_cercati:
        title_element = contenuto.find("h3", class_="h3 product-title", text=lambda t: fumetto in t)
        if title_element:
            trovato = True
            testoUscita = title_element.text + " è in uscita questa settimana!"
            print(testoUscita)
    
if not trovato:
    testoUscita ="Nessun nuovo fumetto in uscita."
    print(testoUscita)




"""
# Effettuiamo una richiesta GET alla pagina contenente l'elenco degli ultimi fumetti in uscita
r = requests.get("https://www.starcomics.com/uscite")

# Utilizziamo BeautifulSoup per analizzare il codice HTML ricevuto dalla richiesta
contenuto = BeautifulSoup(r.text, 'html.parser')

# Ciclo for per cercare ogni fumetto nella lista
fumetti_cercati = ["MY HERO ACADEMIA", "DR.STONE", "FOUR KNIGHTS OF THE APOCALYPSE"]
trovato = False

for fumetto in fumetti_cercati:
    title_element = contenuto.find("h4", class_="card-title mb-0", text=lambda t: fumetto in t)
    if title_element:
        trovato = True
        testoUscita = title_element.text + " è in uscita questa settimana!"
        
if not trovato:
    testoUscita="Nessun nuovo fumetto in uscita."
"""