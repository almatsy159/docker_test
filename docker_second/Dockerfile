FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 2044
ENV DEFAULT = "index.html"
CMD ["python3","app.py"]