FROM python:3.10-slim-bullseye as base

SHELL ["/bin/bash", "-c"]

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl &&  \
    rm -rf /var/lib/apt/lists/*


FROM base as builder

COPY requirements.txt .

RUN python -m venv /venv && \
    source /venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt


FROM base

WORKDIR /home/django

COPY --from=builder /venv /venv

ENV PATH="/venv/bin:$PATH"

ENV PYTHONUNBUFFERED 1

COPY . .

RUN chmod +x /home/django/entrypoint.sh

ENTRYPOINT ["/home/django/entrypoint.sh"]

CMD ["gunicorn"]

EXPOSE 8000
