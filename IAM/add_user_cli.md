# IAM USERS:  

An IAM user is an identity with long-term credentials that is used to interact with AWS in an account.  

## Create an IAM user without any permission

```
aws iam create-user \
    --user-name Mark 
```

## Attach an IAM managed policy to a user:

```
aws iam attach-user-policy \
    --user-name Mark 
    --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess 

```

## create an IAM user with a set permissions boundary

```
aws iam create-user \
    --user-name James \
    --tags '{"Key": "projet", "Value": "training"}' \
    --permissions-boundary arn:aws:iam::aws:policy/AmazonS3FullAccess
```


## Verify that the policy is attached to the user:

```
aws iam list-attached-user-policies \
    --user-name Mark
```

## Set an initial password for an IAM user

```
aws iam create-login-profile \
    --user-name Mark \
    --password myP@ssw0rd \
    --password-reset-required 
```

## Delete an IAM user:  

```
aws iam delete-user \
    --user-name Mark \
    --profile axelt
```
