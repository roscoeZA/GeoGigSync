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
from PyQt4 import QtGui, uic
import csv
import sys



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
        self.configPath = os.path.dirname(os.path.realpath(__file__))
        self.fname = os.path.join(self.configPath, "config.csv")
        self.repo_list = []
        #  self.sync_button.clicked.connect(self.clone_repo)

        self.get_fields()
        self.reload()
        self.btnClone.clicked.connect(self.clone_repo)
        self.btnSync.clicked.connect(self.sync_repo)
        self.btnAdd.clicked.connect(self.set_fields)
        self.btnDelete.clicked.connect(self.delete_field)
        self.btnPush.clicked.connect(self.push)

    def clone_repo(self):
        remote = self.listRepos.currentItem().text()
        print self.listRepos.selectedItems()
        self.set_fields()
        path = self.txtDir.text()
        sql_database = os.path.join(path, 'database.sqlite')
        repos = geo_repo.GeoRepo(remote, path)
        # Ideally should create a boolean decorator to check if connected.
        if self.radioSpatialiteClone.isChecked():
            repos.export_to_spatialite()
        else:
            repos.export_to_shapefiles()

    def sync_repo(self):
        remote = self.listRepos.currentItem().text()
        path = self.txtDir.text()
        sql_database = path + 'database.sqlite'

        name = self.txtName.text()
        email = self.txtEmail.text()
        message = self.txtMessage.text()
        input_type = ""
        if self.radioSpatialiteSync.isChecked():
            input_type = "spatialite"
        else:
            input_type = "shapefiles"
        repos = geo_repo.GeoRepo(remote, path)
        repos.add_commit_push(name, email, message, input_type)

    def get_fields(self):
        if os.path.isfile(self.fname):
            with open(self.fname, 'r+b') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in csv_reader:
                    self.repo_list.append(row[0])
        else:
            print "Creating new file"
            with open(self.fname, 'w+b') as csvfile:
                csv_writer = csv.writer(csvfile, delimiter=',',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow(['http://52.10.196.73:38080'])
                self.txtRemote.setText("http://52.10.196.73:38080")

    def set_fields(self):
        new_repo = self.txtRemote.text()
        self.repo_list.append(new_repo)
        self.save()
        self.reload()

    def save(self):
        with open(self.fname, 'w+b') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)

            for item in self.repo_list:
                if item:
                    csv_writer.writerow([item])

    def reload(self):
        self.listRepos.clear()
        self.repo_list = []
        self.get_fields()
        for item in self.repo_list:
            if item:
                self.listRepos.addItem(item)

    def delete_field(self):
        selected = self.listRepos.currentRow()
        self.repo_list.pop(selected)
        self.save()
        self.reload()

    def push(self):
        remote = 'http' #self.listRepos.currentItem().text()
        path = self.txtDir.text()
        repos = geo_repo.GeoRepo(remote, path)
        print "Remote: " + remote + " Path: " + path
        repos.push_to_remote()
        #repos.export_to_shapefiles()





