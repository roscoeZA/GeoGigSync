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
repo_list = {}
with open('C:\Users\Roscoe\.qgis2\python\plugins\GeoGigSync-master\config.csv', 'r+b') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in csv_reader:
        print row
        repo_list.(row)

print '-------------'
for item in repo_list:
    print item

print repo_list.viewitems()

print '-------------'
for item in repo_list:
    print item