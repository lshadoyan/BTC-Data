# Use the official Ubuntu as the base image
FROM ubuntu:20.04

# Install system dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Set the working directory in the container
WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "data.py"]
