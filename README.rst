===========
RHoK Planet
===========


Installation instructions
=========================

Before starting work on this project, you will need to have the following
software installed and in your PATH:

* The git command-line client, version 1.5.3 or higher:

  - To verify that it is available, run ``git --version`` and verify the
    version is something like ``git version 1.6.6.1``
  - If not, you can download one of the installers from http://git-scm.com/ or
    from your operating system provider.

* PostGIS or Spatialite

   Follow the GeoDjango install document::

       http://docs.djangoproject.com/en/dev/ref/contrib/gis/install/

  - If using postgis create your DB from the template database (if available):
    createdb rhokplanet -T template_postgis
    
  - If using spatialite, use the init script in the sql folder:
    spatialite dev.db < init_spatialite-2.3.sql

#. Create a virtualenv and activate it::

  virtualenv rhok;
  cd rhok;
  source bin/activate;

#. Clone the project::

  git clone git://github.com/rhok-planet/rockplanet.git

#. Install the requirements::

  pip install -r rockplanet/requirements.txt

#. Create the database::

  cd rockplanet;
  # It is very important to leave user creation to the end, because the Profile model
  # has a geometry column and that has to be created before the first user is created 
  python manage.py syncdb --no-input
  # Since you did not create it during syncdb, it is time to create the first superuser
  python manage.py createsuperuser

#. Run the development server::

  python manage.py runserver

#. Point your browser to::

  http://localhost:8000/
