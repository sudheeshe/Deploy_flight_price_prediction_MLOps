FROM python:3.7
COPY . /app
WORKDIR /app
RUN /app/.heroku/python/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]