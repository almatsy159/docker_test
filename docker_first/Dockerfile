FROM python:3.10.12
WORKDIR /app
COPY . /app
CMD ["pip","install","--update","pip","&&","--upgrade pip"]
RUN pip install -r requirements.txt
EXPOSE 1024
ENV NOM ALMA

CMD ["python3","app.py"]