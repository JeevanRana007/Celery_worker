from celery import shared_task


@shared_task(name="say_hello")
def say_hello(name="JEEVAN"):
    print("Hello {}".format(name))

@shared_task(name="say_bye")
def Bye(name):
    print("Bye {}".format(name))