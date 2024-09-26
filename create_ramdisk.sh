#!/usr/bin/env bash
set -eu

ramfs_size_mb=1200
mount_point=/tmp/rdisk

mkramdisk() {
ramfs_size_sectors=$((${ramfs_size_mb}*1024*1024/512))
ramdisk_dev=`hdid -nomount ram://${ramfs_size_sectors}`
newfs_hfs -v 'ram disk' ${ramdisk_dev}
mkdir -p ${mount_point}
mount -o noatime -t hfs ${ramdisk_dev} ${mount_point}
echo "remove with:"
echo "umount ${mount_point}"
echo "diskutil eject ${ramdisk_dev}"
}


echo "Creating ram disk"
mkramdisk


# remove with:
# umount /tmp/rdisk
# diskutil eject /dev/disk4
