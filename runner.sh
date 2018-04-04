cd /home/pi/Desktop/ProjectLocalServer
while true; do
  git reset --hard HEAD
  git pull
  python3 check-script.py
  sleep 1h
done
