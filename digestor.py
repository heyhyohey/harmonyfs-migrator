#!/bin/python

import os
import sys
import time

# Global variables
PMEM_HOME="/mnt/pmem/pmem"
SSD_HOME="/mnt/ssd"

# Migrate files
def migration():
    os.system("mv /mnt/pmem/pmem/dummy /mnt/ssd/")
    print("migration!!!")

# Check remaining space periodically
while True:
    pmem_stat = os.popen("df | grep pmem0").read()
    pmem_stat = str(pmem_stat)

    if pmem_stat == "":
        print("Warnning: No mounted pmem device")
        sys.exit(1)

    pmem_stat = ' '.join(pmem_stat.split())
    pmem_stat = int(list(pmem_stat.split())[4][:-1])
    print(pmem_stat)
    
    # If remaining space is above the threshold
    if pmem_stat >= 20:
        migration()
    time.sleep(1)

