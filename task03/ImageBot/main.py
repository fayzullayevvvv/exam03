from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

from .Handlers import start_command, dog_command, cat_command, fox_command, button_handler, handle_text
from .config import settings


def main() -> None:
    updader = Updater(settings.token)
    dispatcher = updader.dispatcher

    dispatcher.add_handler(CommandHandler(command="start", callback=start_command))
    dispatcher.add_handler(CommandHandler(command="dog", callback=dog_command))
    dispatcher.add_handler(CommandHandler(command="cat", callback=cat_command))
    dispatcher.add_handler(CommandHandler(command="fox", callback=fox_command))

    dispatcher.add_handler(CallbackQueryHandler(button_handler))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

    updader.start_polling()
    updader.idle()
