
import subprocess
import sys
import urllib
import telebot
import urllib.request
import logging
import shutil
import os
import torch
from dotenv import load_dotenv

subprocess.run(["git", "clone", "https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix"])

models = ["style_monet", "style_cezanne", "style_ukiyoe", "style_vangogh"]      # Загрузка предобученных моделей
for model in models:
    subprocess.run(["bash", "./pytorch-CycleGAN-and-pix2pix/scripts/download_cyclegan_model.sh", model])

subprocess.run(["mkdir", "user_image"])         # Создание папки для хранения фото
subprocess.run("cd pytorch-CycleGAN-and-pix2pix/", shell=True)

load_dotenv()
TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")


logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',  # Настройки логгирования
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler(sys.stdout)  ])  
  

bot = telebot.TeleBot(TG_BOT_TOKEN)    

logging.info('Bot is ready!')

@bot.message_handler(commands=['start'])            # Реакция на /start
def command_start(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я умею преобразовывать изображение в один из четырех художественных стилей.\n"
        "Загрузи любое изображение."    )
    logging.info('Bot sent start message to user')

gpu_ids = '0' if torch.cuda.is_available() else '-1'
logging.info(f'gpu_ids is {gpu_ids}')

@bot.message_handler(content_types=['document', 'photo'])
def scan_message(message):
    logging.info('User uploaded a document or a photo')

    if message.content_type == 'photo':    # Проверяет, что загружено изображение
        file_id = message.photo[-1].file_id
    elif message.content_type == 'document':
        if message.document.mime_type.startswith('image'):
            file_id = message.document.file_id
        else:
            bot.send_message(message.chat.id,
                "Что-то пошло не так. Я умею работать только с изображениями, попробуйте загрузить еще раз.")
            logging.error('User uploaded a non-image document')# неизвестный тип контента
            return
    else:
        bot.send_message(message.chat.id,
            "Что-то пошло не так. Я умею работать только с изображениями, попробуйте загрузить еще раз.")
        logging.error('User uploaded a non-image content')
        return


    file_info = bot.get_file(file_id) # Получаем информацию о загруженном файле
    fi = file_info.file_path
    name = file_id + '.jpg'
    urllib.request.urlretrieve(f'https://api.telegram.org/file/bot{TG_BOT_TOKEN}/{fi}', f'./user_image/{name}')

    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)# Показываем клавиатуру
    keyboard.add("Клод Моне", "Поль Сезанн", "Укиё-э", "Ван Гог")
    bot.send_message(message.chat.id, "Теперь выбери стиль:", reply_markup=keyboard)
    bot.register_next_step_handler(message, process_style_selection, name)


def process_style_selection(message, name):
    style_choice = message.text
    logging.info(f'User selected style: {style_choice}')
    bot.send_message(message.chat.id, "Cкоро вернусь")
    
    if style_choice == "Клод Моне":
        model_name = 'style_monet_pretrained'# Отправляем фото в нужную модель
    elif style_choice == "Поль Сезанн":
        model_name = 'style_cezanne_pretrained'
    elif style_choice == "Укиё-э":
        model_name = 'style_ukiyoe_pretrained'
    else:
        model_name = 'style_vangogh_pretrained'

    
    command = [
    "python3",
    "./pytorch-CycleGAN-and-pix2pix/test.py",         
    "--dataroot",
    "./user_image",
    "--name",
    model_name,
    "--model",
    "test",
    "--no_dropout",
    "--gpu_ids",
    gpu_ids,
    "--preprocess",
    "scale_width",
    "--load_size",
    "500"]

    
    subprocess.run(command, capture_output=True)

    fake_img_path = f'./results/{model_name}/test_latest/images/{name[:-4]}_fake.png'

    bot.send_message(message.chat.id, "Готово!")                    # Отправка пользователю
    with open(fake_img_path, "rb") as photo_file:
        bot.send_photo(message.chat.id, photo_file)

    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Другой стиль", "Загрузить новое изображение", "Завершить")  # Добавляем кнопку "Завершить"
    bot.send_message(message.chat.id, "Что дальше?", reply_markup=keyboard)
    logging.info('Bot sent next step options to user')
    bot.register_next_step_handler(message, handle_next_step, name)


def handle_next_step(message, name):
    choice = message.text
    logging.info(f'User chose next step: {choice}')

    if choice == "Другой стиль":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add("Клод Моне", "Поль Сезанн", "Укиё-э", "Ван Гог")  
        bot.send_message(message.chat.id, "Выбери другой стиль:", reply_markup=keyboard)
        bot.register_next_step_handler(message, process_style_selection, name)

    elif choice == "Загрузить новое изображение":
        bot.send_message(message.chat.id, "Загрузи новое изображение:")
        bot.register_next_step_handler(message, scan_message)
        logging.info('Bot prompted user to upload a new image')

    elif choice == "Завершить":
        bot.send_message(message.chat.id, "До новых встреч! Когда захочешь продолжить нажми /start ")
        #shutil.rmtree("user_image")
        #os.makedirs("user_image")
        logging.info('User ended the conversation')


def main():
    bot.polling()


if __name__ == "__main__":
    main()

