# Create Ec2 instance with aws cli:

To create a free-tier eligible EC2 instance using AWS CLI, you can use the following command:

```
aws ec2 run-instances \
    --image-id xxx \
    --instance-type t2.micro \
    --key-name XXX \
    --security-groups xxx \
    --count 1 \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=webserver}]' \
    --user-data file://user-data.sh \
    --query 'Instances[0].InstanceId' \
    --output text
```

## Explanation:
* --image-id ami-0c55b159cbfafe1f0 → Amazon Machine Image (AMI) for Amazon Linux 2 (Check the latest AMI for your region with aws ec2 describe-images).
* --instance-type t2.micro → Free-tier eligible instance type.
* --key-name MyKeyPair → Name of your existing key pair (must be created before using aws ec2 create-key-pair).
* --security-groups MySecurityGroup → Name of an existing security group (Ensure it allows SSH if you want remote access).
* --count 1 → Launches one instance.
* --tag-specifications → Tags the instance with Name=MyFreeTierInstance.
* --user-data option in your AWS CLI command to run a script when the instance starts.
* --query 'Instances[0].InstanceId' --output text → Returns only the instance ID.


# Verify After Instance Launch

* List running instances:
```
aws ec2 describe-instances 
```
* Once the instance is running, find its public IP:
```
aws ec2 describe-instances --query "Reservations[*].Instances[*].PublicIpAddress" --output text
```

