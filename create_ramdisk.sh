#!/usr/bin/env bash
set -eu


echo "Creating ram disk"

# size is (# megabytes * 2048), so for 1 Gb (1024 Mb), we use 1024 * 2048 = 2097152
#
diskutil erasevolume HFS+ "ml_disk" `hdiutil attach -nomount ram://2097152`

echo "To delete the ram disk, type 'umount ml_disk'"
