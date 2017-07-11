#!/usr/bin/env bash

VERSION="1.0"

wget https://github.com/aneesh-neelam/UEFI-SecureBoot-SignTool/releases/download/1.0/sb-signtool-1.0.tar.gz
tar -xzvf sb-signtool-1.0.tar.gz

mkdir -p /usr/bin
mkdir -p /usr/lib/systemd/system
mkdir -p /usr/share/doc/sb-signtool
mkdir -p /usr/etc/sb-signtool/keyfiles

install -m 755 sb-signtool-$VERSION/usr/bin/sb-signtool-sign /usr/bin/
install -m 644 sb-signtool-$VERSION/usr/lib/systemd/system/sb-signtool.service /usr/lib/systemd/system/
install -m 644 sb-signtool-$VERSION/etc/sb-signtool/modules.conf /etc/sb-signtool/
install -m 644 sb-signtool-$VERSION/etc/sb-signtool/mok.rc /etc/sb-signtool/
install -m 644 sb-signtool-$VERSION/usr/share/doc/sb-signtool/example_modules.conf /usr/share/doc/sb-signtool
install -m 644 sb-signtool-$VERSION/usr/share/doc/sb-signtool/README.md /usr/share/doc/sb-signtool
install -m 644 sb-signtool-$VERSION/usr/share/doc/sb-signtool/ /usr/share/doc/sb-signtool

rm -r sb-signtool-$VERSION
rm sb-signtool-1.0.tar.gz
