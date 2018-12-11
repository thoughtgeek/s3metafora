# s3Metafora - README
### A simple S3 file uploader
---
#### Instructions to run on localhost or EC2 instance:

Add a file '.env' in the root with the following information
```python
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = ''
SECRET_KEY = ''
```

# Zappa Deployment Steps


#### Instructions to run on AWS lambda

In settings.py add this line:
```python
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```
Replace the following lines in settings.py:
```python
SECRET_KEY = config('SECRET_KEY')
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
```

By,
```python
SECRET_KEY = os.environ.get('SECRET_KEY')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
```

** Set the database in settings.py and run 'python manage.py migrate --run-syncdb' **


Set permissions for IAM user, by adding following policies to the user:

```
* AmazonAPIGatewayAdministrator
	* AWS managed policy
* AmazonCloudDirectoryFullAccess
	* AWS managed policy
* AmazonEC2FullAccess
	* AWS managed policy
* AmazonS3FullAccess
	* AWS managed policy
* AWSLambdaFullAccess
	* AWS managed policy
* IAMFullAccess
	* AWS managed policy
* AmazonVPCFullAccess
	* AWS managed policy
* AWSCloud9Administrator
	* AWS managed policy
* SecurityAudit
```
Add custom policy to give IAM user full access to Cloudformation:
```json
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
```
Add AWS credentials -
Create a new directory and file ~.aws/credentials and add the following lines:
```python
[default]
aws_access_key_id = YOUR ACCESS KEY
aws_secret_access_key = YOUR SECRET ACCESS KEY
```
To deploy, run:  
```sh
python manage.py collectstatic
zappa init
```
In zappa_settings.json replace 'dev' with the name of your deployment and setting its corrosponding values:

```json
{
    "dev": {
        ...
        "environment_variables": {
            "AWS_ACCESS_KEY_ID": "your_value",
            "SECRET_KEY" : "your_value",
            "AWS_SECRET_ACCESS_KEY" : "your_value",
            "AWS_STORAGE_BUCKET_NAME" : "your_value",

        }
    },
    ...
}
```

Finally,
```sh
zappa deploy
```
