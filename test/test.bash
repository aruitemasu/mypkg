#!/bin/bash
# SPDX-FilecopyrightText: 2024 Katsumi Sunahara
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 20 ros2 launch mypkg talk_listen.launch.py | tee - /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'そのまま'
