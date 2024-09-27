FROM python:3.12

WORKDIR /starlio-web

COPY ./requirements.txt /starlio-web/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /starlio-web/requirements.txt

COPY ./ /starlio-web/

CMD ["fastapi", "run", "main.py", "--port", "8000"]