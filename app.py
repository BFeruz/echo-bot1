from flask import Flask, request
import telegram

app = Flask(__name__)

TOKEN = '6926950017:AAEjcggDcurUZ-j2H4SgRglTG4mZjTNsJo4'
bot = telegram.Bot(TOKEN)
chat_id = '5534265722'

@app.route('/', methods=['POST'])
def user():
    data = request.get_json() 
    print(data)
    bot.send_message(chat_id=chat_id, text='Hello!!')
    return 'join'
if __name__=="__main__":
    app.run(debug=True)