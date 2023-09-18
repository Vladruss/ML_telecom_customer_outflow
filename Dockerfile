FROM python:3.10

ENV POETRY_VERSION=1.6.1

WORKDIR /app

RUN pip install pip --upgrade
RUN pip install poetry==$POETRY_VERSION

# COPY requirements.txt .
COPY poetry.lock pyproject.toml .

# RUN pip install -r requirements.txt
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi


COPY api/ .

CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000 
