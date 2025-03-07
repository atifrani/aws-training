# IAM USERS:  

An IAM user is an identity with long-term credentials that is used to interact with AWS in an account.  

## Create an IAM user without any permission

```
import boto3
from botocore.exceptions import ClientError
import logging

# Create IAM client
session = boto3.Session(profile_name='default')
iam = session.client('iam')
logger = logging.getLogger(__name__)

# Create user
def create_user(user_name):
    """
    Creates a user. By default, a user has no permissions or access keys.

    :param user_name: The name of the user.
    :return: The newly created user.
    """
    try:
        user = iam.create_user(UserName=user_name)
        logger.info("Created user %s.", user_name)
    except ClientError:
        logger.exception("Couldn't create user %s.", user_name)
        raise
    else:
        return user

user_name = 'Mark'
create_user (user_name)
```

## Attach an IAM managed policy to a user:

```
import boto3
from botocore.exceptions import ClientError
import logging


# Create IAM client
session = boto3.Session(profile_name='axelt')
iam = session.client('iam')
logger = logging.getLogger(__name__)

def attach_policy(user_name, policy_arn):
    """
    Attaches a policy to a user.

    :param user_name: The name of the user.
    :param policy_arn: The Amazon Resource Name (ARN) of the policy.
    """
    try:
        iam.attach_user_policy(
            UserName= user_name,
            PolicyArn= policy_arn
        )
        logger.info("Attached policy %s to user %s.", policy_arn, user_name)
    except ClientError:
        logger.exception("Couldn't attach policy %s to user %s.", policy_arn, user_name)
        raise

user_name = 'Mark'
policy_arn = 'arn:aws:iam::aws:policy/AmazonS3FullAccess'
attach_policy (user_name, policy_arn)
```

## Delete an IAM user:  

```
import boto3
from botocore.exceptions import ClientError
import logging


# Create IAM client
session = boto3.Session(profile_name='axelt')
iam = session.client('iam')
logger = logging.getLogger(__name__)

def delete_user(user_name):
    """
    Deletes a user. Before a user can be deleted, all associated resources,
    such as access keys and policies, must be deleted or detached.

    :param user_name: The name of the user.
    """
    try:
        iam.delete_user(UserName = user_name)
        logger.info("Deleted user %s.", user_name)
    except ClientError:
        logger.exception("Couldn't delete user %s.", user_name)
        raise

user_name = 'Mark'
delete_user (user_name)
```
