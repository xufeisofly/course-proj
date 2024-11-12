FROM python:3.10.12
COPY . /course_proj
WORKDIR /course_proj

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN python -m venv venv
RUN source venv/bin/activate
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

ARG DEBIAN_FRONTEND=noninteractive
RUN sed -i 's/deb.debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list
RUN apt-get update
RUN apt-get -qq install nginx
COPY conf/nginx/nginx.conf /etc/nginx/nginx.conf

RUN rm /etc/nginx/sites-available/default
RUN rm /etc/nginx/sites-enabled/default
COPY conf/nginx/sites-available /etc/nginx/sites-available
RUN ln -s /etc/nginx/sites-available /etc/nginx/sites-enabled

EXPOSE 80
CMD ["sh", "./entrypoint.sh"]
