# Server commands

## Permissions

```console
sudo chown qbtuser:qbtuser /mnt/hdd/audiobooks -R
sudo chown qbtuser:qbtuser /mnt/hdd -R
sudo chown qbtuser:qbtuser /mnt/hdd/tv -R
sudo chown qbtuser:qbtuser /mnt/hdd/movies -R
sudo chmod ugo+rwx /mnt/hdd/
sudo chown pi /mnt/hdd/ -R
```

## Plex

```console
sudo service plexmediaserver restart
```

## Drives

```console
sudo umount /dev/sda1
sudo mount /dev/sdb1 /mnt/hdd/tv
sudo mount /dev/sda1 /mnt/hdd/movies
sudo mount /dev/sdb1 /mnt/hdd/tv && sudo mount /dev/sda1 /mnt/hdd/movies
```

## qBittorent

```console
sudo systemctl start qbittorrent
sudo systemctl restart qbittorrent
```

## Webserver

```console
poetry --project=/home/pi/code/philbell.uk run deploy_prod
poetry --project=/home/pi/code/philbell.uk run start_prod
sudo /etc/init.d/nginx restart
```
