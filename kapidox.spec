#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kapidox
Version  : 5.68.0
Release  : 36
URL      : https://download.kde.org/stable/frameworks/5.68/kapidox-5.68.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.68/kapidox-5.68.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.68/kapidox-5.68.0.tar.xz.sig
Summary  : Frameworks API Documentation Tools
Group    : Development/Tools
License  : BSD-2-Clause MIT
Requires: kapidox-bin = %{version}-%{release}
Requires: kapidox-license = %{version}-%{release}
Requires: kapidox-man = %{version}-%{release}
Requires: kapidox-python = %{version}-%{release}
Requires: kapidox-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-kde
BuildRequires : python3

%description
# KDE Doxygen Tools
## Introduction
This framework contains scripts and data for building API documentation (dox) in
a standard format and style.

%package bin
Summary: bin components for the kapidox package.
Group: Binaries
Requires: kapidox-license = %{version}-%{release}

%description bin
bin components for the kapidox package.


%package license
Summary: license components for the kapidox package.
Group: Default

%description license
license components for the kapidox package.


%package man
Summary: man components for the kapidox package.
Group: Default

%description man
man components for the kapidox package.


%package python
Summary: python components for the kapidox package.
Group: Default
Requires: kapidox-python3 = %{version}-%{release}

%description python
python components for the kapidox package.


%package python3
Summary: python3 components for the kapidox package.
Group: Default
Requires: python3-core

%description python3
python3 components for the kapidox package.


%prep
%setup -q -n kapidox-5.68.0
cd %{_builddir}/kapidox-5.68.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1584295872
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1584295872
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kapidox
cp %{_builddir}/kapidox-5.68.0/LICENSE %{buildroot}/usr/share/package-licenses/kapidox/4f348e8e16c398ae808b12f1f31c8f32041f80fc
cp %{_builddir}/kapidox-5.68.0/src/kapidox/data/htmlresource/3rd-party/bootstrap/LICENSE.txt %{buildroot}/usr/share/package-licenses/kapidox/26d8bcc8dbe50e51ae48a8124935dc704d01add2
cp %{_builddir}/kapidox-5.68.0/src/kapidox/data/htmlresource/3rd-party/jquery/LICENSE.txt %{buildroot}/usr/share/package-licenses/kapidox/1238983d71130d0d96aad2acc946818007c77734
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/depdiagram-generate
/usr/bin/depdiagram-generate-all
/usr/bin/depdiagram-prepare
/usr/bin/kapidox_generate

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kapidox/1238983d71130d0d96aad2acc946818007c77734
/usr/share/package-licenses/kapidox/26d8bcc8dbe50e51ae48a8124935dc704d01add2
/usr/share/package-licenses/kapidox/4f348e8e16c398ae808b12f1f31c8f32041f80fc

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/depdiagram-generate-all.1
/usr/share/man/man1/depdiagram-generate.1
/usr/share/man/man1/depdiagram-prepare.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
