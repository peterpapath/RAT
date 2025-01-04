#!/bin/bash
# updater for the RAT
# created by : petros

# remove previous version
cd ~
rm -rf RAT

# install new version
git clone https://github.com/peterpapath/RAT.git

# install dependencies
cd RAT
chmod +x install.sh
./install.sh

# self delete
rm -rf ../update.sh