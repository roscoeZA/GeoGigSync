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


Additional Packages
-----
Run easy_install requests
Run easy_intall py4j

Demo Server
--------

http://52.10.196.73:38080
and
http://52.10.196.73:38080
