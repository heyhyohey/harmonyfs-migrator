#!/bin/zsh

# compile overlay
cd /usr/src/linux-nova
make M=fs/overlayfs modules
