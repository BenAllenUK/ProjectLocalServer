cd /home/pi/Desktop/ProjectLocalServer
while true; do
  python3 -u check-script.py >> /home/pi/Desktop/py-server.log
  git reset --hard HEAD
  git pull
  sleep 1h
done
