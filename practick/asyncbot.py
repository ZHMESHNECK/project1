import asyncio
from random import choice
from aiogram import Bot, Dispatcher, executor, types
from Token import token

"""async def func(x):
    for i in range(x):
        print(i)
        await asyncio.sleep(1)
    return x / 2

async def main():
    x = asyncio.gather(func(6),func(2),func(10))

    await x

loop = asyncio.get_event_loop()
loop.run_until_complete(main())"""

bot = Bot(token)
dp = Dispatcher(bot)

# games = {'chat_id':{'users':[username,2],message_id:123}}
games = {}

"""@dp.message_handler(commands=['start']) # отправляет смс от 1 до 10 раз в сек
async def func(message):
    for i in range(10):
        await bot.send_message(message.chat.id, str(i))
        await asyncio.sleep(1)"""


@dp.message_handler(commands=['play'])
async def func(message):
    if message.chat.id in games:  # проверяем есть ли такая игра
        await bot.send_message(message.chat.id, 'Игра уже начата')
    else:  # если нет, то создаём игру
        m = types.InlineKeyboardMarkup()
        m.add(types.InlineKeyboardButton('Играть', callback_data='play'))
        msg = await bot.send_message(message.chat.id, 'Ждём игроков', reply_markup=m) # сохраняем смс после отправки
        games[message.chat.id] = {'users': [], 'msg': msg}
        await asyncio.sleep(60) 
        if message.chat.id in games:
            games.pop(message.chat.id) # удаляем игру из словаря
            await bot.send_message(message.chat.id, 'Игроки не собраны в нужном количестве') # message смс которое пришло
            await bot.delete_message(msg.chat.id, msg.message_id) # msg смс которое отправил


@dp.callback_query_handler(lambda call: call.data == 'play')
async def play(call: types.CallbackQuery):
    if call.message.chat.id in games:
        msg = games[call.message.chat.id]['msg']
        if call.message.message_id == msg.message_id:
            users_list = games[call.message.chat.id]['users']
            if call.from_user.id not in users_list: # проверка юзара в словаре
                users_list.append(call.from_user.full_name)
                await bot.edit_message_text(f'Игроков в лобби: {len(users_list)}', msg.chat.id, msg.message_id, reply_markup=msg.reply_markup) # достаём клаву из смс

                if len(users_list) >= 1:
                    games.pop(msg.chat.id)
                    await bot.send_message(msg.chat.id, 'Старт игры')
                    await bot.delete_message(msg.chat.id, msg.message_id)
                    await asyncio.sleep(1)
                    await bot.send_message(msg.chat.id, '3')
                    await asyncio.sleep(1)
                    await bot.send_message(msg.chat.id, '2')
                    await asyncio.sleep(1)
                    await bot.send_message(msg.chat.id, '1')
                    await asyncio.sleep(1)
                    await bot.send_message(msg.chat.id, f'Победил {choice(users_list)}')


executor.start_polling(dp, skip_updates=True)
