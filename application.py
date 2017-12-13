"""Application."""

from raven.contrib import flask

from python_crud import api
from python_crud import config
from python_crud import handlers  # noqa


if config.SENTRY:
    api.app.config['SENTRY_DSN'] = config.SENTRY
    flask.Sentry(api.app)

app = api.app
