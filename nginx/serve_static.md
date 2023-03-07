## Serve static for a Django project
1) Define a couple of necessary `Django` settings like the following:
```python
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "collected_static"
```
2) Install `nginx` inside a docker container (see a Dockerfile) and replace its default config like this:
```Dockerfile
RUN apt-get update && apt-get install -y \
    nginx

RUN rm -v /etc/nginx/nginx.conf
COPY backoffice_nginx.conf /etc/nginx/nginx.conf

ENTRYPOINT ["sh", "backoffice_start_in_docker.sh"]
```
3) `backoffice_nginx.conf` must contain the following:
```
events {
    worker_connections 1024;
    accept_mutex       off;
    use                epoll;
    multi_accept       on;
}

http {
    charset utf-8;
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    server {
        listen 8800;

        location / {
            proxy_pass http://0.0.0.0:8000;
            proxy_set_header Host $http_host;
            proxy_set_header X-Real-IP $remote_addr;
        }

        location /static {
            alias /app/backoffice/collected_static;
        }
    }
}
```
4) `backoffice_start_in_docker.sh` file must contain the following lines:
```bash
#!/usr/bin bash

python3 /app/backoffice/manage.py migrate --noinput
python3 /app/backoffice/manage.py collectstatic --noinput

exec "$@"
```
5) Set an appropriate command in `docker-compose.yml` file for a `Django` container:
```yml
command:
  - bash
  - -c
  - |
    nginx
    python3 /app/backoffice/manage.py runserver 0.0.0.0:8000
```
6) Create the containers with `docker compose up` command
