__author__ = 'roscoe'
import os
import geogigpy
from geogigpy import Repository
from geogigpy import geogig
from geogigpy import repo
from datetime import datetime

class GeoRepo(object):

    def __init__(self, remote, path, sql_database):
        """constructor"""
        self.remote = remote
        self.path = path
        self.sql_database = path + 'database.sqlite'
        #Placeholder repo.
        print os.getcwd()
        self.local_repo = self.connect2repo()


    def connect2repo(self):#, remote, path, sql_database):
        # self.remote = remote
        # self.path = path
        # self.sql_database = sql_database
        if os.path.isdir(os.path.join(self.path, '.geogig')):
            print "Set to existing repo"
            local_repo = Repository(self.path)
            return local_repo
        else:
            local_repo = Repository.newrepofromclone(self.remote, self.path)
            print "New repo from clone"
            return local_repo
            return

    def export_to_spatialite(self):
        try:
            print "Exporting layers to database.sqlite"
            for t in self.local_repo.trees:
                print ""
                print t.path
                try:
                    print self.sql_database
                    self.local_repo.exportsl('HEAD', t.path, self.sql_database)
                finally:
                    pass
        except repo.GeoGigException, e:
            print e

    def import_from_spatialite(self):
        try:
            self.local_repo.importsl(self.sql_database, 'all')
            print 'Importing spatialite database'
        except repo.GeoGigException, e:
            print e

    # def configRepo(self, name = "test", email="a@b.c"):


    def add_commit_push(self):
        message = str(datetime.now())
        self.local_repo.config(geogig.USER_NAME, 'myuser')
        self.local_repo.config(geogig.USER_EMAIL, 'myuser@mymail.com')
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

        #add_commit_push()

        #import_from_spatialite()


        # Notes:
        #------------------------------------------------------------------------
        # changed self.connector.importpg to self.connector.importsl in repo.py
        # changed commands.extend(["--table", table]) to commands.extend(["--all"])
        # def importsl(self, database, table, add = False, dest = None):
        #     self.connector.importsl(database, table, add, dest)
        # GeoGig can only import spatialite tables that have been created by
        # export db from Geogig.