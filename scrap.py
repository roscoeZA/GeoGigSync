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

with open(fname, 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

with open(fname) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # print(row['first_name'], row['last_name'])
        repos_dict[row['first_name']] = row['last_name']


print repos_dict


