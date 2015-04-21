__author__ = 'roscoe'
import os
from src.geogigpy import Repository
from src.geogigpy import geogig
from datetime import datetime
from src.geogigpy.geogigexception import GeoGigException

class GeoRepo(object):

    def __init__(self, remote, path):
        """constructor"""
        self.remote = remote
        self.path = path
        self.sql_database = os.path.join(self.path, 'database.sqlite')
        self.local_repo = self.connect2repo()
        self.root_path = os.path.normpath(__file__)

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
        print "Trying to export layers to database.sqlite"
        for t in self.local_repo.trees:

            if t.path not in ("layer_statistics", "views_layer_statistics", "virts_layer_statistics"):
                try:
                    self.local_repo.exportsl('HEAD', t.path, self.sql_database)
                except GeoGigException, e:
                    print e
                    continue

    def export_to_shapefiles(self):
        print "Trying to export layers to shapefiles"
        for t in self.local_repo.trees:
            print t.path

            if t.path not in ("layer_statistics", "views_layer_statistics", "virts_layer_statistics"):
                print "t.path: " + t.path
                try:
                    self.local_repo.exportshp('HEAD', t.path, os.path.join('HEAD', t.path,
                                                                           os.path.join(self.path, t.path) + '.shp'))
                except GeoGigException, e:
                    print e
                    continue

    def import_from_spatialite(self):
        try:
            self.local_repo.importsl(self.sql_database, 'all')
            print 'Importing spatialite database'
        except GeoGigException, e:
            print e

    def import_all_shapefiles(self):
        for f in os.listdir(self.path):
            if f.endswith(".shp"):
                shp_path = os.path.join(self.path, f)
                print shp_path
                try:
                    self.local_repo.importshp(shp_path)
                except GeoGigException, e:
                    print e
                    continue


    def add_commit_push(self, name, email, message, input_type):
        message += " " + str(datetime.now())
        self.local_repo.config(geogig.USER_NAME, name)
        self.local_repo.config(geogig.USER_EMAIL, email)
        try:
            if input_type == "spatialite":
                self.import_from_spatialite()
                print 'Spatialite imported.'
            else:
                self.import_all_shapefiles()
                print 'Shapefiles imported.'

        except GeoGigException, e:
            print 'Error with import_from_spatialite()'
        try:
            self.local_repo.addandcommit(message)
            print 'Repo added and committed.'
        except GeoGigException, e:
            print e
        # try:
        #     self.local_repo.push("origin")
        #     print 'Repo pushed.'
        # except GeoGigException, e:
        #     print e

    def push_to_remote(self):
        try:
            print self.local_repo.remotes.items()
            self.local_repo.push("origin","master",True)

            print 'Repo pushed.'
        except GeoGigException, e:
            print e

    def pull_from_remote(self):
        try:
            self.local_repo.pull("origin")
        except GeoGigException, e:
            print e



        # Notes:
        # ------------------------------------------------------------------------
        # changed self.connector.importpg to self.connector.importsl in repo.py
        # changed commands.extend(["--table", table]) to commands.extend(["--all"])
        # def importsl(self, database, table, add = False, dest = None):
        #     self.connector.importsl(database, table, add, dest)
        # GeoGig can only import spatialite tables that have been created by
        # export db from Geogig.