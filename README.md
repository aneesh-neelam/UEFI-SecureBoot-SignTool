# UEFI Secure Boot sign tool

The default signed Linux kernel on [Ubuntu](https://www.ubuntu.com/) (>=16.04.x), [Fedora](https://getfedora.org/) and perhaps on other distributions as well, won't load unsigned external kernel modules if Secure Boot is enabled on [UEFI](https://en.wikipedia.org/wiki/Unified_Extensible_Firmware_Interface) systems.
Hence, any external kernel modules like the proprietary [Nvidia kernel driver](https://www.nvidia.com/object/unix.html), [Oracle VM VirtualBox](https://www.virtualbox.org/)'s host/guest kernel driver etc. won't work.

External kernel modules must be signed for UEFI Secure Boot using a Machine Owner Key (MOK).
This is useful if you can't or don't wish to disable Secure Boot on your UEFI-enabled system.

UEFI Secure Boot Sign Tool can be used to sign kernel modules.
Essentially, it is a wrapper around the sign-file binary in the kernel sources.

The systemd service can be enabled to automatically sign specific kernel modules with user's own once setup is complete.

### Install and Setup

Fedora Dependencies:
* kernel-devel
* mokutil
* openssl
* Any text editor

Extract/Install the files in their respective locations. See

###### Generating a Public and Private X.509 Key Pair:

Generate a X.509 Key Pair as the UEFI Secure Boot Machine Owner Key.

    $ openssl req -new -x509 -newkey rsa:2048 -keyout "/etc/sb-signtool/keyfiles/sb.priv" -outform DER -out "/etc/sb-signtool/keyfiles/sb_pub.der" -nodes -days 36500 -subj "/CN=<your name>/"

###### Import Public Key into UEFI-enabled System:

    # mokutil --import "/etc/sb-signtool/sb_pub.der"

###### Edit the UEFI Secure Boot Sign Tool config file(s):

Must edit the following file before running script:

    /etc/sb-signtool/modules.conf

You can check out an example file in the [documentation](https://github.com/aneesh-neelam/UEFI-SecureBoot-SignTool/blob/master/usr/share/doc/sb-signtool/example_modules.conf).

### Manual execution and Enabling systemd service

Must run the Signing Tool every time a kernel module is rebuilt or when a new kernel is installed.
Or enable the systemd service to do that on boot.

###### Run the UEFI Secure Boot Signing Tool:

    # /usr/bin/sb-signtool-sign

###### Enable the systemd service:

    # systemctl enable sb-signtool.service


### TODO

* Packaging and distribution for Ubuntu, Fedora, Arch Linux etc.


## Contributing and License

Feel free to create GitHub Issues and issue Pull Requests to contribute to this project.

Code released under [GNU General Public License v2.0](https://github.com/aneesh-neelam/uefi-sb-signtool/blob/master/LICENSE).
