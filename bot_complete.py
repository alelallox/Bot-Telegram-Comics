#library import
import logging
import requests
import time
from bs4 import BeautifulSoup  
from telegram.ext import ApplicationBuilder, CommandHandler

#Definition of the function "all_functions", that call all function 
async def all_functions(update, context, testoUscita2):
    testoUscita2 = search_comics()
    await send_notification(update, context, testoUscita2)

#Definition of the function "send_notification", that send a notification message to the user
async def send_notification(update, context, testoUscita2):
    print("funzione invia_notifica richiamata")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=testoUscita2)

#Definition of the function "search_comics", that analyze html pages to search for comics with the library BeautifulSoup
def search_comics():
    print("funzione cerca_fumetti richiamata")

    url_pagine = ["https://mangayo.it/10-novita?order=product.date_add.desc&q=Categorie-Manga", "https://mangayo.it/10-novita?order=product.date_add.desc&q=Categorie-Manga&page=2", "https://mangayo.it/10-novita?order=product.date_add.desc&q=Categorie-Manga&page=3"]

    fumetti_cercati = ["Tokyo Revengers", "Game Of Familia", "My Hero Academia", "Dr. Stone", "Four Knights"]
    trovato = False

    for url in url_pagine:
        r = requests.get(url)
        contenuto = BeautifulSoup(r.text, 'html.parser')

        for fumetto in fumetti_cercati:
            title_element = contenuto.find("h3", class_="h3 product-title", text=lambda t: fumetto in t)
            if title_element:
                trovato = True
                testoUscita = title_element.text + " è in uscita questa settimana!"
                print("-------------------------------")
                print(testoUscita)
                print("-------------------------------")
       
    if not trovato:
        testoUscita ="Nessun nuovo fumetto in uscita."
        print("-------------------------------")
        print(testoUscita)
        print("-------------------------------")
    return testoUscita
    
#Definition of the function "search_comics",that will be called when the user sends the /start command
async def start(update, context):
    print("funzione start richiamata") 
    await context.bot.send_message(chat_id=update.effective_chat.id, text="benvenuto nel mio bot")
    print("messaggio di benvenuto inviato")
    testoUscita2 = " "
    booleana = True 
    while(booleana == True):
        time.sleep(3600)
        await all_functions(update, context, testoUscita2)


#Configure the logger to show debugging information on standard output
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
print("logger configurato")
#Create an ApplicationBuilder instance and configure the bot token
if __name__ == '__main__':
    application = ApplicationBuilder().token("5855659161:AAFGvgcSh4XzP8s1iUC0uSEqDOqSW1rb0CQ").build()
print("istanza con token creata")
   
#Add a CommandHandler to manage the /start command
start_handler = CommandHandler('start', start)
application.add_handler(start_handler)
application.run_polling()
