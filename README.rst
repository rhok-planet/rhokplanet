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
  python manage.py syncdb

#. Run the development server::

  python manage.py runserver

#. Point your browser to::

  http://localhost:8000/
