import logging
#import Config
import Responses as Respuestas
from telegram.ext import *
import time 
print("....")

logger = logging.getLogger()

def start_command(update, context):
    print(f"El usuario {update.effective_user['username']} mando mensaje")
    name = update.effective_user['first_name']    
    update.message.reply_text(f"Hola {name}")

def help_command(update, context):
    update.message.reply_text("No tengo soporte de ayuda")
    
def handle_message(update, context):
    text = str(update.message.text)
    respuesta = Respuestas.saludo(text)    
    update.message.reply_text(respuesta)
    
def precioBTC_Command(update, context):
    time.sleep(10)
    update.message.reply_text(f"El precio es de ....")
    
def error(update, context):
    print(f"Update {update} causado por {context.error}")
    
def main():
    updater = Updater("1904691009:AAEMFpySeateKXjHJ-geIfyHJFdVQ1EesWs", use_context=True)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("precioBTC", precioBTC_Command))
    
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
    
    dispatcher.add_error_handler(error)    
    updater.start_polling()
    updater.idle()
    

main()
