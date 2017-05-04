===============
wagtail-leaflet
===============

**This project does nothing at all now !**

It's more a POC than every thing else :)


This application provides leaflet blocks integration to Wagtail (StreamFields) blocks

Installation
============

Install application with pypi:

.. code-block:: sh

   $ pip install wagtail-leaflet

Add application to your INSTALLED_APPS:

.. code-block:: python

   INSTALLED_APPS = [
   ...
   'wagtailleaflet',
   'leaflet',
   'djgeojson',
   ...
   ]


Demo project
============

This project aims to demontrate the usage of map blocks in a wagtail project.

Installation
------------

Create a virtualenv and initialize the project

.. code-block:: sh

   $ virtualenv ./virtualenv
   $ . ./virtualenv/bin/activate
   $ cd demo
   $ pip install -r requirements.txt
   $ ./manage.py migrate
   $ ./manage.py createsuperuser

Usage
------------

Launch dev server

.. code-block:: sh

   $ ./manage.py runserver







Enjoy !
=======
