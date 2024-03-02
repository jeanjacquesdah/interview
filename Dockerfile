#Use an official Python image as the base image
FROM python:3.8-slim

# Set the working directory within the container to the application's directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any required dependencies for the application
RUN pip install --trusted-host pypi.python.org Flask

# Expose the port on which the application runs within the Docker container (8080)
EXPOSE 8080

#Define env variable
ENV NAME WORLD

# Specify the command to run the application when the container starts
CMD ["python", "web-server.py"]

#this Dockerfile to build a Docker image, which, when run, will execute your Flask application.