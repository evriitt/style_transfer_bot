# style_transfer_bot


Telegram бот для переноса стиля с загруженных изображений.

В проекте используются предварительно обученные модели из проекта [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/).

Доступны четыре художественных стиля: "Клод Моне", "Поль Сезанн", "Укиё-э", "Ван Гог".
## Примеры работы:

### Клод Моне
![Примеры](examples.jpg)
![photo_2024-02-01_15-13-15](https://github.com/evriitt/style_transfer_bot/assets/130037283/de52a0ef-8dd4-44e6-a3da-b39b2daacd47)  ![photo_2024-02-01_15-14-08](https://github.com/evriitt/style_transfer_bot/assets/130037283/f4a37aa9-f503-4c05-be47-d3a67c2a574e)


### Поль Сезанн
![Примеры](examples.jpg)

### Укиё-э
![Примеры](examples.jpg)

### Ван Гог
![Примеры](examples.jpg)

## Как запустить

### Запуск в Google Colab:
1. Получите свой TG_BOT_TOKEN от [BotFather](https://t.me/BotFather).
2. Откройте блокнот и заполните TG_BOT_TOKEN: [Colab Notebook](https://colab.research.google.com/drive/1vpkU9ZFblbPtjB660AQ1DNuoZkIldwu0?usp=sharing).
3. Запустите бота: [artstyle_transfer_bot](https://t.me/artstyle_transfer_bot).

### Запуск локально:
1. Создайте и активируйте виртуальное окружение
2. Склонируйте репозиторий: `git clone https://github.com/evriitt/style_transfer_bot`.
3. Вставьте свой TG_BOT_TOKEN в файл .env, полученный от [BotFather](https://t.me/BotFather).
3. Запустите контейнер: `docker compose up -d` **или** (для запуска вне контейнера) `pip install -r requirements.txt` и далее `python3 app.py`
5. Подождите 4-6 минут, пока настройка завершится, проверьте логи Docker: `docker logs tg_bot`.
6. Запустите бота: [artstyle_transfer_bot](https://t.me/artstyle_transfer_bot).
