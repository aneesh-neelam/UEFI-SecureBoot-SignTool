# WARNING
# This spec file is still in progress, rpmbuild for this may not work correctly or at all at this time

Name:    sb-signtool
Version: 1.0
Release: 1%{?dist}
Group: System Environment/Kernel
Summary: Script to sign kernel modules and systemd service to run during boot.

URL: https://github.com/aneesh-neelam/UEFI-SecureBoot-SignTool
License: GPLv2+
Source0: https://github.com/aneesh-neelam/UEFI-SecureBoot-SignTool/releases/download/%{version}/%{name}-%{version}.tar.gz

Requires: kernel-devel
Requires: openssl
Requires: mokutil
Requires: bash

BuildArch: noarch

%description
UEFI Secure Boot Sign Tool can be used to sign kernel modules.
Essentially, it is a wrapper around the sign-file binary in the kernel sources.
The systemd service can be enabled to automatically sign specific kernel modules with user's own once setup is complete.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{name}-sign %{buildroot}/%{_bindir}/%{name}-sign


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}-sign


%changelog
* Tue Jul 11 2017 Aneesh Neelam <neelam.aneesh@gmail.com>
- Initial version of the package
