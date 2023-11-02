
FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY djangoapp /djangoapp
COPY scripts /scripts


# Entra na pasta djangoapp no container
WORKDIR /djangoapp

# A porta 8000 estará disponível para conexões externas ao container
# É a porta que vamos usar para o Django.
EXPOSE 8000

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /djangoapp/requirements.txt && \
  adduser --disabled-password --no-create-home duser && \
  chown -R duser:duser /venv && \
  chown -R duser:duser /djangoapp && \
  chmod -R +x /scripts && \
  chmod -R 755 /djangoapp

ENV PATH="/scripts:/venv/bin:$PATH"

# Muda o usuário para duser
USER duser

# Executa o arquivo scripts/commands.sh
CMD ["commands.sh"]