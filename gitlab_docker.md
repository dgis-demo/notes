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
3. Edit `/etc/gitlab.rb`


## Gitlab runner
```shell
docker run -d --name gitlab-runner --restart always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  gitlab/gitlab-runner:latest

gitlab-runner register  \
    --url http://172.17.0.3  \
    --token glrt-2nEAY-QJFqJ_U6n2Cx6a \
    --docker-privileged \
    --docker-volumes "/certs"
```
