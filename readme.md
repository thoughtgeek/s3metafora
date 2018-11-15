AWS S3 File Uploader


Instructions

1. Add a file '.env' in the root with the following information -

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = ''
SECRET_KEY = ''

2. Please run the following commands after initializing a virtualenv -

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver (For Development Server)