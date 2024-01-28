FROM python:3.9
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache pip install -r requirements.txt
COPY . .
