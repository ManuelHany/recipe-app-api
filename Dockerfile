# alpine is a very light weight version of linux 
FROM python:3.9-alpine3.13

LABEL maintainer="manuelhany@gmail.com"

ENV PYTHONUNBUFFERED 1

# copy from local machine to container directory
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
# set working directory so running django commands won't need full path
WORKDIR /app
# access container through port 8000
EXPOSE 8000

ARG DEV=false
# specify a single run command because spreading the commands 
# int multiple RUN commands will divide them into multiple image
# layers which we would like to avoid.  
RUN python -m venv /py && \
/py/bin/pip install --upgrade pip && \
/py/bin/pip install -r /tmp/requirements.txt && \
if [ $DEV = "true" ]; \
    then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
fi && \
rm -rf /tmp && \
adduser \
    --disabled-password \
    --no-create-home \
    django-user

# PATH is the environment variable that is created automatically
# by linux. Which contains all the possible paths for any executables.
# To avoid always having to pass the full path for our commands.
# we add the /py/bin to the system paths.  
ENV PATH="/py/bin:$PATH"
 
# This should be the last command inside a docker image. 
# N.B. all of the previous commands where made by the root user.
USER django-user
