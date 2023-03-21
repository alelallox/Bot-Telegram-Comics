import asyncio
import logging
import requests
import schedule
import time
from bs4 import BeautifulSoup 
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackContext

async def invia_notifica(update, context, testoUscita):
    print("importante") 
    # Invia un messaggio all'utente con il testo contenuto in testoUscita
    await context.bot.send_message(chat_id=update.effective_chat.id, text=testoUscita)


def cerca_fumetti(update, context):
    print("5")
    # codice per la ricerca dei fumetti
    # Creiamo una lista contenente gli url delle pagine
    url_pagine = ["https://mangayo.it/10-novita?order=product.date_add.desc&q=Categorie-Manga", "https://mangayo.it/10-novita?order=product.date_add.desc&q=Categorie-Manga&page=2", "https://mangayo.it/10-novita?order=product.date_add.desc&q=Categorie-Manga&page=3"]

    # Ciclo for per cercare ogni fumetto nella lista
    fumetti_cercati = ["Tokyo Revengers", "Game Of Familia", "My Hero Academia", "Dr. Stone", "Four Knights Of The Apocalypse", "Detective Conan"]
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
                invia_notifica(update, context, testoUscita)
       
        if not trovato:
            testoUscita ="Nessun nuovo fumetto in uscita."
            print(testoUscita)
    #invia_notifica(update, context, testoUscita)


def pianificazione_notifiche(update, context):
    print("4")
    schedule.every(30).seconds.do(lambda: cerca_fumetti(update,context))

    while True:
        schedule.run_pending()
        time.sleep(1)

# Configuriamo il logger per mostrare informazioni di debug sullo standard output
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
print("1")
# Creiamo un'istanza di ApplicationBuilder e configuriamo il token del bot
if __name__ == '__main__':
    application = ApplicationBuilder().token("5855659161:AAFGvgcSh4XzP8s1iUC0uSEqDOqSW1rb0CQ").build()
print("2")
# Definiamo la funzione start che verrà richiamata quando l'utente invia il comando /start
async def start(update, context): 
    # Invia un messaggio all'utente 
    await context.bot.send_message(chat_id=update.effective_chat.id, text="benvenuto nel mio bot")
    print("3")
    pianificazione_notifiche(update, context)
    
# Aggiungiamo un CommandHandler per gestire il comando /start
start_handler = CommandHandler('start', start)
application.add_handler(start_handler)
    
# Avviamo il polling del bot
application.run_polling()











