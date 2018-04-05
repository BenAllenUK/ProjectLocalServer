echo "Please enter environment number:"
read envrioNumber
echo $envrioNumber >> /home/pi/Desktop/environment_number

sudo systemctl enable ssh
sudo systemctl start ssh

sudo apt-get update
sudo apt-get upgrade

sudo apt-get -y install screen mc vim git htop

wget -qO - 'https://bintray.com/user/downloadSubjectPublicKey?username=openhab' | sudo apt-key add -
sudo apt-get -y install apt-transport-https
sudo apt-get -y install libudev-dev
#RESTART
echo 'deb https://dl.bintray.com/openhab/apt-repo2 stable main' | sudo tee /etc/apt/sources.list.d/openhab2.list
sudo apt-get update
sudo apt-get -y install openhab2

sudo adduser openhab dialout
sudo adduser openhab tty
sudo cp openhab2 /etc/default/openhab2

sudo /etc/init.d/openhab2 start
sudo /etc/init.d/openhab2 status

sudo update-rc.d openhab2 defaults
cp ./rc.local /etc/rc.local
clear
hostname -I

#sudo reboot
