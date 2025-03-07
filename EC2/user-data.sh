#!/bin/bash
# Update system packages
sudo yum update -y

# Install Apache web server
sudo yum install -y httpd

# Start the Apache service and enable it at boot
sudo systemctl start httpd
sudo systemctl enable httpd

# Create a sample webpage
echo "<h1>Welcome to My EC2 Instance!</h1>" > /var/www/html/index.html
