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