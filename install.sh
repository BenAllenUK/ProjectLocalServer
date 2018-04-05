echo "Please enter environment number:"
read envrioNumber
echo "export ENV_NUM="$envrioNumber >> ~/.bashrc
source ~/.bashrc

sudo systemctl enable ssh
sudo systemctl start ssh

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install screen mc vim git htop

wget -qO - 'https://bintray.com/user/downloadSubjectPublicKey?username=openhab' | sudo apt-key add -
sudo apt-get install apt-transport-https
sudo apt-get install libudev-dev
sudo adduser openhab dialout
sudo adduser openhab tty
#RESTART
echo 'deb https://dl.bintray.com/openhab/apt-repo2 stable main' | sudo tee /etc/apt/sources.list.d/openhab2.list
sudo apt-get update
sudo apt-get install openhab2

sudo /etc/init.d/openhab2 start
sudo /etc/init.d/openhab2 status

sudo update-rc.d openhab2 defaults
clear
hostname -I

#sudo reboot
