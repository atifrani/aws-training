# Workshop :

This application is built with Python FastAPI and Streamlit frameworks and POSTGRESQL  integrating for CRUD operations (Create, Read, Update, Delete) on books and users. 

* FastAPI is a powerful web framework for building APIs, 
* Streamlit is UI web framework to deliver dynamic data apps with only a few lines of code,  
* POSTGRESQL is a SQL database that provides flexibility and scalability.

## Backend: 
FastAPI for managing books and users
This backend exposes REST endpoints for adding, searching, borrowing books, and managing users.

## Frontend: 
Streamlit to deliver web UI to interact with the backend.

## Create aws infrastructure:
We will create some aws services to host the application.

1. Create aws Security group for EC2.

You need to update the following commands before run it in your terminal.

```
aws ec2 create-security-group --group-name ec2-SecurityGroup --description "Security group for HTTP and SSH access"
```

This command returns a **GroupId**, which you will use in the next steps.

**Authorize Inbound HTTP Traffic (Port 80)**:
```
aws ec2 authorize-security-group-ingress --group-name ec2-SecurityGroup --protocol tcp --port 80 --cidr 0.0.0.0/0
```
This allows anyone on the internet to access the server via HTTP.

**Authorize Inbound SSH Traffic (Port 22)**:
```
aws ec2 authorize-security-group-ingress --group-name MySecurityGroup --protocol tcp --port 22 --cidr 0.0.0.0/0
```
This allows SSH access from anywhere.

**Launch an EC2 Instance**:

```
aws ec2 run-instances \
    --image-id ami-1234567890abcdef0 \ # Replace with a valid AMI ID (e.g., Amazon Linux 2)
    --instance-type t2.micro \
    --key-name MyKeyPair \ # Replace with your key pair name
    --security-group-ids sg-xxxxxxxx \ # Replace with the GroupId from Step before
    --subnet-id subnet-xxxxxxxx \ # Replace with a valid subnet ID
    --count 1 \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=MyEC2Instance}]'

```

**Connect to the EC2 Instance**:

Go the the aws console:
1. select EC2 service and click on instances.
2. Select your EC2 instance
3. click on connect button
4. Connect using EC2 instance connect


# Clone or donwload the project:



```
git clone https...
```

# Create python virtualenv:

```
cd aws-library-project

python -m venv venv

or 

python3 -m venv venv

```

## Activate the virtualenv

```
.\venv\Scripts\activate

ou 

source venv/bin/activate 
```

# Install the dependencies:

```
pip install -r requierements.txt

or 

pip3 install -r requirements.txt
```
# Test the applicaiton localy

## Launch the backend:

Open a terminal and run this command:

```
uvicorn backend:app --reload
```
visite this url **http://127.0.0.1:8000/docs**

## Launch the Frontend:

Open a terminal and run this command:

```
streamlit run frontend.py
```
Visite this url **http://localhost:8501/**