__author__ = 'roscoe'
import os
import geogigpy
from geogigpy import Repository
from geogigpy import geogig
from geogigpy import repo
from datetime import datetime
import pydevd

class GeoRepo(object):

    def __init__(self, remote, path, sql_database):
        """constructor"""
        self.remote = remote
        self.path = path
        self.sql_database = path + 'database.sqlite'
        print os.getcwd()
        self.local_repo = self.connect2repo()

    def connect2repo(self):
        if os.path.isdir(os.path.join(self.path, '.geogig')):
            print "Set to existing repo"
            local_repo = Repository(self.path)
            return local_repo
        else:
            local_repo = Repository.newrepofromclone(self.remote, self.path)
            print "New repo from clone"
            return local_repo

    def export_to_spatialite(self):
        print "Exporting layers to database.sqlite"
        for t in self.local_repo.trees:
            print t.path

            if t.path not in ("layer_statistics", "views_layer_statistics", "virts_layer_statistics"):
                print "t.path: " + t.path
                try:
                    self.local_repo.exportsl('HEAD', t.path, self.sql_database)
                except repo.GeoGigException, e:
                    print e
                    continue

    def import_from_spatialite(self):
        try:
            self.local_repo.importsl(self.sql_database, 'all')
            print 'Importing spatialite database'
        except repo.GeoGigException, e:
            print e

    def add_commit_push(self, name, email, message):
        message += " " + str(datetime.now())
        self.local_repo.config(geogig.USER_NAME, name)
        self.local_repo.config(geogig.USER_EMAIL, email)
        try:
            self.import_from_spatialite()
            print 'Spatialite imported.'
        except repo.GeoGigException, e:
            print 'Error with import_from_spatialite()'
        try:
            self.local_repo.addandcommit(message)
            print 'Repo added and committed.'
        except repo.GeoGigException, e:
            print e
        try:
            self.local_repo.push("origin")
            print 'Repo pushed.'
        except repo.GeoGigException, e:
            print e

        # Notes:
        # ------------------------------------------------------------------------
        # changed self.connector.importpg to self.connector.importsl in repo.py
        # changed commands.extend(["--table", table]) to commands.extend(["--all"])
        # def importsl(self, database, table, add = False, dest = None):
        #     self.connector.importsl(database, table, add, dest)
        # GeoGig can only import spatialite tables that have been created by
        # export db from Geogig.