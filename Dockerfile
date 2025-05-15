
FROM python:3.13

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./therapy_backend /code/therapy_backend

CMD ["fastapi", "run", "therapy_backend/main.py", "--port", "80"]