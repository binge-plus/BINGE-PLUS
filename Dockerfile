# Use an official Ubuntu image as a base
FROM ubuntu:latest

# Install Apache2
RUN apt-get update && \
    apt-get install -y apache2 && \
    apt-get clean

# Set working directory
WORKDIR /var/www/html

# Copy your website files to the container
COPY . .

# Expose port 80 to the outside world
EXPOSE 80

# Start Apache2 server
CMD ["apachectl", "-D", "FOREGROUND"]

