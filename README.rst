===============
Full Stack Hero
===============

ToDo's:

1. like snippet -> done
2. comment snippet -> done
3. make costum render for source code (pygments in model)
4. nicer template for snippet list and details
5. hot page
6. api
7. setup beta server
8. user profil page
9. js front-end
10. filter snippets
11. snippet of the day
12. add language icons
13. post snippet on insta & co
14. user singup (email or fb, insta etc.)


Setup server

sudo apt-get update
sudo apt-get install python3-pip python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx git


sudo -u postgres psql
CREATE DATABASE fsh;
CREATE USER fshuser WITH PASSWORD '1234';
ALTER ROLE fshuser SET client_encoding TO 'utf8';
ALTER ROLE fshuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE fshuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE fsh TO fshuser;


sudo -H pip3 install --upgrade pip
git clone https://github.com/axju/fsh-server.git
cd fsh-server
python3 -m venv venv
source venv/bin/activate
pip install .
python -m pip install gunicorn psycopg2
#gunicorn --bind 0.0.0.0:8000 fsh.wsgi
python -m fsh migrate --settings=fsh.settings.production


sudo nano /etc/systemd/system/gunicorn.service
[Unit]
Description=gunicorn daemon
After=network.target
[Service]
User=user
Group=www-data
WorkingDirectory=/home/user/fsh-server
ExecStart=/home/user/fsh-server/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/user/fsh.sock fsh.wsgi:application
[Install]
WantedBy=multi-user.target

sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl status gunicorn


sudo nano /etc/nginx/sites-available/fsh
server {
    listen 80;
    server_name ip;
    location / {
        include proxy_params;
        proxy_pass http://unix:/home/user/fsh.sock;
    }
}

sudo ln -s /etc/nginx/sites-available/fsh /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
