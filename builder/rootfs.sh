#! /bin/bash

sudo apt-get update && sudo apt-get upgrade -y

sudo apt-get install qemu qemu-user-static binfmt-support -y


mkdir ~/rootfs


export JETSON_ROOTFS_DIR=~/rootfs

sudo -E ./create-rootfs.sh

chmod -R 777 ~/rootfs

cp /usr/bin/qemu-aarch64-static usr/bin

sudo mount --bind /dev dev/
sudo mount --bind /sys sys/
sudo mount --bind /proc proc/
sudo mount --bind /dev/pts dev/pts

chroot . ~/owls_drone/builder/update_iso.sh

chroot . ~/owls_drone/builder/user_add.sh

