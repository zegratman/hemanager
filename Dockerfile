FROM python:2.7-alpine
RUN apk add build-base jpeg-dev zlib-dev sqlite
ENV LIBRARY_PATH=/lib:/usr/lib
ADD python-django-he /code
WORKDIR /code/sitehe/
RUN pip install Django==1.11.10
RUN pip install Pillow==6.0.0
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
