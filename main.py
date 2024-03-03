from celery import Celery

app = Celery(
    'jeevan_celery',
    broker='amqp://guest@localhost//',
)

app.autodiscover_tasks(
    packages =["random_tasks"]
)

if __name__ == "__main__":
    args = ["worker","--loglevel=DEBUG"]
    app.worker_main(argv=args)