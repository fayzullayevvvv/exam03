from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

from .ImageService import fetch_random_image


def start_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=f"<b>Assalomu alaykum {update.message.from_user.first_name}!</b>",
        parse_mode="HTML",
    )

    keyboard = [
        [
            InlineKeyboardButton("🐶 Dog", callback_data="dog"),
            InlineKeyboardButton("🐱 Cat", callback_data="cat"),
            InlineKeyboardButton("🦊 Fox", callback_data="fox"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("Tanlang:", reply_markup=reply_markup)

def send_image(update: Update, context: CallbackContext, animal: str):
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=fetch_random_image(animal))

def dog_command(update: Update, context: CallbackContext):
    send_image(update, context, "dog")

def cat_command(update: Update, context: CallbackContext):
    send_image(update, context, "cat")

def fox_command(update: Update, context: CallbackContext):
    send_image(update, context, "fox")

def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    data = query.data
    if data == "dog":
        dog_command(update, context)
    elif data == "cat":
        cat_command(update, context)
    elif data == "fox":
        fox_command(update, context)

    keyboard = [
        [
            InlineKeyboardButton("🐶 Dog", callback_data="dog"),
            InlineKeyboardButton("🐱 Cat", callback_data="cat"),
            InlineKeyboardButton("🦊 Fox", callback_data="fox"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query.message.reply_text("Tanlang:", reply_markup=reply_markup)

def handle_text(update: Update, context: CallbackContext):
    text = update.message.text.lower()
    if text == "dog":
        dog_command(update, context)
    elif text == "cat":
        cat_command(update, context)
    elif text == "fox":
        fox_command(update, context)