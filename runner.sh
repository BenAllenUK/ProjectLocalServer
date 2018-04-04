cd /home/pi/Desktop/ProjectLocalServer
while true; do
  python3 check-script.py
  git reset --hard HEAD
  git pull
  sleep 1h
done
