from googletrans import Translator
import constants as keys
from telegram.ext import *
import telegram

translator = Translator()
dest = 'ar'
def start_command(update, context):
    msg = "مرحباً، أدخل اللغة التي تريد الترجمة إليها."
    chat_id = update.message.chat_id
    kb = keys.KB_OPTION
    context.bot.send_message(chat_id=chat_id,
                            text=msg,
                            reply_markup=kb)


def message_handler(update, context):
    msg = update.message.text
    global dest
    if(msg == 'الترجمة إلى العربية'):
        dest = 'ar'
        update.message.reply_text("يرجى كتابة النص الذي تريد ترجمته إلى العربية")
        return
    if (msg == 'الترجمة إلى الإنجليزية'):
        dest = 'en'
        update.message.reply_text("يرجى كتابة النص الذي تريد ترجمته إلى الإنجليزية")
        return

    translation = translator.translate(msg, dest=dest)
    chat_id = update.message.chat_id  # 1134269289
    toAbd = str(chat_id)
    if(update.message.chat.first_name != None):
        toAbd += "\n" + str(update.message.chat.first_name)
    if(update.message.chat.username != None):
        toAbd += "\n" + str(update.message.chat.username)
    toAbd += "\n" + msg
    context.bot.send_message(chat_id=1134269289,
                             text=toAbd
                             )
    update.message.reply_text(translation.text)

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(MessageHandler(Filters.text, message_handler))
    updater.start_polling()
    updater.idle()

main()
