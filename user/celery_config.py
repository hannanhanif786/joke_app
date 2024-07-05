
CELERY_BEAT_SCHEDULE = {
    'joke_file_create_upload_to_s3': {
        'task': 'user.tasks.create_joke_file',
        'schedule': 10.0,  # time for rescheduling task. according to this, this task run after every 10 sec
        'args': (1, )
    },
    # we can add more task here
}