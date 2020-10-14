#!/bin/python

import os

# 1. Get remaining space
pmem_stat = os.popen("df | grep pmem0").read()
pmem_stat = str(pmem_stat)
pmem_stat = ' '.join(pmem_stat.split())
pmem_stat = int(list(pmem_stat.split())[4][0])
print(pmem_stat)
