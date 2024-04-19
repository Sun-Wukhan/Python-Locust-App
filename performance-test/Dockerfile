# Use an official Python runtime as a base image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8089 available to the world outside this container
EXPOSE 8089

# Define environment variable
ENV NAME=LocustApp

# Run locust using variables which will be passed by Kubernetes ConfigMap
CMD ["sh", "-c", "locust -f ${LOCUST_FILE} --host=${HOST} --users=${USERS} --spawn-rate=${SPAWN_RATE} --run-time=${RUN_TIME} --headless --logfile logs/locust_log.txt --html logs/locust_report.html"]
