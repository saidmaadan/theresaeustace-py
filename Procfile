
web: gunicorn theresaeustace.wsgi --log-file -
release: bash release.sh
beat: celery -A theresaeustace.celeryapp:app beat -S redbeat.RedBeatScheduler  --loglevel=DEBUG --pidfile /tmp/celerybeat.pid
worker: celery -A theresaeustace.celeryapp:app  worker -Q default -n theresaeustace.%%h --without-gossip --without-mingle --without-heartbeat --loglevel=INFO --max-memory-per-child=512000 --concurrency=1

