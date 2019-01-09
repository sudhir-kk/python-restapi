FROM python:3.7
COPY . /app
WORKDIR /app
EXPOSE 8080
RUN pip install pipenv
RUN pipenv install --system --deploy --skip-lock
CMD ["python", "run.py"]