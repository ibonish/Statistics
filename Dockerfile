FROM python:3.9
WORKDIR /statistics
COPY . /statistics/
RUN pip install --no-cache-dir --upgrade -r /statistics/requirements.txt
RUN alembic upgrade head
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
