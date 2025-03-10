# Python Script to Launch EC2 Instance
```
import boto3

# Initialize EC2 client
ec2 = boto3.client("ec2")

# Define user data script
user_data_script = """#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo '<h1>Welcome to My EC2 Instance!</h1>' > /var/www/html/index.html
"""

# Launch EC2 instance
response = ec2.run_instances(
    ImageId="ami-0c55b159cbfafe1f0",  # Update this with the latest AMI ID for your region
    InstanceType="t2.micro",
    KeyName="MyKeyPair",
    SecurityGroups=["MySecurityGroup"],
    MinCount=1,
    MaxCount=1,
    TagSpecifications=[
        {
            "ResourceType": "instance",
            "Tags": [{"Key": "Name", "Value": "MyFreeTierInstance"}],
        }
    ],
    UserData=user_data_script,
)

# Extract Instance ID
instance_id = response["Instances"][0]["InstanceId"]
print(f"EC2 Instance Created: {instance_id}")
```

##How This Works
* Uses boto3.client("ec2") to interact with AWS EC2.
* Defines the user_data_script to install Apache and create a web page.
* Calls run_instances() to create an instance with the same settings as your AWS CLI command.
* Prints the Instance ID once the instance is launched.

## Next Steps

* Run this script in a Python environment with AWS credentials configured (aws configure).
* Retrieve the public IP of your instance:

```
instance_info = ec2.describe_instances(InstanceIds=[instance_id])
public_ip = instance_info["Reservations"][0]["Instances"][0]["PublicIpAddress"]
print(f"Access your instance: http://{public_ip}")
```
* Open a browser and visit http://<PUBLIC_IP> to see the webpage!