FROM python:2.7-alpine
RUN apk add build-base jpeg-dev zlib-dev sqlite
ENV LIBRARY_PATH=/lib:/usr/lib
RUN mkdir -p /code/sitehe/
WORKDIR /code/sitehe/
RUN pip install Django==1.11.26 Pillow==6.0.0
ADD python-django-he /code
EXPOSE 2506
CMD ["python", "manage.py", "runserver", "0.0.0.0:2506"]
