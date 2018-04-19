from celery import Celery

app = Celery()


@app.task
def panic():
    """
    TODO add celery periodic task
    :return:
    """
    pass


if __name__ == '__main__':
    app.worker_main()
