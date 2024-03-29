#!/bin/zsh

# make filesystem on /dev/pmem0 and mount dax filesystem
mkfs -t ext4 /dev/pmem0
mount -o dax /dev/pmem0 /mnt/pmem

# make filesystem on /dev/pmem0 and mount dax filesystem
:<<'COMMEND'
mkfs -t ext4 /dev/sdb
mount /dev/sdb /mnt/lower
COMMEND

# make directories
mkdir /mnt/pmem/work
mkdir /mnt/pmem/upper

# mount overlayfs
mount -t overlay overlay -o lowerdir=/mnt/lower,upperdir=/mnt/pmem/upper,workdir=/mnt/pmem/work /mnt/merged
