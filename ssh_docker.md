## SSH server inside a docker container
1) Install SSH server inside a docker-container:

```command
apt install openssh-server vim
```

2) Change the SSH config:
```
vim /etc/ssh/sshd_config
```
Set the following:
```
PermitRootLogin yes
PermitEmptyPassords yes
```

3) Start the SSH server
```
service ssh start 
/usr/sbin/sshd -D
```

4) Remove the root password:
```
passwd -d root
```

5) Connect to the container:
```
root@<container ip address>
```

## Visual debugging inside a container
1) pdb debugger
- Set inside a container description in `docker-compose.yaml`
the following:

```
stdin_open: true
tty: true
```

- Attach to the docker-container in order to get the access to
the terminal:

```
docker attach <contaier name>
```

- Set a breakpoint inside the code:

```python
breakpoint()

```

2) Debugpy 
- Add the following lines to the `docker-compose.yaml` file

```
command: bash -c "pip3 install debugpy && python3 -m debugpy --listen 0.0.0.0:5678 manage.py runserver 0.0.0.0:8000"
ports:
  - 5678:5678
```

- Connect to the debugger using Python VScode extension

Attach to remote - enter localhost and 5678
