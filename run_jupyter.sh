#!/bin/sh


username=`/usr/bin/whoami`

. /home/${username}/.bashrc
cd /home/${username}/dsrm

/usr/bin/tmux new-session -d -s my_session 'cd ~/dsrm ; jupyter notebook --no-browser --ip=0.0.0.0' 

