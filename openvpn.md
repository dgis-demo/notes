## Start a session
```shell
openvpn3 session-start --config ${MY_CONFIGURATION_FILE}
```

## Stop a session
```shell
openvpn3 session-manage --session-path /net/openvpn/v3/sessions/..... --disconnect
```

## Installation
Replase `$DISTRO` with an Ubuntu distributive name like `focal` (Ubuntu 20.04) and run the following commands:
```shell
sudo apt install apt-transport-https
sudo wget https://swupdate.openvpn.net/repos/openvpn-repo-pkg-key.pub
sudo apt-key add openvpn-repo-pkg-key.pub

sudo wget -O /etc/apt/sources.list.d/openvpn3.list https://swupdate.openvpn.net/community/openvpn3/repos/openvpn3-$DISTRO.list
sudo apt update
sudo apt install openvpn3
```
