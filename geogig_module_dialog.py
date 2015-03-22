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

    def clone_repo(self):
        remote = self.txtRemote.text()
        path = self.txtDir.text()
        sql_database = path + 'database.sqlite'
        repoObject = geo_repo.GeoRepo(remote, path, sql_database)
        # Ideally should create a boolean decorator to check if connected.
        repoObject.export_to_spatialite()

    def sync_repo(self):
        remote = self.txtRemote.text()
        path = self.txtDir.text()
        sql_database = path + 'database.sqlite'

        name = self.txtName.text()
        email = self.txtEmail.text()
        message = self.txtMessage.text()
        repoObject = geo_repo.GeoRepo(remote, path, sql_database)
        repoObject.add_commit_push()




