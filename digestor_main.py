#!/bin/python

import os
import sys
import time
import digestor_migration as migration

# Global variables
PMEM_HOME="/mnt/pmem/pmem"
SSD_HOME="/mnt/ssd"

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
    
    # If remaining space is above the pm threshold
    if pmem_stat <= 50:
        migration.migration_to_upper()

    # If remaining space is the threshold
    if pmem_stat >= 80:
        migration.migration_to_lower()

    time.sleep(1)

