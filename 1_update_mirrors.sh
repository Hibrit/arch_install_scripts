#!/bin/bash

#* clear screen
clear

#* setting time
timedatectl set-ntp true &> /dev/null

#? first check for wget
sudo pacman -Sy --noconfirm --needed wget

#* set the proper pacman configuration
rm /etc/pacman.conf
wget --directory-prefix /etc/ https://raw.githubusercontent.com/Hibrit/archlinuxsettings/master/pacman/pacman.conf
pacman -Syy


#! for this create a interactial sequence and a automated one !
#* listing partitions
lsblk
echo
lsblk -f

echo
echo

#* printing what to do
echo "get done with the cfdisk /dev/DEVICE and done mounting to /mnt"
echo
