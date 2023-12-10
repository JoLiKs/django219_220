import asyncio
import logging
import time
from asyncio import Lock
from aiogram import Bot, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import types
from aiogram.types import InputFile
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from PIL import Image, ImageFont, ImageDraw

logging.basicConfig(level=logging.INFO)

bot = Bot(token="")
dp = Dispatcher(bot=bot, storage=MemoryStorage())

Base = declarative_base()
lock = Lock()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    surname = Column(String, nullable=True)
    age = Column(Integer, nullable=True)

    def __init__(self, n, s, a):
        self.name = n
        self.surname = s
        self.age = a

engine = create_engine("sqlite:///base.db")

session = scoped_session(sessionmaker(bind=engine))


@dp.message_handler(text='фото')
async def cmd_start(message: types.Message):
    photo = InputFile("r1.png")

    await message.answer_photo(photo=photo, caption='фото из интернета')
class RegisterMessages(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()


class DB:
    answer_data = {}

@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message: types.Message):
    await message.photo[-1].download('r1.png')
    time.sleep(1)
    sample = Image.open('r1.png')
    width, height = sample.size
    print(width, height, sample.size)
    resized_image1 = sample.resize((width // 2, height // 2))  # первый варинт - так не работает
   # resized_image2 = img.resize((200, 300))  # второй вариант , просто к примеру - работает
    print(resized_image1.size)
    resized_image1.save('r2.png')
   # resized_image2.save('r3.png')

    await message.answer_photo(InputFile('r2.png'))

@dp.message_handler(text='/start', state=None)
async def start(message: types.Message):
   await message.answer("Hi!")

@dp.message_handler(content_types='text', state=RegisterMessages.step1)
async def reg_step3(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        return await message.answer('Возраст не может содержать буквы!')
    async with lock:
        DB.answer_data['age'] = message.text
    await bot.send_message(message.from_user.id, text='Замечательный возраст!')
    await state.finish()
    session.add(Users(DB.answer_data['name'], DB.answer_data['surname'], DB.answer_data['age']))
    session.commit()


async def main():
    await dp.start_polling(bot)



