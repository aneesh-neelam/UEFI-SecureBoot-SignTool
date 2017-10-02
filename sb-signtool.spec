# WARNING
# This spec file is still in progress, rpmbuild for this may not work correctly or at all at this time

Name:    sb-signtool
Version: 1.0
Release: 2%{?dist}
Group: System/Kernel and hardware
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
%autosetup 

%build

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_docdir}/sb-signtool
mkdir -p %{buildroot}/usr/lib/systemd/system
mkdir -p %{buildroot}/%{_sysconfdir}/sb-signtool/keyfiles

install -m 644 usr/bin/sb-signtool-sign %{buildroot}/usr/bin/
install -m 644 etc/sb-signtool/modules.conf %{buildroot}/%{_sysconfdir}/sb-signtool/
install -m 644 etc/sb-signtool/mok.rc %{buildroot}/%{_sysconfdir}/sb-signtool/
install -m 644 usr/share/doc/sb-signtool/example_modules.conf %{buildroot}/usr/share/doc/sb-signtool/
install -m 644 usr/lib/systemd/system/sb-signtool.service %{buildroot}/usr/lib/systemd/system/
chmod a+x %{buildroot}/usr/bin/sb-signtool-sign
touch %{buildroot}/%{_sysconfdir}/sb-signtool/keyfiles/sb.priv
touch %{buildroot}/%{_sysconfdir}/sb-signtool/keyfiles/sb_pub.der

%post
%systemd_post sb-signtool.service

%preun
%systemd_preun sb-signtool.service

%postun
%systemd_postun_with_restart sb-signtool.service


%files
%license usr/share/doc/sb-signtool/LICENSE
%doc usr/share/doc/sb-signtool/README.md
%{_bindir}/%{name}-sign
%{_docdir}/sb-signtool/
%config(noreplace) %{_sysconfdir}/sb-signtool/modules.conf
%config(noreplace) %{_sysconfdir}/sb-signtool/mok.rc
%config(noreplace) %{_sysconfdir}/sb-signtool/keyfiles/sb.priv
%config(noreplace) %{_sysconfdir}/sb-signtool/keyfiles/sb_pub.der
/usr/lib/systemd/system/sb-signtool.service


%changelog

* Sat Sep 30 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.0-2
- Config changes 
- Upstream

* Tue Jul 11 2017 Aneesh Neelam <neelam.aneesh@gmail.com>
- Initial version of the package
