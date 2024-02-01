# style_transfer_bot


Telegram бот для переноса стиля с загруженных изображений.

В проекте используются предварительно обученные модели из проекта [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/).

Доступны четыре художественных стиля: "Клод Моне", "Поль Сезанн", "Укиё-э", "Ван Гог".
## Примеры работы:

### Клод Моне
![photo_2024-02-01_15-17-08](https://github.com/evriitt/style_transfer_bot/assets/130037283/31ceb130-604b-46d1-8891-9119d9cdae25)  ![photo_2024-02-01_15-17-13](https://github.com/evriitt/style_transfer_bot/assets/130037283/c229c645-7d6e-49ad-a21b-22ad3577c9f0)

![photo_2024-02-01_15-13-15](https://github.com/evriitt/style_transfer_bot/assets/130037283/679ea465-ac7e-4368-9bbd-ca6cd6c0ebd5)  ![photo_2024-02-01_15-14-08](https://github.com/evriitt/style_transfer_bot/assets/130037283/6b17963a-ceb9-49d2-92c6-1635adccaa90)

![photo_2024-02-01_15-21-16](https://github.com/evriitt/style_transfer_bot/assets/130037283/d492efe6-d5ca-4bfb-b726-4e1ca119116a)  ![photo_2024-02-01_15-21-22](https://github.com/evriitt/style_transfer_bot/assets/130037283/b526e5a5-6c60-4a07-87ac-8e88cd4aebb3)





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
