# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.7-alpine

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install pip requirements
COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

RUN mkdir /src
WORKDIR /src
ADD . /src

RUN adduser -D user
USER user

# During debugging, this entry point will be overridden. For more information, refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "manage.py", "ruserver", "0.0.0.0:8000"]
