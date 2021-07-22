import logging
import Files
import BinanceAccount
import Responses as Respuestas
from telegram.ext import *
import time 
print("....")

logger = logging.getLogger()
cuenta = BinanceAccount.Binance()
file = Files.Controller()
APIS = file.openFile()

def start_command(update, context):
    print(f"El usuario {update.effective_user['username']} mando mensaje")
    name = update.effective_user['first_name']    
    update.message.reply_text(f"Hola {name}")
    update.message.reply_text(f"Actualmente este bot esta en desarollo, el link del proyecyo es el siguiente")
    update.message.reply_text(f"https://github.com/JairoBoss/Telegram-bot-for-Binance")
    

def help_command(update, context):
    update.message.reply_text("No tengo soporte de ayuda")
    
def handle_message(update, context):
    text = str(update.message.text)
    respuesta = Respuestas.saludo(text)    
    update.message.reply_text(respuesta)
    
def precioBTC_Command(update, context):
    update.message.reply_text(f"El precio es actual de BTC es de: {cuenta.cryptoPrice()}, te lo enviaremos de nuevo en 5")
    time.sleep(5)
    update.message.reply_text(f"El precio es actual de BTC es de: {cuenta.cryptoPrice()}")
    
def error(update, context):
    print(f"Update {update} causado por {context.error}")
    
def main():
    print(file.getKey(APIS[0]))
    updater = Updater(file.getKey(APIS[0]), use_context=True)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("precioBTC", precioBTC_Command))
    
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
    
    dispatcher.add_error_handler(error)    
    updater.start_polling()
    updater.idle()
    

main()
