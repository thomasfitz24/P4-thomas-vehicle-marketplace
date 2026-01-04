from django.conf import settings
import os


def env_flags(request):
    return {"ON_HEROKU": "DYNO" in os.environ}
