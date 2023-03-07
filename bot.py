import os
from telegram.ext import Updater, CommandHandler

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm a bot.")

def main():
    token = os.environ.get('6201719090:AAHVmrXtpwRTD31h2XZtvF29S8sVr2VTOj8')
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
