import asyncio
import logging
import requests
import schedule
import time
from bs4 import BeautifulSoup 
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackContext

def schedulazione(update, context, testoUscita2):
    testoUscita2 = cerca_fumetti()
    invia_notifica(update, context, testoUscita2)


def invia_notifica(update, context, testoUscita2):
    print("funzione invia_notifica richiamata")
    bot.send_message(chat_id=update.effective_chat.id, text=testoUscita2)

def cerca_fumetti():
    print("funzione cerca_fumetti richiamata")
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
       
    if not trovato:
        testoUscita ="Nessun nuovo fumetto in uscita."
        print(testoUscita)
    return testoUscita
    

# Definiamo la funzione start che verrà richiamata quando l'utente invia il comando /start
def start(update, context):
    print("funzione start richiamata")
    # Invia un messaggio all'utente 
    bot.send_message(chat_id=update.effective_chat.id, text="benvenuto nel mio bot")
    print("messaggio di benvenuto inviato")
    testoUscita2 = " "

    schedule.every(30).seconds.do(lambda: schedulazione(update,context,testoUscita2))

    # Loop principale per eseguire il job
    while True:
        schedule.run_pending()
        time.sleep(1)
    print("fine codice")



# Configuriamo il logger per mostrare informazioni di debug sullo standard output
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
print("logger configurato")
# Creiamo un'istanza di ApplicationBuilder e configuriamo il token del bot
if __name__ == '__main__':
    bot = Bot(token="5855659161:AAFGvgcSh4XzP8s1iUC0uSEqDOqSW1rb0CQ")
print("istanza con token creata")


    
# Aggiungiamo un CommandHandler per gestire il comando /start
start_handler = CommandHandler('start', start)
print("1")
dispatcher = bot.dispatcher
dispatcher.add_handler(start_handler)
print("2")
bot.run_polling()




