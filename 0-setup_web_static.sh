#!/usr/bin/env bash
# Bash Script to Setup Airbnb Static_web 
sudo apt-get update -y
sudo apt-get install -y nginx
sudo chown -R "$USER":"$USER" /var/www/
sudo chown -R "$USER":"$USER" /etc/nginx
mkdir -R  /data/web_static/
mkdir -R /data/web_static/releases/test/
mkdir /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "Hello AirBnb" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current 
chown ubuntu:ubuntu -R /data/
# ToDo: Config ngnix Using Alias
sudo service nginx restart 
