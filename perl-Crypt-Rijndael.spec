#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Crypt-Rijndael
Version  : 1.13
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/L/LE/LEONT/Crypt-Rijndael-1.13.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/L/LE/LEONT/Crypt-Rijndael-1.13.tar.gz
Summary  : 'Crypt::CBC compliant Rijndael encryption module'
Group    : Development/Tools
License  : LGPL-3.0
Requires: perl-Crypt-Rijndael-lib = %{version}-%{release}
Requires: perl-Crypt-Rijndael-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Crypt::Rijndael - Crypt::CBC compliant Rijndael encryption module
VERSION
Version 1.13

%package dev
Summary: dev components for the perl-Crypt-Rijndael package.
Group: Development
Requires: perl-Crypt-Rijndael-lib = %{version}-%{release}
Provides: perl-Crypt-Rijndael-devel = %{version}-%{release}

%description dev
dev components for the perl-Crypt-Rijndael package.


%package lib
Summary: lib components for the perl-Crypt-Rijndael package.
Group: Libraries
Requires: perl-Crypt-Rijndael-license = %{version}-%{release}

%description lib
lib components for the perl-Crypt-Rijndael package.


%package license
Summary: license components for the perl-Crypt-Rijndael package.
Group: Default

%description license
license components for the perl-Crypt-Rijndael package.


%prep
%setup -q -n Crypt-Rijndael-1.13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Crypt-Rijndael
cp COPYING %{buildroot}/usr/share/package-licenses/perl-Crypt-Rijndael/COPYING
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/x86_64-linux-thread-multi/Crypt/Rijndael.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Crypt::Rijndael.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/x86_64-linux-thread-multi/auto/Crypt/Rijndael/Rijndael.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Crypt-Rijndael/COPYING
