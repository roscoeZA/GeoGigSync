__author__ = 'roscoe'
import os
from datetime import datetime
import qgis.utils
import qgis.utils

from src.geogigpy import Repository
from src.geogigpy import geogig
from src.geogigpy.geogigexception import GeoGigException
from qgis.core import QgsVectorLayer, QgsMapLayerRegistry


class GeoRepo(object):

    def __init__(self, remote, path, repo_type):
        """constructor"""
        self.repo_type = repo_type
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
            if self.repo_type=="remote":
                local_repo = Repository.newrepofromclone(self.remote, self.path)
                print "New repo from clone"
            else:
                local_repo = Repository(self.path, init=True)
                print "New repo initialized at : %s" % self.path
            return local_repo


    def export_to_shapefiles(self):
        for t in self.local_repo.trees:
            if t.path not in ("layer_statistics", "views_layer_statistics", "virts_layer_statistics"):
                self.local_repo.exportshp('HEAD', t.path, os.path.join('HEAD', t.path,
                                                                       os.path.join(self.path, t.path) + '.shp'))
                # layer = qgis.utils.iface.addVectorLayer(os.path.join(self.path, t.path) + '.shp', t.path, "ogr")
                vl = QgsVectorLayer("Point", "temporary_points", "memory")
                print layer.geometryType()
                pr = vl.dataProvider()
                layer = qgis.utils.iface.addVectorLayer(os.path.join(self.path, t.path) + '.shp', t.path, "ogr")

                # layers = QgsMapLayerRegistry.instance().mapLayers()
                # for name, layer in layers.iteritems():
                #     print 'name: ' + str(name), 'layer type: ' + str(layer.geometryType())


                my_dir = self.path
                print 'deleting %s' % my_dir
                for fname in os.listdir(my_dir):
                    if fname.startswith(t.path):
                        os.remove(os.path.join(my_dir, fname))

    def import_all_shapefiles(self):
        for f in os.listdir(self.path):
            if f.endswith(".shp"):
                shp_path = os.path.join(self.path, f)
                self.local_repo.importshp(shp_path)

    def add_commit_push(self, name, email, message):
        message += " " + str(datetime.now())
        self.local_repo.config(geogig.USER_NAME, name)
        self.local_repo.config(geogig.USER_EMAIL, email)
        try:
            self.import_all_shapefiles()

        except GeoGigException, e:
            print 'Error with import_from_spatialite()'
        try:
            self.local_repo.addandcommit(message)
            print 'Repo added and committed.'
        except GeoGigException, e:
            print e

    def push_to_remote(self):
        try:
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