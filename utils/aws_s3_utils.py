import boto3
from django.conf import settings
import os


def upload_file_to_s3(file):

    session = boto3.Session(
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )
    s3 = session.resource('s3')
    s3.meta.client.upload_file(Filename=file, Bucket=settings.AWS_BUCKET_NAME, Key=file)
    os.remove(file)
