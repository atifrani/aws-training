#  Run EC2 instance with user data

aws ec2 run-instances 
--image-id ami-xxxxx
--count 1 
--instance-type t2.micro \
--key-name EC2ProjectKeyPair 
--subnet-id subnet-xxxx 
--security-group-ids sg-xxxxx \
--user-data file://my_script.txt

# List ec2 instances:

aws ec2 describe-instances


# Start EC2 instance:
aws ec2 start-instances --instance-ids i-dxxxx

# Stop EC2 instance:
aws ec2 stop-instances --instance-ids i-dxxxx


# Terminate EC2 instance:

aws ec2 terminate-instances --dry-run --instance-ids i-dxxxx