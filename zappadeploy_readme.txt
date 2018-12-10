///////////////////////

Zappa Deployment Steps 

///////////////////////

1.In settings.py -
Add this line:
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

Set the values directly for the following(Without using python decouple):
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME

**Set the database in settings.py and run 'python manage.py migrate'


2.Set Permissions for IAM user -
Add following policies to the user:

>AmazonAPIGatewayAdministrator
AWS managed policy
>AmazonCloudDirectoryFullAccess
AWS managed policy
>AmazonEC2FullAccess
AWS managed policy
>AmazonS3FullAccess
AWS managed policy
>AWSLambdaFullAccess
AWS managed policy
>IAMFullAccess
AWS managed policy
>AmazonVPCFullAccess
AWS managed policy
>AWSCloud9Administrator
AWS managed policy
>SecurityAudit

Add custom policy to give IAM user full access to Cloudformation:

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "cloudformation:*",
            "Resource": "*"
        }
    ]
}

3.Add AWS credentials -
Create a new directory and file ~.aws/credentials and add the following lines:

[default]
aws_access_key_id = YOUR ACCESS KEY
aws_secret_access_key = YOUR SECRET ACCESS KEY

4. Deploy -

Run:  
python manage.py collectstatic
zappa init
zappa deploy


