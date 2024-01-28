
import os
import urllib
import telebot
import urllib.request
import logging



TOKEN = '6656785887:AAFhKHuVhSTMilM94kgHAYSOK6EsRAeyNho'

LOG_FILENAME = 'bot.log'

# Configure logging
logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a bot instance
bot = telebot.TeleBot(TOKEN)

# Log user starting interaction with the bot
logging.info('User started interaction with the bot')


@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я умею преобразовывать изображение в один из четырех художественных стилей.\n"
        "Загрузи любое изображение через скрепку (прикрепить файл)"
    )
    logging.info('Bot sent start message to user')


@bot.message_handler(content_types=['document'])
def scan_message(message):
    document_id = message.document.file_id
    file_info = bot.get_file(document_id)
    fi = file_info.file_path
    name = message.document.file_name
    image_path = f'./user_image/{name}'
    url = f'https://api.telegram.org/file/bot{TOKEN}/{fi}'
    urllib.request.urlretrieve(url, image_path)
    print("ПУТЬ",image_path)
    # Create a keyboard with style choices
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Клод Моне", "Поль Сезанн", "Укиё-э", "Ван Гог")
    bot.send_message(message.chat.id, "Теперь выбери стиль:", reply_markup=keyboard)
    logging.info('Bot sent style selection keyboard to user')

    # Wait for user's style choice
    bot.register_next_step_handler(message, process_style_selection, name)


def process_style_selection(message, name):
    style_choice = message.text
    logging.info(f'User selected style: {style_choice}')
    print("СТИЛЬ", style_choice)

    bot.send_message(message.chat.id, "Cкоро вернусь")
    
    # Determine the selected model based on user's style choice
    if style_choice == "Клод Моне":
        model_name = 'style_monet_pretrained'
    elif style_choice == "Поль Сезанн":
        model_name = 'style_cezanne_pretrained'
    elif style_choice == "Укиё-э":
        model_name = 'style_ukiyoe_pretrained'
    else:
        model_name = 'style_vangogh_pretrained'

    # Run the model to process the uploaded image with the selected style
    #command = rf"python ./pytorch-CycleGAN-and-pix2pix/test.py --dataroot ./user_image --name {model_name} --model test --no_dropout --gpu_ids -1 --preprocess scale_width --load_size 350"        
    #os.system(command)
    import subprocess
    import subprocess

    # Замените 'your_model_name' на фактическое имя модели


    # Формируем команду с аргументами
    command = [
        'python', './pytorch-CycleGAN-and-pix2pix/test.py',
        '--dataroot', './user_image',
        '--name', model_name,
        '--model', 'test',
        '--no_dropout',
        '--gpu_ids', '-1',
        '--preprocess', 'scale_width',
        '--load_size', '350'
    ]

    # Запускаем команду
    result = subprocess.run(command, capture_output=True, text=True)

    # Если необходимо проверить результат выполнения команды, можно вывести его
    print("Exit code:", result.returncode)
    print("Output:", result.stdout)
    print("Error:", result.stderr)
    #command = "python ./pytorch-CycleGAN-and-pix2pix/test.py --dataroot ./user_image --name {} --model test --no_dropout --gpu_ids -1 --preprocess scale_width --load_size 350".format(model_name)

    #subprocess.run(command, hell=True)
    #fake_img_path = rf'./results/{model_name}/test_latest/images/{name[:-4]}_fake.png'
    fake_img_path = rf'./results/{model_name}/test_latest/images/{name[:-4]}_fake.png'
    print("Путь фейка",fake_img_path)
    # Send the processed image to the user
    bot.send_message(message.chat.id, "Готово!")
    with open(fake_img_path, "rb") as photo_file:
        bot.send_photo(message.chat.id, photo_file)

    # Offer the user to select another style or upload a new image
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("Другой стиль", "Загрузить новое изображение")
    bot.send_message(message.chat.id, "Что дальше?", reply_markup=keyboard)
    logging.info('Bot sent next step options to user')

    # Wait for the user's response
    bot.register_next_step_handler(message, handle_next_step, name)


def handle_next_step(message, name):
    choice = message.text
    logging.info(f'User chose next step: {choice}')

    if choice == "Другой стиль":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add("Клод Моне", "Поль Сезанн", "Укиё-э", "Ван Гог")
        bot.send_message(message.chat.id, "Выбери другой стиль:", reply_markup=keyboard)
        bot.register_next_step_handler(message, process_style_selection, name)
        logging.info('Bot sent style selection keyboard to user')
    elif choice == "Загрузить новое изображение":
        bot.send_message(message.chat.id, "Загрузи новое изображение:")
        bot.register_next_step_handler(message, scan_message)
        logging.info('Bot prompted user to upload a new image')


def main():
    bot.polling()


if __name__ == "__main__":
    main()