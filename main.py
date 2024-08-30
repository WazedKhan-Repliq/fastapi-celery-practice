from my_celery_app import hello_world, hello_earth

hello_world.delay()
hello_earth.delay()
