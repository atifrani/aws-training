#!/bin/bash
# Update system packages
yum update -y

# Install Apache web server
yum install -y httpd

# Start the Apache service and enable it at boot
systemctl start httpd
systemctl enable httpd

# Create a sample webpage
echo "<h1>Welcome to My EC2 Instance!</h1>" > /var/www/html/index.html
