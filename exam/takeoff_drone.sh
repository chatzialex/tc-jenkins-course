#!/bin/bash

python -m unittest test_drone_sim.py

if [ $? -eq 0 ]; then
  rostopic pub /drone/takeoff std_msgs/Empty '{}' &
  TAKEOFF_PID=$!
  sleep 5s
  kill $TAKEOFF_PID
else
  echo "Test failed, not running takeoff."
fi