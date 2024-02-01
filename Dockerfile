FROM python:3.10

ADD requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt

ADD app.py /
ADD .env / 
ENV PYTHONUNBUFFERED=1

CMD [ "python", "./app.py" ]