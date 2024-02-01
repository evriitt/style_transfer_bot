# style_transfer_bot


Telegram бот для переноса стиля с загруженных изображений.

В проекте используются предварительно обученные модели из проекта [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/).

Доступны четыре художественных стиля: "Клод Моне", "Поль Сезанн", "Укиё-э", "Ван Гог".
## Примеры работы:

### Клод Моне

![photo_2024-02-01_15-13-15](https://github.com/evriitt/style_transfer_bot/assets/130037283/499c83ca-6d19-4ebc-8fec-a5479232de1a)  ![photo_2024-02-01_15-14-08](https://github.com/evriitt/style_transfer_bot/assets/130037283/6fe65304-f193-485c-9a3a-9ffe8b21a417)


![photo_2024-02-01_15-17-08](https://github.com/evriitt/style_transfer_bot/assets/130037283/31ceb130-604b-46d1-8891-9119d9cdae25)  ![photo_2024-02-01_15-17-13](https://github.com/evriitt/style_transfer_bot/assets/130037283/c229c645-7d6e-49ad-a21b-22ad3577c9f0)

![photo_2024-02-01_15-13-15](https://github.com/evriitt/style_transfer_bot/assets/130037283/679ea465-ac7e-4368-9bbd-ca6cd6c0ebd5)  ![photo_2024-02-01_15-14-08](https://github.com/evriitt/style_transfer_bot/assets/130037283/6b17963a-ceb9-49d2-92c6-1635adccaa90)

![photo_2024-02-01_15-21-16](https://github.com/evriitt/style_transfer_bot/assets/130037283/d492efe6-d5ca-4bfb-b726-4e1ca119116a)  ![photo_2024-02-01_15-21-22](https://github.com/evriitt/style_transfer_bot/assets/130037283/b526e5a5-6c60-4a07-87ac-8e88cd4aebb3)

### Поль Сезанн
![photo_2024-02-01_15-06-00](https://github.com/evriitt/style_transfer_bot/assets/130037283/62016b3c-9f16-41bb-9b06-0813717b02a4)  ![photo_2024-02-01_15-06-05](https://github.com/evriitt/style_transfer_bot/assets/130037283/369d96c6-adfe-4160-b333-58e7d394de6b)

![photo_2024-02-01_14-59-43](https://github.com/evriitt/style_transfer_bot/assets/130037283/cbaf5439-377e-496a-99ec-4a31d1406f8a)  ![photo_2024-02-01_14-59-55](https://github.com/evriitt/style_transfer_bot/assets/130037283/9ae46fab-49bd-4d4e-8242-0cfd92b01b90)

![photo_2024-02-01_15-01-26](https://github.com/evriitt/style_transfer_bot/assets/130037283/91847009-3c90-456d-b609-edf235cad73b)  ![photo_2024-02-01_15-01-33](https://github.com/evriitt/style_transfer_bot/assets/130037283/e92dc0b3-009b-431b-9d6e-bb7b1f09c420)


### Укиё-э
![photo_2024-02-01_15-36-21](https://github.com/evriitt/style_transfer_bot/assets/130037283/a3851a2a-d4b4-4cdf-b898-b6e8ba11d3b7)  ![photo_2024-02-01_15-36-34](https://github.com/evriitt/style_transfer_bot/assets/130037283/cabc19f1-8299-4c72-87bd-0dab5af10189)

![photo_2024-02-01_15-48-09](https://github.com/evriitt/style_transfer_bot/assets/130037283/eae79bd8-a474-4e7b-807a-b14fd2b89254)  ![photo_2024-02-01_15-48-13](https://github.com/evriitt/style_transfer_bot/assets/130037283/eb2793f3-ad36-4d44-8fc4-2537a0cb4e30)

![photo_2024-02-01_15-42-32](https://github.com/evriitt/style_transfer_bot/assets/130037283/0fa9f8a3-439b-40e2-8746-da7b8141e70f)  ![photo_2024-02-01_15-42-36](https://github.com/evriitt/style_transfer_bot/assets/130037283/5dd44d53-e926-4231-9c72-321a956a79a3)




### Ван Гог
![photo_2024-02-01_15-31-25](https://github.com/evriitt/style_transfer_bot/assets/130037283/497f305c-19f3-4b8c-8ab8-65b3b0bbf0f0)  ![photo_2024-02-01_15-31-30](https://github.com/evriitt/style_transfer_bot/assets/130037283/d0d96c90-ff53-4033-bb95-56db9514f339)

![photo_2024-02-01_15-28-35](https://github.com/evriitt/style_transfer_bot/assets/130037283/9eeb8d35-c0b4-4745-9f4a-e276341af1cb)  ![photo_2024-02-01_15-28-48](https://github.com/evriitt/style_transfer_bot/assets/130037283/532a8ad0-8a35-4074-9e83-d8cca61031c5)

![photo_2024-02-01_15-37-51](https://github.com/evriitt/style_transfer_bot/assets/130037283/b16731d2-54f5-4a16-ba53-82e11b734574)  ![photo_2024-02-01_15-38-07](https://github.com/evriitt/style_transfer_bot/assets/130037283/1b95dcf4-726f-4183-8a96-4ab1ca6c0800)




## Как запустить

### Запуск в Google Colab:
1. Получите свой TG_BOT_TOKEN от [BotFather](https://t.me/BotFather).
2. Откройте [блокнот](https://colab.research.google.com/drive/1vpkU9ZFblbPtjB660AQ1DNuoZkIldwu0?usp=sharing) и заполните TG_BOT_TOKEN.
3. Запустите бота: [artstyle_transfer_bot](https://t.me/artstyle_transfer_bot).

### Запуск локально:
1. Создайте и активируйте виртуальное окружение
2. Склонируйте репозиторий: `git clone https://github.com/evriitt/style_transfer_bot`.
3. Вставьте свой TG_BOT_TOKEN в файл .env, полученный от [BotFather](https://t.me/BotFather).
3. Запустите контейнер: `docker compose up -d` **или** (для запуска вне контейнера) `pip install -r requirements.txt` и далее `python3 app.py`
5. Подождите 4-6 минут, пока завершится установка, проверьте логи Docker: `docker logs tg_bot`.
6. Запустите бота: [artstyle_transfer_bot](https://t.me/artstyle_transfer_bot).
