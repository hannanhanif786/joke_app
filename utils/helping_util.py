from utils.aws_s3_utils import upload_file_to_s3


def create_joke_file(jokes, user):
    file_name = f"joke_{user.id}"
    for joke in jokes:
        try:
            with open(file_name, 'a') as f:
                f.write(f"*{joke.setup}*\n")
                f.write(f"{joke.punctuation}\n")
        except FileNotFoundError:
            print('File')
    upload_file_to_s3(file_name)