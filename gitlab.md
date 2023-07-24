## Run Gitlab in a Docker container
1. Run the following command:
```shell
docker run --detach \
  --publish 1443:443 --publish 8880:80 --publish 2200:22 \
  --name gitlab \
  --restart always \
  --shm-size 2gb \
  gitlab/gitlab-ce:latest
```
2. Go to `http://localhost:8880`
