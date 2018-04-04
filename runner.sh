cd /home/pi/Desktop/ProjectLocalServer
echo $$
while true; do
  stdbuf -oL python3 check-script.py > /home/pi/Desktop/ProjectLocalServer/py-server.log
  git reset --hard HEAD
  git pull
  sleep 1h
done
