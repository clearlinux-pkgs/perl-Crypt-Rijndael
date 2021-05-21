#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Crypt-Rijndael
Version  : 1.16
Release  : 20
URL      : https://cpan.metacpan.org/authors/id/L/LE/LEONT/Crypt-Rijndael-1.16.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/L/LE/LEONT/Crypt-Rijndael-1.16.tar.gz
Summary  : 'Crypt::CBC compliant Rijndael encryption module'
Group    : Development/Tools
License  : LGPL-3.0
Requires: perl-Crypt-Rijndael-license = %{version}-%{release}
Requires: perl-Crypt-Rijndael-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Crypt::Rijndael - Crypt::CBC compliant Rijndael encryption module
VERSION
Version 1.16

%package dev
Summary: dev components for the perl-Crypt-Rijndael package.
Group: Development
Provides: perl-Crypt-Rijndael-devel = %{version}-%{release}
Requires: perl-Crypt-Rijndael = %{version}-%{release}

%description dev
dev components for the perl-Crypt-Rijndael package.


%package license
Summary: license components for the perl-Crypt-Rijndael package.
Group: Default

%description license
license components for the perl-Crypt-Rijndael package.


%package perl
Summary: perl components for the perl-Crypt-Rijndael package.
Group: Default
Requires: perl-Crypt-Rijndael = %{version}-%{release}

%description perl
perl components for the perl-Crypt-Rijndael package.


%prep
%setup -q -n Crypt-Rijndael-1.16
cd %{_builddir}/Crypt-Rijndael-1.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Crypt-Rijndael
cp %{_builddir}/Crypt-Rijndael-1.16/COPYING %{buildroot}/usr/share/package-licenses/perl-Crypt-Rijndael/f45ee1c765646813b442ca58de72e20a64a7ddba
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Crypt::Rijndael.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Crypt-Rijndael/f45ee1c765646813b442ca58de72e20a64a7ddba

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Crypt/Rijndael.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Crypt/Rijndael/Rijndael.so
