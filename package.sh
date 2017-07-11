#!/usr/bin/env bash

VERSION="1.0"

mkdir sb-signtool-$VERSION
mkdir -p sb-signtool-$VERSION/usr/bin
mkdir -p sb-signtool-$VERSION/usr/lib/systemd/system
mkdir -p sb-signtool-$VERSION/usr/share/doc/sb-signtool
mkdir -p sb-signtool-$VERSION/etc/sb-signtool/keyfiles

install -m 755 usr/bin/sb-signtool-sign sb-signtool-$VERSION/usr/bin/
install -m 644 usr/lib/systemd/system/sb-signtool.service sb-signtool-$VERSION/usr/lib/systemd/system/
install -m 644 etc/sb-signtool/modules.conf sb-signtool-$VERSION/etc/sb-signtool/
install -m 644 etc/sb-signtool/mok.rc sb-signtool-$VERSION/etc/sb-signtool/
install -m 644 usr/share/doc/sb-signtool/example_modules.conf sb-signtool-$VERSION/usr/share/doc/sb-signtool/

tar -zcvf sb-signtool-1.0.tar.gz sb-signtool-1.0/

rm -r sb-signtool-$VERSION
