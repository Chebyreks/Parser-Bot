FROM python:3.12.3

RUN apt-get update && apt-get install -y curl

RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.8.3 POETRY_HOME=/root/poetry python3 -
ENV PATH="${PATH}:/root/poetry/bin"

RUN mkdir /parser_bot
COPY parser_bot/. /parser_bot

COPY poetry.lock pyproject.toml /
RUN poetry install --no-dev --no-interaction

CMD ["poetry", "run", "python", "-m", "parser_bot.main"]



