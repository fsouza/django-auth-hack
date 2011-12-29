django-auth-hack
================

This is a Django application for hacking the builtin ``django.contrib.auth`` application.
This app aims to add support to a longer username field on ``User`` model.

Installation and configuration
==============================

To install this app you need first to add it to your environment using pip:

::

    $ [sudo] pip install django-auth-hack

Then you need to add the ``auth_hacks`` on **top** of your ``INSTALLED_APPS``, before any other application:

::

    INSTALLED_APPS = (
        'auth_hacks',
        # other apps
    )

You can customize the new username max length by defining  the ``USERNAME_MAX_LENGTH`` in your settings file:

::

    USERNAME_MAX_LENGTH = 255

Database
========

Make sure you alter the column ``username`` in the table ``auth_user``. You can use South or run an ``ALTER TABLE``
SQL manually. Using MySQL, you could run:

::

    ALTER TABLE auth_user MODIFY COLUMN auth_user VARCHAR(255) NOT NULL;
