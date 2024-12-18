# Use the official Python 3.9 image as the base image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV HF_API_KEY=${HF_API_KEY}

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
