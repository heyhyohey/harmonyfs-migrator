#!/bin/zsh

# compile overlay
cd /usr/src/linux-transparent-digestor
make M=fs/overlayfs modules
