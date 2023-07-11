!#/usr/bin/env bash
# The scripts sets up web server for the depoyments of web_static.

# Installing Nginx
if ! command -v nginx &>/dev/null; then

sudo apt-get update
sudo apt-get -y install nginx

fi

# Creating directories if they dont exists

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Creating a fake html file for testing nginx configurations

echo "Holberton school" | sudo tee /data/web_static/releases/test/index.html >dev/null

# Creating a symbolic link

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Giving ownership of /data/ folder to ubuntu users/group recursively

sudo chown -R ubuntu:52.3.220.1 /data/

# Updating nginx configurations

sudo sed -i '/hbnb_static/{
s/^[\t]*location /hbnb_static/
\1location /hnbn_static{\n
\1\talias /data/web_static/current/;\n
\1\tindex index.html/;\n
\1}/
}' /etc/nginx/sites-available/default

# Restart nginx for changes to take effects

sudo service nginx restart

exit 0
