# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GeoGigDialog
                                 A QGIS plugin
 This plugin simplifies the GeoGig workflow .
                             -------------------
        begin                : 2015-03-18
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Roscoe Lawrence
        email                : roscoelawrence@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
import geo_repo
from geogigpy import Repository
from PyQt4 import QtGui, uic
from geogigpy import repo
import csv
import sys
sys.path.append('~/dev/geogig_auto/GeoGigSync/pycharm-debug.egg_FILES/')
sys.path.append('~/dev/pydev/')
import pydevd

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'geogig_module_dialog_base.ui'))


class GeoGigDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(GeoGigDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        #  self.sync_button.clicked.connect(self.clone_repo)
        self.btnClone.clicked.connect(self.clone_repo)
        self.btnSync.clicked.connect(self.sync_repo)

        self.configPath = os.path.dirname(os.path.realpath('geo_repo.py'))
        self.fname = os.path.join(self.configPath, "config.csv")
        self.populate_clone()
        print(self.fname)

    def clone_repo(self):
        remote = self.txtRemote.text()
        path = self.txtDir.text()
        sql_database = path + 'database.sqlite'
        repos = geo_repo.GeoRepo(remote, path, sql_database)
        # Ideally should create a boolean decorator to check if connected.
        repos.export_to_spatialite()

    def sync_repo(self):
        remote = self.txtRemote.text()
        path = self.txtDir.text()
        sql_database = path + 'database.sqlite'

        name = self.txtName.text()
        email = self.txtEmail.text()
        message = self.txtMessage.text()
        repos = geo_repo.GeoRepo(remote, path, sql_database)
        repos.add_commit_push(name, email, message)

    def populate_clone(self):
        if os.path.isfile(self.fname):
            pydevd.settrace('localhost',
            port=53100,
            stdoutToServer=True,
            stderrToServer=True)
            with open(self.fname, 'rb') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in csv_reader:
                    self.txtRemote.setText(row[0])
                    print (row)
        else:
            print "creating new file"
            with open(self.fname, 'wb') as csvfile:
                csv_writer = csv.writer(csvfile, delimiter=' ',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow(['http://localhost:38080'])
                self.txtRemote.setText("http://localhost:38080")


