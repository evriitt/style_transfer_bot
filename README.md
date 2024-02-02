# style_transfer_bot


Telegram бот для переноса стиля с загруженных изображений.

В проекте используются предварительно обученные модели из проекта [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/).

Доступны четыре художественных стиля: "Клод Моне", "Поль Сезанн", "Укиё-э", "Ван Гог".
## Примеры работы:

### Клод Моне

![photo_2024-02-01_15-21-16](https://github.com/evriitt/style_transfer_bot/assets/130037283/9e0d2f01-05af-4741-98b5-bec8e26eb952)  ![photo_2024-02-01_15-21-22](https://github.com/evriitt/style_transfer_bot/assets/130037283/d02a4322-6018-4e01-91f3-df45043af42b)

![photo_2024-02-01_17-15-17](https://github.com/evriitt/style_transfer_bot/assets/130037283/f645d9fb-ebef-4967-8530-435c4413824b)  ![photo_2024-02-01_17-15-25](https://github.com/evriitt/style_transfer_bot/assets/130037283/27b1b32a-6d59-4b3e-bc1b-d8ddeb05987a)


### Поль Сезанн
![photo_2024-02-01_14-59-43](https://github.com/evriitt/style_transfer_bot/assets/130037283/7e9d6a12-4c69-4253-99a3-aa22668f686c)  ![photo_2024-02-01_14-59-55](https://github.com/evriitt/style_transfer_bot/assets/130037283/e9cee558-bd25-4c38-8142-61e9b0a65c0c)

![photo_2024-02-01_15-01-26](https://github.com/evriitt/style_transfer_bot/assets/130037283/8f9b59f8-0678-4d0d-9e7b-3119032b25fc)  ![photo_2024-02-01_15-01-33](https://github.com/evriitt/style_transfer_bot/assets/130037283/333a27da-0e90-4fcf-9c72-be88a2f11187)

![photo_2024-02-01_15-06-00](https://github.com/evriitt/style_transfer_bot/assets/130037283/70537262-f273-4e64-b06e-f47f7e6dba3e)  ![photo_2024-02-01_15-06-05](https://github.com/evriitt/style_transfer_bot/assets/130037283/9e3151af-ec10-410c-b299-1b344fb45f42)



### Укиё-э
![photo_2024-02-01_15-48-09](https://github.com/evriitt/style_transfer_bot/assets/130037283/8c51064e-7d0c-41c4-a292-5027a5942805)  ![photo_2024-02-01_15-48-13](https://github.com/evriitt/style_transfer_bot/assets/130037283/bfd92c1d-66a1-48a0-aa11-6a3aa9fdd74d)

![photo_2024-02-01_15-36-21](https://github.com/evriitt/style_transfer_bot/assets/130037283/adcbbbd1-d0f9-4606-b1aa-77ff85f6876c)  ![photo_2024-02-01_15-36-34](https://github.com/evriitt/style_transfer_bot/assets/130037283/f28f12d3-a46b-44a0-8011-49dae0f39dcd)

![photo_2024-02-01_17-13-32](https://github.com/evriitt/style_transfer_bot/assets/130037283/309a5f60-c154-4bc2-9b1b-5d198f563d4a)  ![photo_2024-02-01_17-13-48](https://github.com/evriitt/style_transfer_bot/assets/130037283/4979793d-0d6e-4b30-911b-0d7299f33671)




### Ван Гог
![photo_2024-02-01_15-28-35](https://github.com/evriitt/style_transfer_bot/assets/130037283/e4fc94f8-30ed-4ccc-93c6-9a5617bb6f7b)  ![photo_2024-02-01_15-28-48](https://github.com/evriitt/style_transfer_bot/assets/130037283/00337d79-8d78-4a71-981e-25aa5c9fa76c)

![photo_2024-02-01_15-37-51](https://github.com/evriitt/style_transfer_bot/assets/130037283/4af60cb6-0302-4200-81f0-1b7d2aca69f8)  ![photo_2024-02-01_15-38-07](https://github.com/evriitt/style_transfer_bot/assets/130037283/5a5d03e8-9563-4878-acd1-a087edb0efad)



## Как запустить

### Запуск в Google Colab:
1. Получите свой TG_BOT_TOKEN от [BotFather](https://t.me/BotFather).
2. Откройте [блокнот](https://colab.research.google.com/drive/1vpkU9ZFblbPtjB660AQ1DNuoZkIldwu0?usp=sharing) и заполните TG_BOT_TOKEN.
3. Запустите бота: [artstyle_transfer_bot](https://t.me/artstyle_transfer_bot).

### Запуск локально:
1. Создайте и активируйте виртуальное окружение
2. Склонируйте репозиторий: `git clone https://github.com/evriitt/style_transfer_bot`.
3. Вставьте свой TG_BOT_TOKEN в файл .env, полученный от [BotFather](https://t.me/BotFather).
3. Запустите контейнер: `docker compose up -d` **или** (для запуска вне контейнера)
   
                  `pip install -r requirements.txt` и далее `python app.py`
   
5. Подождите 4-6 минут, пока завершится установка, проверьте логи Docker: `docker logs tg_bot`.
6. Запустите бота: [artstyle_transfer_bot](https://t.me/artstyle_transfer_bot).
