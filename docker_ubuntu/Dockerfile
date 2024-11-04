FROM ubuntu:24.04
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 80
ENV DEFAULT = "index.html"
RUN ["head","~/.bashrc"]
