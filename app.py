from flask import Flask
import telegram

app = Flask(__name__)

TOKEN = '6926950017:AAEjcggDcurUZ-j2H4SgRglTG4mZjTNsJo4'
bot = telegram.bot(TOKEN)
chat_id = '5534265722'

@app.route('/', methods=['POST'])
def index():
    print('index page')
    bot.send_message(chat_id=chat_id, text='Hello World!!!')
    return 'index page'