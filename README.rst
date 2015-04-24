Geogig Sync QGIS Plugin
========

This is a very simple QGIS pluin that simplifies version controlling using Geogig. It is intended
to be used between a remote or local repository and a single user. Branches are not yet supported.

Installation
-------------

1) Install Java JRE and JDK.
2) Install geogig as follows:
    - Clone Boundless' Geogig from https://github.com/boundlessgeo/GeoGig.git
    - Add 'GeoGig/bin' to the environment PATH
    - Test GeoGig is working by opening terminal and typing 'geogig'
3) Open terminal and type 'geogig-gateway'. This service needs to run whilst the plugin is being used.
4) Clone GeoGigSync from https://github.com/roscoeZA/GeoGigSync.git
5) Copy the GeoGigSync folder into ~/.qgis2 directory (Make sure all file are executable)
6) Start QGIS and navigate to Plugins -> Manage and Install Plugins and tick the box next to GeoGigSync.




Usage
-----

Usage is described `here <./doc/source/usage.rst>`_.

Examples
--------

You can find `here <./doc/source/examples.rst>`_ some examples on how to use geogig-py for basic and more complex scripting tasks.



Architecture. Connectors
-------------------------

The ``repo`` object delegates most of its work to a connector, which communicates with a GeoGig instance. Currently there are two connectors available:

- A CLI-based connector, which uses the console to call the GeoGig command-line interface and parses its output. It assumes that GeoGig is installed in your system and available in your current PATH. Basically, if you open a console, type ``geogig`` and you get the GeoGig help, you are ready to use a ``geogig-py`` repository using the CLI connector. This is far from efficient, as it has to call GeoGig (and thus, start a JVM) each time an operation is performed.

- A Py4J-based connector, which communicates with a GeoGig gateway server. To start the server, you have to run ``geogig-gateway`` on a console. The server is part of a standar GeoGig distribution.

By default, a ``Repository`` object uses a Py4J-based connector if no connector is passed.

Testing
--------

To run unit tests, just run the ``test.py`` module in ``src/test``. Most of the tests are integration tests, but test data is included and the only requisite is to have GeoGig installed and correctly configured. The geogig-gateway must be running

