#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-pcov
Version  : 1.0.6
Release  : 6
URL      : https://pecl.php.net//get/pcov-1.0.6.tgz
Source0  : https://pecl.php.net//get/pcov-1.0.6.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
Requires: php-pcov-lib = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : pcre2-dev

%description
PCOV
====
[![Build Status](https://travis-ci.org/krakjoe/pcov.svg?branch=develop)](https://travis-ci.org/krakjoe/pcov)
[![Build status](https://ci.appveyor.com/api/projects/status/w265n0w7yk6o3y6m?svg=true)](https://ci.appveyor.com/project/krakjoe/pcov)

%package lib
Summary: lib components for the php-pcov package.
Group: Libraries

%description lib
lib components for the php-pcov package.


%prep
%setup -q -n pcov-1.0.6
cd %{_builddir}/pcov-1.0.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20190902/pcov.so
