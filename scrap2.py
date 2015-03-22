__author__ = 'roscoe'
import geogigpy
from geogigpy import Repository
from geogigpy import geogig
from geogigpy import repo
class ClassA(object):
    def __init__(self):
        self.repoA = Repository('/tmp/')

    def addStuff(self):
        self.repoA.importsl('/tmp/database.sqlite','all')
        print 'added'

x = ClassA()
x.addStuff()