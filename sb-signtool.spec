%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

Name:    sb-signtool
Version: 1.0
Release: 1.0%{?dist}
Group: System Environment/Kernel
Summary: Script to sign kernel modules and systemd service to run during boot.
URL: https://github.com/aneesh-neelam/UEFI-SecureBoot-SignTool
License: BSD
Source0: %{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
%{summary}

%prep
%setup -q

%build
# Empty section.

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}

# in builddir
cp -a * %{buildroot}
