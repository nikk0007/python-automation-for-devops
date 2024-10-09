How to Dockerize a FLASK application:

The basic idea is to package your Flask app with all its dependencies into a Docker container.

1. Make sure to use host='0.0.0.0' in app.run() so that Flask listens on all interfaces inside the container.
==> use  app.run(host='0.0.0.0') instead of  app.run()
-------------------------------------

2. Create a requirements.txt file
This file will list all the dependencies your Flask app needs. If you haven’t created one yet, you can generate it by running:

pip freeze > requirements.txt

For example, it might contain:
Flask==2.0.1
-------------------------------------

3. Create a Dockerfile
The Dockerfile is the recipe Docker uses to build your image. Here’s a basic Dockerfile to Dockerize your Flask app:

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run flask when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
-------------------------------------

4. Create a .dockerignore File (Optional)
Just like .gitignore, .dockerignore tells Docker which files and directories to ignore during the build process. Create a .dockerignore file to avoid copying unnecessary files into the Docker image:

__pycache__
*.pyc
.env
.git
-------------------------------------
5. Build the Docker Image
Once you have your Dockerfile and requirements.txt, you can build the Docker image.

In the directory where your Dockerfile is located, run the following command:

docker build -t flask-app .

-t flask-app: This tags the image with the name flask-app.
. : Tells Docker to look for the Dockerfile in the current directory.
-------------------------------------

6. Run the Docker Container
Once the image is built, you can run it as a container:

docker run -d -p 5000:5000 flask-app

-d: Runs the container in detached mode (in the background).
-p 5000:5000: Maps port 5000 on your host to port 5000 in the container.

Now, open your browser and go to http://localhost:5000. You should see the "Welcome to the home page!" message from your Flask app.
-------------------------------------

7. Verify the Container is Running
You can verify that the container is running by using:

docker ps
-------------------------------------

8. Stopping and Removing the Container
To stop the running container:

docker stop <container_id>
To remove the container:

docker rm <container_id>
You can also remove the image using:

docker rmi flask-app
-------------------------------------
