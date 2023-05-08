#!/usr/bin/env bash
# Sets up web server for deployments of web_static

# Installing Nginx if not already installed
if ! dpkg -s nginx < /dev/null 2>&1; then
    apt-get -y update
    apt-get -y install nginx
fi

# Creating necessary packages
mkdir -p /data/web_static/release/test/
mkdir -p /data/web_static/shared/

# Creating an HTML file
echo "<html>
  <head></head>
  <body>
    Holberton school!
  </body>
</html>" > /data/web_static/release/test/index.html

# Creating symbolic link
rm -rf /data/web_static/current
ln -sf /data/web_static/release/test/ /data/web_static/current

# Give ownership of /data/ to ubuntu user and group
chown -R www-data:www-data /data/

# Updating nginx configurations
config_file="/etc/nginx/sites-available/default"
config_content="server {
    location /hbnb_static {
       alias /data/web_static/current/;
       index index.html;
}
}"

if ! grep -q "location /hbnb_static" "$config_file"; then
   sed -i "/server_name _;/a $config_content" "$config_file"
fi

# Restart nginx
service nginx restart
