FROM python:3.7

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . app
WORKDIR /app

EXPOSE 8000

ENTRYPOINT ["python", "filmes/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]