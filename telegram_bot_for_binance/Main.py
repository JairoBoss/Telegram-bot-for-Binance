import Config
import Responses as Respuestas
from telegram.ext import *
 
print("....")

def start_command(update, context):
    update.message.reply_text("Hola, escribe algo")

def help_command(update, context):
    update.message.reply_text("No tengo soporte de ayuda")
    
def handle_message(update, context):
    text = str(update.message.text)
    respuesta = Respuestas.saludo(text)
    
    update.message.reply_text(respuesta)
    
def error(update, context):
    print(f"Update {update} causado por {context.error}")
    
def main():
    updater = Updater(Config.API_KEY_TELEGRAM, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
    

main()