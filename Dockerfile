FROM python:alpine3.7
COPY . /
VOLUME /
RUN pip install -r requirements.txt
CMD ["python", "./schedule.py"]