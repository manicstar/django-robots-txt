"""
Source: http://datadesk.latimes.com/posts/2012/06/test-your-django-app-with-travisci/
Slightly modified by Nicolas Kuttler.
"""

import os
import sys
import argparse

from django import setup
from django.conf import settings
from django.test.runner import DiscoverRunner


class QuickDjangoTest(object):
    """
    A quick way to run the Django test suite without a fully-configured project.

    Example usage:

        >>> QuickDjangoTest('app1', 'app2')

    Based on a script published by Lukasz Dziedzia at:
    http://stackoverflow.com/questions/3841725/how-to-launch-tests-for-django-reusable-app
    """
    DIRNAME = os.path.dirname(__file__)
    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
    )

    def __init__(self, options, *args, **kwargs):
        self.apps = options.apps
        self._tests()

    def _tests(self):
        """
        Fire up the Django test suite developed for version 1.2
        """
        settings.configure(
            DEBUG=True,
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': os.path.join(self.DIRNAME, 'database.db'),
                    'USER': '',
                    'PASSWORD': '',
                    'HOST': '',
                    'PORT': '',
                }
            },
            INSTALLED_APPS=self.INSTALLED_APPS + tuple(self.apps),
            ROOT_URLCONF='test_project.urls',
            TEMPLATE_DIRS=(
                './test_project/templates/',
            ),
        )

        # Django 1.8
        setup()
        DiscoverRunner().run_tests(self.apps, verbosity=1)


if __name__ == '__main__':
    """
    What do when the user hits this file from the shell.

    Example usage:

        $ python quicktest.py app1 app2

    """
    parser = argparse.ArgumentParser(
        usage="[args]",
        description="Run Django tests on the provided applications."
    )
    parser.add_argument('apps', nargs='+', type=str)
    options = parser.parse_args()
    QuickDjangoTest(options)
