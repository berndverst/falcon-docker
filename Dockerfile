FROM python:alpine

EXPOSE 80

# Install gunicorn & falcon
RUN pip install gunicorn falcon

# Add demo app
COPY ./app /app
WORKDIR /app

CMD ["gunicorn", "-b", "0.0.0.0:80", "main:app"]
