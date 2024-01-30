FROM python:3.10

ADD requirements.txt /

RUN pip install --no-cache-dir -r requirements.txt

ADD art_style_bot_ipynb.py /

ENV PYTHONUNBUFFERED=1

CMD [ "python", "./art_style_bot_ipynb.py" ]