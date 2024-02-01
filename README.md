# style_transfer_bot


Telegram bot с функциями переноса художественного стиля с загруженного изображения. 

Используются предобученные модели из прокта https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/

Всего доступно 4 стиля: "Клод Моне", "Поль Сезанн", "Укиё-э", "Ван Гог".
Примеры генераций:
# тут фото пар изображение-генерация для каждого художника


Запуск в colab:

1. Получить TG_BOT_TOKEN от https://t.me/BotFather
2. Открыть блокнот и заполнить TG_BOT_TOKEN: https://colab.research.google.com/drive/1vpkU9ZFblbPtjB660AQ1DNuoZkIldwu0?usp=sharing
3. Запустить бота https://t.me/artstyle_transfer_bot

Запуск в контейнере:
1. Клонирвоать репозиторий git clone https://github.com/evriitt/style_transfer_bot
2. В файл .env вставить TG_BOT_TOKEN от https://t.me/BotFather
3. Поднять контейнер docker compose up -d
4. Подождать 4-6 минут пока все установится, проверить лог docker logs tg_bot,
5. Запустить бота https://t.me/artstyle_transfer_bot

Запуск локально:
1. Создать и активировать среду:
   python3 -m venv venv
   source venv/bin/activate
2. Установить библиотеки
pip install -r requirements.txt
3. Запустить программу 
4. python3 app.py и подождать несколько минут
5. Запустить бота https://t.me/artstyle_transfer_bot
