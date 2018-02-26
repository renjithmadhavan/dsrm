#!/bin/sh

cd ~
git clone git clone https://github.com/renjithmadhavan/dsrm.git
curl -O https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
bash Anaconda3-5.0.1-Linux-x86_64.sh
source ~/.bashrc
conda create --name ml101 python=3
source activate ml101
cd ~
jupyter notebook --generate-config
echo "c.NotebookApp.password = 'sha1:62fe0f984350:6f1ac3b3da2573e2f997518e346eee917cb1521b'" >> ~/.jupyter/jupyter_notebook_config.py
echo "alias mlstart='cd ~/dsrm; jupyter notebook --no-browser --ip=0.0.0.0'" >> ~/.bashrc
echo "source activate ml101" >> ~/.bashrc
source ~/.bashrc
