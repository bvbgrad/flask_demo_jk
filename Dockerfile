# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /demo

# copy the dependencies file to the working directory
COPY docs/requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY flask_demo.py .

WORKDIR /demo/app
COPY  app .
WORKDIR /demo

# command to run on container start
CMD [ "python", "./flask_demo.py" ]
# CMD ["sh"]