from config import bot_token
import logging
from telegram.ext import Updater, CommandHandler

# bot setup
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


# bot response functions
def start_command(update, context):
    message = "Hi welcome to my bot , the bot is still in development so some of the functions are not available"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def help_command(update, context):
    message = "The help menu is still in development"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


# create handlers
start_handler = CommandHandler(command='start', callback=start_command)
help_handler = CommandHandler(command='help', callback=help_command)
# register handlers
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)

# start the Bot
updater.start_polling()
