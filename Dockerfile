# Dockerfile - this is a comment. Delete me if you want.
FROM python:2.7
WORKDIR /app
COPY app.py /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
