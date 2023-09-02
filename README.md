# gameshelf
self-hosted video game library tracker

# installation
the simplest way to run gameshelf is with Docker, below is an example Docker Compose file which can be used:
```yml
version: "3.7"
services:
  gameshelf:
    image: public.ecr.aws/alexchesters/gameshelf:latest
    container_name: gameshelf
    restart: unless-stopped
    volumes:
      - gameshelf_static:/var/www/gameshelf/static
      - gameshelf_db:/usr/lib/gameshelf/db
    environment:
      SECRET_KEY: $SECRET_KEY # replace with a unique, unpredictable value - https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-SECRET_KEY
      DEBUG_MODE: false # can be set to true for debugging, but should be used with caution - https://docs.djangoproject.com/en/4.2/ref/settings/#debug
      ALLOWED_HOSTS: mydomain.net # replace with the hostname of your server running gameshelf
      ALLOWED_ORIGINS: https://mydomain.net # replace with the origin of your server running gameshelf
  nginx:
    image: arm64v8/nginx:1.25.2-alpine
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - gameshelf_static:/var/www/gameshelf/static
    ports:
      - 8050:80

volumes:
  gameshelf_static:
  gameshelf_db:
```

The above example uses Nginx as a front to gameshelf, below is an example of an Nginx config file that can be used:
```nginx
events {
  worker_connections 1024;
}

http {
  server {
    listen 80;
    listen [::]:80;

    root /var/www/gameshelf;

    location / {
      proxy_set_header Host $host;
      proxy_pass http://gameshelf:8000;
    }

    location /static/ {
      include /etc/nginx/mime.types;
      proxy_set_header Host $host;
      try_files $uri $uri/ =404;
    }
  }
}
```

# backups and restoring
all data for gameshelf is stored in an SQLite database (in the above Docker Compose example, the SQLite file will be
called `db.sqlite3` and can be found at the root of the `gameshelf_db` volume), this file is the only file needed for
backup/restoring
