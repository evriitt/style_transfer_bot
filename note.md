python3 -m venv venv
source venv/bin/activate
pip install -r ./pytorch-CycleGAN-and-pix2pix/requirements.txt
git clone https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
pip install telebot

conda env update -f ./pytorch-CycleGAN-and-pix2pix/environment.yml

bash ./pytorch-CycleGAN-and-pix2pix/scripts/download_cyclegan_model.sh  style_monet
bash ./pytorch-CycleGAN-and-pix2pix/scripts/download_cyclegan_model.sh  style_cezanne
bash ./pytorch-CycleGAN-and-pix2pix/scripts/download_cyclegan_model.sh  style_ukiyoe
bash ./pytorch-CycleGAN-and-pix2pix/scripts/download_cyclegan_model.sh  style_vangogh


numpy-1.23.5

python app.py

git config --global user.email "ok6234954@gmail.com"
git config --global user.name "evriitt"
ssh-keygen -t ed25519 -C "ok6234954@gmail.com"

git remote add amvera https://git.amvera.ru/evriitt/style_transfer_bot


style_transfer_bot
git add style_transfer_bot/
git commit -m "Initial commit for style_transfer_bot"

python3 ./pytorch-CycleGAN-and-pix2pix/test.py --dataroot ./user_image --name style_monet_pretrained --model test --no_dropout --gpu_ids -1 --preprocess scale_width --load_size 350

pip install -r requirements.txt

python3 -m pip install Pillow
pip install torchvision

python -m pip freeze > 1.txt


python3 art_style_bot_ipynb.py


mkdir bot
mv art_style_bot_ipynb.py bot

python3 -m pip freeze > requirements.txt

docker compose build

docker compose up -d

pip install --upgrade setuptools

sudo apt-get install python3.10-tk

sudo apt update

sudo apt-get install libsystemd

sudo apt-get install libdbus-1-dev

RUN apt-get update && apt-get install -y libpq-dev build-essential

sudo apt update && sudo apt upgrade -y