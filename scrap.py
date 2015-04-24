import os
import sys
import csv
# import multiprocessing
# import time
# import sys
# from src.geogigpy import Repository
# from src.geogigpy import geogig
# import subprocess
#
#
# # os.system("C:\\geogig\\bin\\geogig-gateway")
# # print "operations contiue"
#
# def daemon():
#     p = multiprocessing.current_process()
#     os.system("C:\\geogig\\bin\\geogig-gateway")
#     print 'Starting:', p.name, p.pid
#     sys.stdout.flush()
#     time.sleep(2)
#     print 'Exiting :', p.name, p.pid
#     sys.stdout.flush()
#
# def non_daemon():
#     p = multiprocessing.current_process()
#     print 'Starting:', p.name, p.pid
#     sys.stdout.flush()
#     print 'Exiting :', p.name, p.pid
#     sys.stdout.flush()
#
# if __name__ == '__main__':
#     d = multiprocessing.Process(name='daemon', target=daemon)
#     d.daemon = True
#
#     n = multiprocessing.Process(name='non-daemon', target=non_daemon)
#     n.daemon = False
#
#     d.start()
#     time.sleep(1)
#     n.start()
#

import csv

configPath = os.path.dirname(os.path.realpath(__file__))
fname = os.path.join(configPath, "config.csv")
repos_dict = {}

import csv
with open(fname, 'r') as infile:
    reader = csv.reader(infile)
    with open('coors_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        repos_dict = dict(row[:2] for row in reader if row)


for key in repos_dict:
    print key + repos_dict[key]


