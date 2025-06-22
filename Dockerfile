FROM python:3.13.5-alpine3.22

COPY requirements.txt /opt/app/requirements.txt
RUN pip install --no-cache-dir -r /opt/app/requirements.txt

COPY . /opt/app

WORKDIR /opt/app/

EXPOSE 8000

ENTRYPOINT [ "python" ]

CMD ["manage.py", "runserver"]