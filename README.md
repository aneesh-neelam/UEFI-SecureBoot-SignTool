# UEFI Secure Boot sign tool

The default signed Linux kernel on [Ubuntu](https://www.ubuntu.com/) (>=16.04.x), [Fedora](https://getfedora.org/) (>=18) and perhaps on other distributions as well, won't load unsigned external kernel modules if Secure Boot is enabled on [UEFI](https://en.wikipedia.org/wiki/Unified_Extensible_Firmware_Interface) systems.
Hence, any external kernel modules like the proprietary [Nvidia kernel driver](https://www.nvidia.com/object/unix.html), [Oracle VM VirtualBox](https://www.virtualbox.org/)'s host/guest kernel driver etc. won't work.

External kernel modules must be signed for UEFI Secure Boot using a Machine Owner Key (MOK).

You can use the UEFI Secure Boot Sign Tool to sign kernel modules.
This is useful if you can't or don't wish to disable Secure Boot on your UEFI-enabled system.

### Usage

Here, we use a X.509 Key Pair as the UEFI Secure Boot Machine Owner Key.

You'll have to run the Signing Tool every time a kernel module is rebuilt or when a new kernel is installed.

Maybe in the future this tool could hook into [DKMS](https://github.com/dell/dkms) whenever a new kernel or kernel module is installed to completely automate this process.

###### Generating a Public and Private X.509 Key Pair:

    $ openssl req -new -x509 -newkey rsa:2048 -keyout "<private key filepath>" -outform DER -out "<public key filepath>" -nodes -days 36500 -subj "/CN=<your name>/"

###### Import Public Key into UEFI-enabled System:

    # mokutil --import "<public key filepath>"

###### Edit the UEFI Secure Boot Sign Tool config files:

You can check out example config files in the [examples directory](https://github.com/aneesh-neelam/uefi-sb-signtool/tree/master/examples).

    /usr/local/etc/sb-signtool/mok.rc
    /usr/local/etc/sb-signtool/modules.conf

###### Run the UEFI Secure Boot Signing Tool:

    # /usr/local/bin/sb-signtool-sign

## Contributing and License

Feel free to create GitHub Issues and issue Pull Requests to contribute to this project.

Code released under [BSD 3-Clause License](https://github.com/aneesh-neelam/uefi-sb-signtool/blob/master/LICENSE).
