import datetime, dateutil
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from finaltraininng.models import User, Training, Trainer, Prize, Abon, Order, Wallet
import telebot
from telebot import types
from decimal import Decimal, DecimalException

config = {
    'name': 'Jackyficj_bot',
    'token': '5629735612:AAGM5LsvmjVBhKPfedmYBJtUW5SN0fIm-jg'
}
buy_verfy = False
bot = telebot.TeleBot(config['token'])
keybord = types.ReplyKeyboardMarkup(resize_keyboard=True)
keybord1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
button2 = types.KeyboardButton('Train')
button3 = types.KeyboardButton('Basket')
button4 = types.KeyboardButton('Pay/buy')
button5 = types.KeyboardButton('Addmoney')
button6 = types.KeyboardButton('Abonum')

keybord.add(button2, button3, button4, button5, button6)
@bot.message_handler(commands=['start', 'cart', 'payorder'])
def start(message):
        bot.send_message(message.chat.id, 'Menu: ', reply_markup=keybord)
        if not User.objects.filter(userid=message.chat.id):
            User.objects.get_or_create(
                userid=message.chat.id,
            )
            Wallet.objects.get_or_create(
                userid=User.objects.get(userid=message.chat.id),
            )
@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == "Train":
        prod = ""
        for i in Training.objects.all():
            prod = prod + f'Training - {i.Name},<Short Info - {i.Info} \n'
        bot.send_message(message.chat.id, prod)
    elif message.text == "Abonum":
        keyboard = types.InlineKeyboardMarkup()
        for i in Abon.objects.all():
            button = types.InlineKeyboardButton(f'Name - {i.Name} \n', callback_data=i.Name)
            keyboard.add(button)
        bot.send_message(message.chat.id, "Choose training", reply_markup=keyboard)
    elif message.text == "Basket":
        costmark, costmark1 = 0, 0
        inf = ""
        for y1 in Order.objects.filter(userid__userid=message.chat.id):
            inf = inf + f' Abonument - {y1.prodid.Name}\n Trainer - {y1.prodid.trainin.Name}\n ' \
                        f'Training - {y1.prodid.trainerin.Name}\n Prize - {y1.prodid.prizein.Name}\n -----------------\n'
            costmark += y1.prodid.prizein.Prize
            costmark1 += y1.prodid.prizein.Prize2
        bot.send_message(message.chat.id, inf)
        bot.send_message(message.chat.id, f'Prize for day - {costmark}, for month - {costmark1}')
    elif message.text == "Pay/buy":
        keybord1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton('Day')
        button7 = types.KeyboardButton('Month')
        keybord1.add(button, button7)
        y = bot.send_message(message.chat.id, "Choose day or year", reply_markup=keybord1)
        bot.register_next_step_handler(y, buyabon)
    elif message.text == "Addmoney":
        y = bot.send_message(message.chat.id, 'Enter cost of money')
        bot.register_next_step_handler(y, addmoney)
def buyabon(message):
    temp = str
    temp = message.text
    costmark = 0
    user = Wallet.objects.get(userid__userid=message.chat.id)
    for y in Order.objects.filter(userid__userid=message.chat.id):
        if temp == "Day":
            costmark += y.prodid.prizein.Prize
        elif temp == "Month":
            costmark += y.prodid.prizein.Prize2
    if user.balance < costmark:
        s = bot.send_message(message.chat.id, f'You dont have still money', reply_markup=keybord)
    else:
        user.balance -= costmark
        user.save()
        s = bot.send_message(message.chat.id, f'Operation done! {user.balance}', reply_markup=keybord)
        bot.register_next_step_handler(s, deleteinf)
def addmoney(message):
    try:
        user = Wallet.objects.filter(userid__userid=message.chat.id)[0]
        user.balance +=Decimal(message.text)
        user.save()
    except DecimalException:
        bot.send_message(message.chat.id, 'Non Digit')
    else:
        bot.send_message(message.chat.id, f'Cost adds, cost on balance - {user.balance}')
def deleteinf(message, *args, **options):
    temp = message.text
    ttime = timedelta
    if temp == "Day":
        for i in Order.objects.filter(date=+relativedelta(days=1)):
            i.delete()
    elif temp == "Month":
        for i in Order.objects.filter(date=message.chat.id + relativedelta(months=+1)):
            i.delete()
    bot.send_message(message.chat.id, f'Abunument for {temp}, late is {ttime}')
    bot.send_message(message.chat.id, "Operation done!")
@bot.callback_query_handler(func=lambda call:True)
def callback_data(call):
    if call.data:
        a=Order.objects.get_or_create(
            userid=User.objects.get(userid=call.message.chat.id),
            prodid=Abon.objects.get(Name=call.data),
            date=datetime.datetime.now()
        )
        bot.send_message(call.message.chat.id, f'Product {call.data} add for order and basket!', reply_markup=keybord)
bot.polling(none_stop=True, interval=0)