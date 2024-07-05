from celery import shared_task
from utils.aws_s3_utils import upload_file_to_s3
from user.models import Joke


@shared_task
def create_joke_file(user):
    jokes = Joke.objects.filter(user_id=user)
    file_name = f"joke_{user}"
    for joke in jokes:
        try:
            with open(file_name, 'a') as f:
                f.write(f"*{joke.setup}*\n")
                f.write(f"{joke.punctuation}\n")
        except FileNotFoundError:
            print('File')
    upload_file_to_s3(file_name)