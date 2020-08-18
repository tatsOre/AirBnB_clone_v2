#!/usr/bin/env bash
# Bash script that configures a new Ubuntu machine and sets up web servers for the deployment of 'web_static'

apt-get -y update
apt-get -y upgrade
apt-get -y install nginx

# Creates folders recursively:
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared

# Creates a HTML file /data/web_static/releases/test/index.html to test your Nginx configuration:
echo "Hello World" | sudo tee /data/web_static/releases/test/index.html

# Creates a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder. 
# If the symbolic link already exists, will override:
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Changes ownership of the /data/ folder to the ubuntu user AND group:
# -h, --no-dereference (affect symbolic links)
chown -hR ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of '/data/web_static/current/' to 'hbnb_static'
sudo sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default

sudo service nginx restart
