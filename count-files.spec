Name:       count-files
Version:    1.0
Release:    1
Summary:    Script to count files in etc
License:    MIT
Source0:    count-files-1.0.tar.gz
BuildArch:  noarch

%description
A script from Lab 2 that counts files in /etc directory.

%prep
%setup -q

%install
mkdir -p %{buildroot}/usr/local/bin
install -m 755 count_files.sh %{buildroot}/usr/local/bin/count_files.sh

%files
/usr/local/bin/count_files.sh
