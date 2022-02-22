from telegram.ext import Updater,CommandHandler
import ephem
def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def main():
    
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater("5084818916:AAFyboNKygsu25nAZ35IHk_-rKGzbstG6MA", use_context=True)
    # Командуем боту начать ходить в Telegram за сообщениями
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()

main()