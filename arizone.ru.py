from re import M
from aiogram import Dispatcher, executor
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import CallbackQuery, Message
import urllib.parse
import urllib.request
import ssl
import time
import ftplib
"""
host = 'ruvip51.hostiman.ru'
ftp_user = 'cicada'
ftp_password = 'Tramadol1989!'

ftp = ftplib.FTP(host, ftp_user, ftp_password)
 
welcome = ftp.getwelcome() 
print(welcome)

ftp.cwd("www/arizone.ru/")

ftp_file = 'index.html'
local_file = 'index.html'
file = "index.html"
with open(local_file, 'wb') as local_file: 
    ftp.retrbinary('retr ' + ftp_file, local_file.write) 

ssl._create_default_https_context = ssl._create_unverified_context

site = "http://arizone.ru"


url = urllib.parse.quote_plus(site)
width = 1920
height = 1080
output = "image"
"""
ssl._create_default_https_context = ssl._create_unverified_context

site = "http://arizone.ru"


url = urllib.parse.quote_plus(site)
width = 1920
height = 1080
output = "image"
token = "J2R5PZN-34Q4J42-JPTRJD4-Y9F6BHT"
bot = Bot(token="5277009385:AAFw-LUouS4qHJ7sS_iDI3sKYKGKLyvesYU", parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class sms13(StatesGroup):
    sms_text = State()

class sms12(StatesGroup):
    sms_text = State()

class sms11(StatesGroup):
    sms_text = State()

class sms10(StatesGroup):
    sms_text = State()

class sms9(StatesGroup):
    sms_text = State()

class sms8(StatesGroup):
    sms_text = State()

class sms7(StatesGroup):
    sms_text = State()

class sms6(StatesGroup):
    sms_text = State()

class sms5(StatesGroup):
    sms_text = State()

class sms4(StatesGroup):
    sms_text = State()

class sms3(StatesGroup):
    sms_text = State()

class sms2(StatesGroup):
    sms_text = State()



xxx = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📱 Оператор", callback_data="oper"),
            InlineKeyboardButton(text="💡 Техпродажи", callback_data="tex"),
            InlineKeyboardButton(text="🤖 Бот", callback_data="bbb")
        ],

        [
            InlineKeyboardButton(text="🐍 Hudra", callback_data="hudra"),
            InlineKeyboardButton(text="💰 Работа", callback_data="rab"),
            InlineKeyboardButton(text="💵 Работа WhatsApp", callback_data="whatsApp")
        ],

        [
            InlineKeyboardButton(text="🖇 Резерв", callback_data="rezerv"),
            InlineKeyboardButton(text="🎟 Legal", callback_data="leg"),
            InlineKeyboardButton(text="📖 Отзывы", callback_data="otz")
        ],

        [
            InlineKeyboardButton(text="🏙 Фон сайта", callback_data="fon"),
            InlineKeyboardButton(text="🎆 Логотип", callback_data="logot"),
            InlineKeyboardButton(text="📝 Виджет", callback_data="widjet")
        ],

        [
            InlineKeyboardButton(text="🚑 Востановить", callback_data="news")
        ]
    ]
)


@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer("<b>Загружаю сайт ожидай....</b>")
    host = 'ruvip51.hostiman.ru'
    ftp_user = 'cicada'
    ftp_password = 'Tramadol1989!'

    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    
    ftp.cwd("www/arizone.ru/")

    ftp_file = 'index.html'
    local_file = 'index.html'
    file = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write) 
    chat_id = message.chat.id
    with open ('index.html', 'r') as f:
      old_data = f.readlines()
      tt = old_data[518]
      tat = tt.split('"')
      otziv = tat[7]
      tt1 = old_data[505]
      tat1 = tt1.split('"')
      legal = tat1[7]
      tt2 = old_data[497]
      tat2 = tt2.split('"')
      rez = tat2[7]
      tt3 = old_data[481]
      tat3 = tt3.split('"')
      wc = tat3[7]
      tt4 = old_data[474]
      tat4 = tt4.split('"')
      rabota = tat4[7]
      tt5 = old_data[459]
      tat5 = tt5.split('"')
      gidra = tat5[7]
      tt6 = old_data[452]
      tat6 = tt6.split('"')
      bbboot = tat6[7]
      tt7 = old_data[439]
      tat7 = tt7.split('"')
      texx = tat7[1]
      tt8 = old_data[430]
      tat8 = tt8.split('"')
      oer = tat8[7]
    query = "https://shot.screenshotapi.net/screenshot"
    query += "?token=%s&url=%s&width=%d&height=%d&output=%s" % (token, url, width, height, output)
    urllib.request.urlretrieve(query, "./screenshot.png")
    with open("screenshot.png", 'rb') as f:
      foto = f.read()
    cap = "<b>Так Выглядит Сайт</b>"
    await bot.send_photo(chat_id, foto, caption=cap)
    time.sleep(4)
    await message.answer(
      f"<b>Пример сайта онлаин тут: </b>\n\n"
      f"http://arizone.ru\n"
      f"<b>Сейчас Установлены такие контакты: </b>\n\n"
      f"<b>📱 Оператор:</b>  <code>{oer}</code>\n"
      f"<b>💡 Техпродажи:</b> <code>{texx}</code>\n"
      f"<b>🤖 Бот:</b>  <code>{bbboot}</code>\n"
      f"<b>🐍 Hudra:</b>  <code>{gidra}</code>\n"
      f"<b>💰 Работа:</b> <code>{rabota}</code>\n"
      f"<b>💵 Работа WhatsApp:</b>  <code>{wc}</code>\n"
      f"<b>🖇 Резерв:</b> <code>{rez}</code>\n"
      f"<b>🎟 Legal:</b>  <code>{legal}</code>\n"
      f"<b>📖 Отзывы:</b> <code>{otziv}</code>\n\n"
      f"<b>Изменение контактов</b>", reply_markup=xxx)
    file_to_upload = open(file, 'rb')
    ftp.storbinary('STOR ' + file, file_to_upload)

    ftp.close()


@dp.callback_query_handler(text="widjet", state="*")
async def widjet(call: CallbackQuery, state: FSMContext):
    await call.message.answer(
      f"<b>Для Установки Виджета </b>\n"
      f"<b>1. Нужно иметь Публичный Канал либо Группу</b>\n"
      f"<b>Добавить в канал или группу бота @tgwidgetgroup_bot</b>\n"
      f"<b>И начать с ним диалог он даст ссылку, перейти по ней</b>\n"
      f"<b>Для активации бота для трансляции на сайт</b>\n"
      f"<b>2. Перейти на Сайт создания <a href='https://tgwidget.com/'>виджета</a></b>\n"
      f"<b>Нажать получить новый Виджет</b>\n"
      f"<b>Ввести username канала в таком формате @username</b>\n"
      f"<b>В появившемся окне скопировать код</b>\n"
      f"<b>нужного вам виджета и отправить сюда</b>\n"
      f"<b>Если нужно убрать виджет отправь мне '-'</b>")
    await sms13.sms_text.set()

    @dp.message_handler(state=sms13.sms_text)
    async def widjet(message: Message,  state: FSMContext):
        await message.answer("<b>Идет Обновления Данных Сайта....</b>")
        chat_id = message.chat.id
        data = await state.get_data()
        sms = message.text
        nonwidjet = '<!-- <iframe id="tgw_6228fffaa05ecf3a2f3eb723" frameborder="0" scrolling="no" horizontalscrolling="no" verticalscrolling="no" width="100%" height="540px" async></iframe><script>document.addEventListener("DOMContentLoaded",function(){document.getElementById("tgw_6228fffaa05ecf3a2f3eb723").setAttribute("src","https://tgwidget.com/channel/v2.0/?id=6228fffaa05ecf3a2f3eb723")})</script>-->'
        if sms == '-':
            sms = nonwidjet
        host = 'ruvip51.hostiman.ru'
        ftp_user = 'cicada'
        ftp_password = 'Tramadol1989!'

        ftp = ftplib.FTP(host, ftp_user, ftp_password)
        
        ftp.cwd("www/arizone.ru/")

        ftp_file = 'index.html'
        local_file = 'index.html'
        file = "index.html"
        with open(local_file, 'wb') as local_file: 
            ftp.retrbinary('retr ' + ftp_file, local_file.write)
        with open ('index.html', 'r') as f:
          old_data = f.readlines()
          tt = old_data[527]
          with open ('index.html', 'r') as f:
            old_data = f.read()
            new_data = old_data.replace(tt, sms)
          with open ('index.html', 'w') as f:
            f.write(new_data)
          file_to_upload = open(file, 'rb')
          ftp.storbinary('STOR ' + file, file_to_upload)

          ftp.close()
          query = "https://shot.screenshotapi.net/screenshot"
          query += "?token=%s&url=%s&width=%d&height=%d&output=%s" % (token, url, width, height, output)
          urllib.request.urlretrieve(query, "./screenshot.png")
          with open("screenshot.png", 'rb') as f:
            foto = f.read()
          cap = (
            f"<b>Даные по Виджету Обновлены !</b>\n"
            f"<b>Посмотреть как выглядит: </b>\n\n"
            f"http://arizone.ru\n"
          )
          await bot.send_photo(chat_id, foto, caption=cap, reply_markup=xxx)


@dp.callback_query_handler(text="news", state="*")
async def news(call: CallbackQuery, state: FSMContext):
    chat_id = call.message.chat.id
    host = 'ruvip51.hostiman.ru'
    ftp_user = 'cicada'
    ftp_password = 'Tramadol1989!'

    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    
    ftp.cwd("www/arizone.ru/")
    await call.message.answer("<b>Идет Востановление Данных Сайта....</b>")
    file = "recovery.html"
    
    file_to_upload = open(file, 'rb')
    ftp.storbinary('STOR ' + file, file_to_upload)

    ftp.close()
    query = "https://shot.screenshotapi.net/screenshot"
    query += "?token=%s&url=%s&width=%d&height=%d&output=%s" % (token, url, width, height, output)
    urllib.request.urlretrieve(query, "./screenshot.png")
    with open("screenshot.png", 'rb') as f:
      foto = f.read()
    cap = (
      f"<b>Сайт успешно востановлен !</b>\n"
      f"<b>Посмотреть как выглядит: </b>\n\n"
      f"http://arizone.ru\n"
    )
    await bot.send_photo(chat_id, foto, caption=cap, reply_markup=xxx)



@dp.callback_query_handler(text="logot", state="*")
async def logot(call: CallbackQuery, state: FSMContext):
    host = 'ruvip51.hostiman.ru'
    ftp_user = 'cicada'
    ftp_password = 'Tramadol1989!'

    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    
    ftp.cwd("www/arizone.ru/")

    ftp_file = 'index.html'
    local_file = 'index.html'
    file = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    with open ('index.html', 'r') as f:
      old_data = f.readlines()
      tt = old_data[413]
      tat = tt.split('"')
      zc = tat[29][22:-2]
    await sms12.sms_text.set()
    await call.message.answer(
      f"<b>Сейчас установлен {zc}</b>\n\n"
      f"<b>Введи сылку на изображение в таком формате http://image.jpg </b>")
    

    @dp.message_handler(state=sms12.sms_text)
    async def logot(message: Message,  state: FSMContext):
        chat_id = message.chat.id
        data = await state.get_data()
        sms = message.text
        print(sms[-3:])
        if sms[-3:] == "png":
          await message.answer("<b>Идет Обновления Данных Сайта....</b>")
          with open ('index.html', 'r') as f:
            old_data = f.read()
            new_data = old_data.replace(zc, sms)
          
          with open ('index.html', 'w') as f:
            f.write(new_data)
          file_to_upload = open(file, 'rb')
          ftp.storbinary('STOR ' + file, file_to_upload)

          ftp.close()
          query = "https://shot.screenshotapi.net/screenshot"
          query += "?token=%s&url=%s&width=%d&height=%d&output=%s" % (token, url, width, height, output)
          urllib.request.urlretrieve(query, "./screenshot.png")
          with open("screenshot.png", 'rb') as f:
            foto = f.read()
          cap = (
            f"<b>Логотип успешно изменен !</b>\n"
            f"<b>Посмотреть как выглядит: </b>\n\n"
            f"http://arizone.ru\n"
          )
          await bot.send_photo(chat_id, foto, caption=cap, reply_markup=xxx)

        if sms[-3:] == "jpg":
          await message.answer("<b>Идет Обновления Данных Сайта....</b>")
          with open ('index.html', 'r') as f:
            old_data = f.read()
            new_data = old_data.replace(zc, sms)
          
          with open ('index.html', 'w') as f:
            f.write(new_data)
          file_to_upload = open(file, 'rb')
          ftp.storbinary('STOR ' + file, file_to_upload)

          ftp.close()
          query = "https://shot.screenshotapi.net/screenshot"
          query += "?token=%s&url=%s&width=%d&height=%d&output=%s" % (token, url, width, height, output)
          urllib.request.urlretrieve(query, "./screenshot.png")
          with open("screenshot.png", 'rb') as f:
            foto = f.read()
          cap = (
            f"<b>Логотип успешно изменен !</b>\n"
            f"<b>Посмотреть как выглядит: </b>\n\n"
            f"http://arizone.ru\n"
          )
          await bot.send_photo(chat_id, foto, caption=cap, reply_markup=xxx)

        else:
          await call.message.answer("<b>Не верный формат</b>")


@dp.callback_query_handler(text="fon", state="*")
async def fon(call: CallbackQuery, state: FSMContext):
    host = 'ruvip51.hostiman.ru'
    ftp_user = 'cicada'
    ftp_password = 'Tramadol1989!'

    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    
    ftp.cwd("www/arizone.ru/")

    ftp_file = 'index.html'
    local_file = 'index.html'
    file = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    with open ('index.html', 'r') as f:
      old_data = f.readlines()
      tt = old_data[378]
      tat = tt.split('"')
      zc = tat[1][22:-2]
    await call.message.answer(
      f"<b>Сейчас установлен {zc}</b>\n\n"
      f"<b>Введи сылку на изображение в таком формате http://image.jpg </b>")
    await sms11.sms_text.set()

    @dp.message_handler(state=sms11.sms_text)
    async def otz(message: Message,  state: FSMContext):
        chat_id = message.chat.id
        data = await state.get_data()
        sms = message.text
        print(sms[-3:])
        if sms[-3:] == "png":
          await message.answer("<b>Идет Обновления Данных Сайта....</b>")
          with open ('index.html', 'r') as f:
            old_data = f.read()
            new_data = old_data.replace(zc, sms)
          
          with open ('index.html', 'w') as f:
            f.write(new_data)
          file_to_upload = open(file, 'rb')
          ftp.storbinary('STOR ' + file, file_to_upload)

          ftp.close()
          query = "https://shot.screenshotapi.net/screenshot"
          query += "?token=%s&url=%s&width=%d&height=%d&output=%s" % (token, url, width, height, output)
          urllib.request.urlretrieve(query, "./screenshot.png")
          with open("screenshot.png", 'rb') as f:
            foto = f.read()
          cap = (
            f"<b>Данные Сайта Обновлены !</b>\n"
            f"<b>Посмотреть как выглядит: </b>\n\n"
            f"http://arizone.ru\n"
          )
          await bot.send_photo(chat_id, foto, caption=cap, reply_markup=xxx)

        if sms[-3:] == "jpg":
          await message.answer("<b>Идет Обновления Данных Сайта....</b>")
          with open ('index.html', 'r') as f:
            old_data = f.read()
            new_data = old_data.replace(zc, sms)
          
          with open ('index.html', 'w') as f:
            f.write(new_data)
          file_to_upload = open(file, 'rb')
          ftp.storbinary('STOR ' + file, file_to_upload)
          ftp.close()
          query = "https://shot.screenshotapi.net/screenshot"
          query += "?token=%s&url=%s&width=%d&height=%d&output=%s" % (token, url, width, height, output)
          urllib.request.urlretrieve(query, "./screenshot.png")
          with open("screenshot.png", 'rb') as f:
            foto = f.read()
          cap = (
            f"<b>Данные Сайта Обновлены !</b>\n"
            f"<b>Посмотреть как выглядит: </b>\n\n"
            f"http://arizone.ru\n"
          )
          await bot.send_photo(chat_id, foto, caption=cap, reply_markup=xxx)

        else:
          await call.message.answer("<b>Не верный формат</b>")


@dp.callback_query_handler(text="otz", state="*")
async def otz(call: CallbackQuery, state: FSMContext):
    host = 'ruvip51.hostiman.ru'
    ftp_user = 'cicada'
    ftp_password = 'Tramadol1989!'

    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    
    ftp.cwd("www/arizone.ru/")

    ftp_file = 'index.html'
    local_file = 'index.html'
    file = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    with open ('index.html', 'r') as f:
      old_data = f.readlines()
      tt = old_data[518]
      tat = tt.split('"')
      otziv = tat[7]
      tt1 = old_data[505]
      tat1 = tt1.split('"')
      legal = tat1[7]
      tt2 = old_data[497]
      tat2 = tt2.split('"')
      rez = tat2[7]
      tt3 = old_data[481]
      tat3 = tt3.split('"')
      wc = tat3[7]
      tt4 = old_data[474]
      tat4 = tt4.split('"')
      rabota = tat4[7]
      tt5 = old_data[459]
      tat5 = tt5.split('"')
      gidra = tat5[7]
      tt6 = old_data[452]
      tat6 = tt6.split('"')
      bbboot = tat6[7]
      tt7 = old_data[439]
      tat7 = tt7.split('"')
      texx = tat7[1]
      tt8 = old_data[430]
      tat8 = tt8.split('"')
      oer = tat8[7]


    await call.message.answer(
      f"<b>Сейчас установлен {otziv}</b>\n\n"
      f"<b>Введи новый контакт оператора в таком формате http://t.me/username/ </b>")
    await sms10.sms_text.set()


    @dp.message_handler(state=sms10.sms_text)
    async def otz(message: Message,  state: FSMContext):
        chat_id = message.chat.id
        data = await state.get_data()
        sms = message.text
        if sms[:3] == 'htt':
          await message.answer("<b>Идет Обновления Данных Сайта....</b>")
          with open ('index.html', 'r') as f:
            old_data = f.read()
            new_data = old_data.replace(otziv, sms)
          
          with open ('index.html', 'w') as f:
            f.write(new_data)
          file_to_upload = open(file, 'rb')
          ftp.storbinary('STOR ' + file, file_to_upload)
          ftp.close()
          query = "https://shot.screenshotapi.net/screenshot"
          query += "?token=%s&url=%s&width=%d&height=%d&output=%s" % (token, url, width, height, output)
          urllib.request.urlretrieve(query, "./screenshot.png")
          with open("screenshot.png", 'rb') as f:
            foto = f.read()
          cap = (
            f"<b>Данные Сайта Обновлены !</b>\n"
            f"<b>Посмотреть как выглядит: </b>\n\n"
            f"http://arizone.ru\n"
          )
          await bot.send_photo(chat_id, foto, caption=cap, reply_markup=xxx)

        else:
          await call.message.answer("<b>Не верный формат</b>")



@dp.callback_query_handler(text="leg", state="*")
async def leg(call: CallbackQuery, state: FSMContext):
    host = 'ruvip51.hostiman.ru'
    ftp_user = 'cicada'
    ftp_password = 'Tramadol1989!'

    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    
    ftp.cwd("www/arizone.ru/")

    ftp_file = 'index.html'
    local_file = 'index.html'
    file = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    with open ('index.html', 'r') as f:
      old_data = f.readlines()
      tt = old_data[518]
      tat = tt.split('"')
      otziv = tat[7]
      tt1 = old_data[505]
      tat1 = tt1.split('"')
      legal = tat1[7]
      tt2 = old_data[497]
      tat2 = tt2.split('"')
      rez = tat2[7]
      tt3 = old_data[481]
      tat3 = tt3.split('"')
      wc = tat3[7]
      tt4 = old_data[474]
      tat4 = tt4.split('"')
      rabota = tat4[7]
      tt5 = old_data[459]
      tat5 = tt5.split('"')
      gidra = tat5[7]
      tt6 = old_data[452]
      tat6 = tt6.split('"')
      bbboot = tat6[7]
      tt7 = old_data[439]
      tat7 = tt7.split('"')
      texx = tat7[1]
      tt8 = old_data[430]
      tat8 = tt8.split('"')
      oer = tat8[7]

    await call.message.answer(
      f"<b>Сейчас установлен {legal}</b>\n\n"
      f"<b>Введи новый контакт оператора в таком формате http://t.me/username/ </b>")
    await sms9.sms_text.set()


    @dp.message_handler(state=sms9.sms_text)
    async def leg(message: Message,  state: FSMContext):
        await message.answer("<b>Идет Обновления Данных Сайта....</b>")
        chat_id = message.chat.id
        data = await state.get_data()
        sms = message.text
        with open ('index.html', 'r') as f:
          old_data = f.read()
          new_data = old_data.replace(legal, sms)
        
        with open ('index.html', 'w') as f:
          f.write(new_data)
        file_to_upload = open(file, 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        query = "https://shot.screenshotapi.net/screenshot"
        query += "?token=%s&url=%s&width=%d&height=%d&output=%s" % (token, url, width, height, output)
        urllib.request.urlretrieve(query, "./screenshot.png")
        with open("screenshot.png", 'rb') as f:
          foto = f.read()
        cap = (
          f"<b>Данные Сайта Обновлены !</b>\n"
          f"<b>Посмотреть как выглядит: </b>\n\n"
          f"http://arizone.ru\n"
        )
        await bot.send_photo(chat_id, foto, caption=cap, reply_markup=xxx)

@dp.callback_query_handler(text="rezerv", state="*")
async def rezerv(call: CallbackQuery, state: FSMContext):
    host = 'ruvip51.hostiman.ru'
    ftp_user = 'cicada'
    ftp_password = 'Tramadol1989!'

    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    
    ftp.cwd("www/arizone.ru/")

    ftp_file = 'index.html'
    local_file = 'index.html'
    file = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    with open ('index.html', 'r') as f:
      old_data = f.readlines()
      tt = old_data[518]
      tat = tt.split('"')
      otziv = tat[7]
      tt1 = old_data[505]
      tat1 = tt1.split('"')
      legal = tat1[7]
      tt2 = old_data[497]
      tat2 = tt2.split('"')
      rez = tat2[7]
      tt3 = old_data[481]
      tat3 = tt3.split('"')
      wc = tat3[7]
      tt4 = old_data[474]
      tat4 = tt4.split('"')
      rabota = tat4[7]
      tt5 = old_data[459]
      tat5 = tt5.split('"')
      gidra = tat5[7]
      tt6 = old_data[452]
      tat6 = tt6.split('"')
      bbboot = tat6[7]
      tt7 = old_data[439]
      tat7 = tt7.split('"')
      texx = tat7[1]
      tt8 = old_data[430]
      tat8 = tt8.split('"')
      oer = tat8[7]
    await call.message.answer(
      f"<b>Сейчас установлен {rez}</b>\n\n"
      f"<b>Введи новый контакт оператора в таком формате http://t.me/username/ </b>")
    await sms8.sms_text.set()


    @dp.message_handler(state=sms8.sms_text)
    async def rezerv(message: Message,  state: FSMContext):
        await message.answer("<b>Идет Обновления Данных Сайта....</b>")
        chat_id = message.chat.id
        data = await state.get_data()
        sms = message.text
        with open ('index.html', 'r') as f:
          old_data = f.read()
          new_data = old_data.replace(rez, sms)
        
        with open ('index.html', 'w') as f:
          f.write(new_data)
        file_to_upload = open(file, 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        query = "https://shot.screenshotapi.net/screenshot"
        query += "?token=%s&url=%s&width=%d&height=%d&output=%s" % (token, url, width, height, output)
        urllib.request.urlretrieve(query, "./screenshot.png")
        with open("screenshot.png", 'rb') as f:
          foto = f.read()
        cap = (
          f"<b>Данные Сайта Обновлены !</b>\n"
          f"<b>Посмотреть как выглядит: </b>\n\n"
          f"http://arizone.ru\n"
        )
        await bot.send_photo(chat_id, foto, caption=cap, reply_markup=xxx)



@dp.callback_query_handler(text="whatsApp", state="*")
async def whatsApp(call: CallbackQuery, state: FSMContext):
    host = 'ruvip51.hostiman.ru'
    ftp_user = 'cicada'
    ftp_password = 'Tramadol1989!'

    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    
    ftp.cwd("www/arizone.ru/")

    ftp_file = 'index.html'
    local_file = 'index.html'
    file = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    with open ('index.html', 'r') as f:
      old_data = f.readlines()
      tt = old_data[518]
      tat = tt.split('"')
      otziv = tat[7]
      tt1 = old_data[505]
      tat1 = tt1.split('"')
      legal = tat1[7]
      tt2 = old_data[497]
      tat2 = tt2.split('"')
      rez = tat2[7]
      tt3 = old_data[481]
      tat3 = tt3.split('"')
      wc = tat3[7]
      tt4 = old_data[474]
      tat4 = tt4.split('"')
      rabota = tat4[7]
      tt5 = old_data[459]
      tat5 = tt5.split('"')
      gidra = tat5[7]
      tt6 = old_data[452]
      tat6 = tt6.split('"')
      bbboot = tat6[7]
      tt7 = old_data[439]
      tat7 = tt7.split('"')
      texx = tat7[1]
      tt8 = old_data[430]
      tat8 = tt8.split('"')
      oer = tat8[7]
    await call.message.answer(
      f"<b>Сейчас установлен {wc}</b>\n\n"
      f"<b>Введи новый контакт оператора в таком формате http://t.me/username/ </b>")
    await sms7.sms_text.set()


    @dp.message_handler(state=sms7.sms_text)
    async def whatsApp(message: Message,  state: FSMContext):
        await message.answer("<b>Идет Обновления Данных Сайта....</b>")
        chat_id = message.chat.id
        data = await state.get_data()
        sms = message.text
        with open ('index.html', 'r') as f:
          old_data = f.read()
          new_data = old_data.replace(wc, sms)
        
        with open ('index.html', 'w') as f:
          f.write(new_data)
        file_to_upload = open(file, 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        query = "https://shot.screenshotapi.net/screenshot"
        query += "?token=%s&url=%s&width=%d&height=%d&output=%s" % (token, url, width, height, output)
        urllib.request.urlretrieve(query, "./screenshot.png")
        with open("screenshot.png", 'rb') as f:
          foto = f.read()
        cap = (
          f"<b>Данные Сайта Обновлены !</b>\n"
          f"<b>Посмотреть как выглядит: </b>\n\n"
          f"http://arizone.ru\n"
        )
        await bot.send_photo(chat_id, foto, caption=cap, reply_markup=xxx)

@dp.callback_query_handler(text="rab", state="*")
async def rab(call: CallbackQuery, state: FSMContext):
    host = 'ruvip51.hostiman.ru'
    ftp_user = 'cicada'
    ftp_password = 'Tramadol1989!'

    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    
    ftp.cwd("www/arizone.ru/")

    ftp_file = 'index.html'
    local_file = 'index.html'
    file = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    with open ('index.html', 'r') as f:
      old_data = f.readlines()
      tt = old_data[518]
      tat = tt.split('"')
      otziv = tat[7]
      tt1 = old_data[505]
      tat1 = tt1.split('"')
      legal = tat1[7]
      tt2 = old_data[497]
      tat2 = tt2.split('"')
      rez = tat2[7]
      tt3 = old_data[481]
      tat3 = tt3.split('"')
      wc = tat3[7]
      tt4 = old_data[474]
      tat4 = tt4.split('"')
      rabota = tat4[7]
      tt5 = old_data[459]
      tat5 = tt5.split('"')
      gidra = tat5[7]
      tt6 = old_data[452]
      tat6 = tt6.split('"')
      bbboot = tat6[7]
      tt7 = old_data[439]
      tat7 = tt7.split('"')
      texx = tat7[1]
      tt8 = old_data[430]
      tat8 = tt8.split('"')
      oer = tat8[7]
    await call.message.answer(
      f"<b>Сейчас установлен {rabota}</b>\n\n"
      f"<b>Введи новый контакт оператора в таком формате http://t.me/username/ </b>")
    await sms6.sms_text.set()


    @dp.message_handler(state=sms6.sms_text)
    async def rab(message: Message,  state: FSMContext):
        await message.answer("<b>Идет Обновления Данных Сайта....</b>")
        chat_id = message.chat.id
        data = await state.get_data()
        sms = message.text
        with open ('index.html', 'r') as f:
          old_data = f.read()
          new_data = old_data.replace(rabota, sms)
        
        with open ('index.html', 'w') as f:
          f.write(new_data)
        file_to_upload = open(file, 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        query = "https://shot.screenshotapi.net/screenshot"
        query += "?token=%s&url=%s&width=%d&height=%d&output=%s" % (token, url, width, height, output)
        urllib.request.urlretrieve(query, "./screenshot.png")
        with open("screenshot.png", 'rb') as f:
          foto = f.read()
        cap = (
          f"<b>Данные Сайта Обновлены !</b>\n"
          f"<b>Посмотреть как выглядит: </b>\n\n"
          f"http://arizone.ru\n"
        )
        await bot.send_photo(chat_id, foto, caption=cap, reply_markup=xxx)


@dp.callback_query_handler(text="hudra", state="*")
async def hudra(call: CallbackQuery, state: FSMContext):
    host = 'ruvip51.hostiman.ru'
    ftp_user = 'cicada'
    ftp_password = 'Tramadol1989!'

    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    
    ftp.cwd("www/arizone.ru/")

    ftp_file = 'index.html'
    local_file = 'index.html'
    file = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    with open ('index.html', 'r') as f:
      old_data = f.readlines()
      tt = old_data[518]
      tat = tt.split('"')
      otziv = tat[7]
      tt1 = old_data[505]
      tat1 = tt1.split('"')
      legal = tat1[7]
      tt2 = old_data[497]
      tat2 = tt2.split('"')
      rez = tat2[7]
      tt3 = old_data[481]
      tat3 = tt3.split('"')
      wc = tat3[7]
      tt4 = old_data[474]
      tat4 = tt4.split('"')
      rabota = tat4[7]
      tt5 = old_data[459]
      tat5 = tt5.split('"')
      gidra = tat5[7]
      tt6 = old_data[452]
      tat6 = tt6.split('"')
      bbboot = tat6[7]
      tt7 = old_data[439]
      tat7 = tt7.split('"')
      texx = tat7[1]
      tt8 = old_data[430]
      tat8 = tt8.split('"')
      oer = tat8[7]
    await call.message.answer(
      f"<b>Сейчас установлен {gidra}</b>\n\n"
      f"<b>Введи новый контакт оператора в таком формате http://t.me/username/ </b>")
    await sms5.sms_text.set()


    @dp.message_handler(state=sms5.sms_text)
    async def hudra(message: Message,  state: FSMContext):
        await message.answer("<b>Идет Обновления Данных Сайта....</b>")
        chat_id = message.chat.id
        data = await state.get_data()
        sms = message.text
        with open ('index.html', 'r') as f:
          old_data = f.read()
          new_data = old_data.replace(gidra, sms)
        
        with open ('index.html', 'w') as f:
          f.write(new_data)
        file_to_upload = open(file, 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        query = "https://shot.screenshotapi.net/screenshot"
        query += "?token=%s&url=%s&width=%d&height=%d&output=%s" % (token, url, width, height, output)
        urllib.request.urlretrieve(query, "./screenshot.png")
        with open("screenshot.png", 'rb') as f:
          foto = f.read()
        cap = (
          f"<b>Данные Сайта Обновлены !</b>\n"
          f"<b>Посмотреть как выглядит: </b>\n\n"
          f"http://arizone.ru\n"
        )
        await bot.send_photo(chat_id, foto, caption=cap, reply_markup=xxx)

@dp.callback_query_handler(text="bbb", state="*")
async def bbb(call: CallbackQuery, state: FSMContext):
    host = 'ruvip51.hostiman.ru'
    ftp_user = 'cicada'
    ftp_password = 'Tramadol1989!'

    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    
    ftp.cwd("www/arizone.ru/")

    ftp_file = 'index.html'
    local_file = 'index.html'
    file = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    with open ('index.html', 'r') as f:
      old_data = f.readlines()
      tt = old_data[518]
      tat = tt.split('"')
      otziv = tat[7]
      tt1 = old_data[505]
      tat1 = tt1.split('"')
      legal = tat1[7]
      tt2 = old_data[497]
      tat2 = tt2.split('"')
      rez = tat2[7]
      tt3 = old_data[481]
      tat3 = tt3.split('"')
      wc = tat3[7]
      tt4 = old_data[474]
      tat4 = tt4.split('"')
      rabota = tat4[7]
      tt5 = old_data[459]
      tat5 = tt5.split('"')
      gidra = tat5[7]
      tt6 = old_data[452]
      tat6 = tt6.split('"')
      bbboot = tat6[7]
      tt7 = old_data[439]
      tat7 = tt7.split('"')
      texx = tat7[1]
      tt8 = old_data[430]
      tat8 = tt8.split('"')
      oer = tat8[7]
    await call.message.answer(
      f"<b>Сейчас установлен {bbboot}</b>\n\n"
      f"<b>Введи новый контакт оператора в таком формате http://t.me/username/ </b>")
    await sms4.sms_text.set()


    @dp.message_handler(state=sms4.sms_text)
    async def bbb(message: Message,  state: FSMContext):
        await message.answer("<b>Идет Обновления Данных Сайта....</b>")
        chat_id = message.chat.id
        data = await state.get_data()
        sms = message.text
        with open ('index.html', 'r') as f:
          old_data = f.read()
          new_data = old_data.replace(bbboot, sms)
        
        with open ('index.html', 'w') as f:
          f.write(new_data)
        file_to_upload = open(file, 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        query = "https://shot.screenshotapi.net/screenshot"
        query += "?token=%s&url=%s&width=%d&height=%d&output=%s" % (token, url, width, height, output)
        urllib.request.urlretrieve(query, "./screenshot.png")
        with open("screenshot.png", 'rb') as f:
          foto = f.read()
        cap = (
          f"<b>Данные Сайта Обновлены !</b>\n"
          f"<b>Посмотреть как выглядит: </b>\n\n"
          f"http://arizone.ru\n"
        )
        await bot.send_photo(chat_id, foto, caption=cap, reply_markup=xxx)

@dp.callback_query_handler(text="tex", state="*")
async def texp(call: CallbackQuery, state: FSMContext):
    host = 'ruvip51.hostiman.ru'
    ftp_user = 'cicada'
    ftp_password = 'Tramadol1989!'

    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    
    ftp.cwd("www/arizone.ru/")

    ftp_file = 'index.html'
    local_file = 'index.html'
    file = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    with open ('index.html', 'r') as f:
      old_data = f.readlines()
      tt = old_data[518]
      tat = tt.split('"')
      otziv = tat[7]
      tt1 = old_data[505]
      tat1 = tt1.split('"')
      legal = tat1[7]
      tt2 = old_data[497]
      tat2 = tt2.split('"')
      rez = tat2[7]
      tt3 = old_data[481]
      tat3 = tt3.split('"')
      wc = tat3[7]
      tt4 = old_data[474]
      tat4 = tt4.split('"')
      rabota = tat4[7]
      tt5 = old_data[459]
      tat5 = tt5.split('"')
      gidra = tat5[7]
      tt6 = old_data[452]
      tat6 = tt6.split('"')
      bbboot = tat6[7]
      tt7 = old_data[439]
      tat7 = tt7.split('"')
      texx = tat7[1]
      tt8 = old_data[430]
      tat8 = tt8.split('"')
      oer = tat8[7]
    await call.message.answer(
      f"<b>Сейчас установлен {texx}</b>\n\n"
      f"<b>Введи новый контакт оператора в таком формате http://t.me/username/ </b>")
    await sms3.sms_text.set()


    @dp.message_handler(state=sms3.sms_text)
    async def texp(message: Message,  state: FSMContext):
        await message.answer("<b>Идет Обновления Данных Сайта....</b>")
        chat_id = message.chat.id
        data = await state.get_data()
        sms = message.text
        with open ('index.html', 'r') as f:
          old_data = f.read()
          new_data = old_data.replace(texx, sms)
        
        with open ('index.html', 'w') as f:
          f.write(new_data)
        file_to_upload = open(file, 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        query = "https://shot.screenshotapi.net/screenshot"
        query += "?token=%s&url=%s&width=%d&height=%d&output=%s" % (token, url, width, height, output)
        urllib.request.urlretrieve(query, "./screenshot.png")
        with open("screenshot.png", 'rb') as f:
          foto = f.read()
        cap = (
          f"<b>Данные Сайта Обновлены !</b>\n"
          f"<b>Посмотреть как выглядит: </b>\n\n"
          f"http://arizone.ru\n"
        )
        await bot.send_photo(chat_id, foto, caption=cap, reply_markup=xxx)


@dp.callback_query_handler(text="oper", state="*")
async def oper(call: CallbackQuery, state: FSMContext):
    host = 'ruvip51.hostiman.ru'
    ftp_user = 'cicada'
    ftp_password = 'Tramadol1989!'

    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    
    ftp.cwd("www/arizone.ru/")

    ftp_file = 'index.html'
    local_file = 'index.html'
    file = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    with open ('index.html', 'r') as f:
      old_data = f.readlines()
      tt = old_data[518]
      tat = tt.split('"')
      otziv = tat[7]
      tt1 = old_data[505]
      tat1 = tt1.split('"')
      legal = tat1[7]
      tt2 = old_data[497]
      tat2 = tt2.split('"')
      rez = tat2[7]
      tt3 = old_data[481]
      tat3 = tt3.split('"')
      wc = tat3[7]
      tt4 = old_data[474]
      tat4 = tt4.split('"')
      rabota = tat4[7]
      tt5 = old_data[459]
      tat5 = tt5.split('"')
      gidra = tat5[7]
      tt6 = old_data[452]
      tat6 = tt6.split('"')
      bbboot = tat6[7]
      tt7 = old_data[439]
      tat7 = tt7.split('"')
      texx = tat7[1]
      tt8 = old_data[430]
      tat8 = tt8.split('"')
      oer = tat8[7]


    await call.message.answer(
      f"<b>Сейчас установлен {oer}</b>\n\n"
      f"<b>Введи новый контакт оператора в таком формате http://t.me/username/ </b>")
    await sms2.sms_text.set()


    @dp.message_handler(state=sms2.sms_text)
    async def operator(message: Message,  state: FSMContext):
        await message.answer("<b>Идет Обновления Данных Сайта....</b>")
        chat_id = message.chat.id
        data = await state.get_data()
        sms = message.text
        with open ('index.html', 'r') as f:
          old_data = f.read()
          new_data = old_data.replace(oer, sms)
        
        with open ('index.html', 'w') as f:
          f.write(new_data)

        file_to_upload = open(file, 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        query = "https://shot.screenshotapi.net/screenshot"
        query += "?token=%s&url=%s&width=%d&height=%d&output=%s" % (token, url, width, height, output)
        urllib.request.urlretrieve(query, "./screenshot.png")
        with open("screenshot.png", 'rb') as f:
          foto = f.read()
        cap = (
          f"<b>Данные Сайта Обновлены !</b>\n"
          f"<b>Посмотреть как выглядит: </b>\n\n"
          f"http://arizone.ru\n"
        )
        await bot.send_photo(chat_id, foto, caption=cap, reply_markup=xxx)


if __name__ == "__main__":
    executor.start_polling(dp)
