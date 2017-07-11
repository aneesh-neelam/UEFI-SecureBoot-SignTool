Name:    sb-signtool
Version: 1.0
Release: 1%{?dist}
Group: System Environment/Kernel
Summary: Script to sign kernel modules and systemd service to run during boot.

URL: https://github.com/aneesh-neelam/UEFI-SecureBoot-SignTool
License: GPLv2
Source0: %{name}-%{version}.tar.gz

# BuildRequires:
# Requires:

%description
%{summary}

%prep
%autosetup


%build
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license LICENSE
#%doc README.md



%changelog
* Tue Jul 11 2017 Aneesh Neelam <neelam.aneesh@gmail.com>
- Initial version of the package
