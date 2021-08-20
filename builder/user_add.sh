


adduser --disabled-password --gecos "" owls

echo "owls:qweqwe2" | chpasswd
echo "root:qweqwe2" | chpasswd

usermod -aG sudo owls


cat <<EOF > /etc/sudoers
root    ALL=(ALL:ALL) NOPASSWD: ALL

owls    ALL=(ALL) NOPASSWD: ALL
EOF

cat <<EOF > /etc/hosts
127.0.0.1       ubuntu
EOF