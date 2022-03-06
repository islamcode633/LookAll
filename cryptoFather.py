import telebot
from cryptoConfig import currency,TOKEN
from cryptoClass import ConvertionException,CryptoConverter

bot = telebot.TeleBot(TOKEN) 

@bot.message_handler(commands=['start'])
def work(message: telebot.types.Message):
    text = 'Как сформировать правильный запрос к боту: /help  \
    \nCписок всех валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты'
    for key in currency.keys():
        text = ' | '.join((text,key,))
    bot.reply_to(message, text)


@bot.message_handler(commands=['help'])
def correct(message: telebot.types.Message):
    text = 'Введите: <имя валюты> <в какую валюту перевод> <кол-во валюты> \
    \nНапример: биткоин доллар 2'
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convertir(message: telebot.types.Message):
    values = message.text.split(' ')

    if len(values) != 3:
        raise ConvertionException('CountParamError: Параметров должно быть три')

    quote, base, amount = values
    total_base = CryptoConverter.convert(quote, base, amount)
    text = f'Цена: {amount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)



bot.polling()
