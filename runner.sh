while true; do
  git stash
  git pull
  python3 check-script.py
  sleep 1h
done
