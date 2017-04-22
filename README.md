# UEFI Secure Boot sign tool

The Linux kernel on Ubuntu (>=16.04.x), Fedora (>=18) won't load unsigned external kernel modules if Secure Boot is enabled on UEFI systems.
Hence, any external kernel modules like the Nvidia Proprietary kernel driver, VirtualBox kernel driver etc. won't work.

External kernel modules must be signed for UEFI Secure Boot using a Machine Owner Key (MOK).

UEFI Secure Boot Sign Tool is a set of scripts that you can use to sign kernel modules.
This is useful if you can't or don't wish to disable Secure Boot on your UEFI-enabled system.

Here we use a X.509 Key Pair as the UEFI Secure Boot Machine Owner Key.

### Usage

You'll have to run the Signing Tool every time a kernel module is rebuilt or when a new kernel is installed.

Maybe in the future this tool could hook into [DKMS](https://github.com/dell/dkms) whenever a new kernel or kernel module is installed to automate this process completely.

###### Generating a Public and Private X.509 Key Pair:

    $ openssl req -new -x509 -newkey rsa:2048 -keyout "<private key filepath>" -outform DER -out "<public key filepath>" -nodes -days 36500 -subj "/CN=<your name>/"

###### Import Public Key into UEFI-enabled System:

    # mokutil --import "<public key filepath>"

###### Edit the UEFI Secure Boot Sign Tool config files:

You can check out example config files in the [examples directory](https://github.com/aneesh-neelam/uefi-sb-signtool/tree/master/examples).

    /etc/sb-signtool/mok.rc
    /etc/sb-signtool/modules.conf

###### Run the UEFI Secure Boot Signing Tool:

    # /usr/local/bin/sb-signtool-sign

## Contributing and License

Feel free to create GitHub Issues and issue Pull Requests to contribute to this project.

Code released under [BSD 3-Clause License](https://github.com/aneesh-neelam/uefi-sb-signtool/blob/master/LICENSE).
