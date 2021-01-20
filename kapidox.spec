#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kapidox
Version  : 5.78.0
Release  : 54
URL      : https://download.kde.org/stable/frameworks/5.78/kapidox-5.78.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.78/kapidox-5.78.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.78/kapidox-5.78.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 MIT
Requires: kapidox-bin = %{version}-%{release}
Requires: kapidox-license = %{version}-%{release}
Requires: kapidox-man = %{version}-%{release}
Requires: kapidox-python = %{version}-%{release}
Requires: kapidox-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-kde
BuildRequires : python3
Patch1: 0001-Remove-optional-dependencies.patch

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
%setup -q -n kapidox-5.78.0
cd %{_builddir}/kapidox-5.78.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1611181157
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1611181157
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kapidox
cp %{_builddir}/kapidox-5.78.0/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kapidox/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
cp %{_builddir}/kapidox-5.78.0/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kapidox/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/kapidox-5.78.0/src/kapidox/data/htmlresource/3rd-party/jquery/LICENSE.txt %{buildroot}/usr/share/package-licenses/kapidox/1238983d71130d0d96aad2acc946818007c77734
cp %{_builddir}/kapidox-5.78.0/src/kapidox/data/htmlresource/ako.webmanifest.license %{buildroot}/usr/share/package-licenses/kapidox/8c29bbabd9e5f8751e29519f8913d4a8e3cf2146
cp %{_builddir}/kapidox-5.78.0/src/kapidox/data/htmlresource/icons/api-kde-org@1x.png.license %{buildroot}/usr/share/package-licenses/kapidox/3130f127d410d33b06d00cf5ee0a28a921eb7f44
cp %{_builddir}/kapidox-5.78.0/src/kapidox/data/htmlresource/icons/api-kde-org@2x.png.license %{buildroot}/usr/share/package-licenses/kapidox/3130f127d410d33b06d00cf5ee0a28a921eb7f44
cp %{_builddir}/kapidox-5.78.0/src/kapidox/data/htmlresource/icons/api-kde-org@3x.png.license %{buildroot}/usr/share/package-licenses/kapidox/3130f127d410d33b06d00cf5ee0a28a921eb7f44
cp %{_builddir}/kapidox-5.78.0/src/kapidox/data/htmlresource/icons/api-kde-org@4x.png.license %{buildroot}/usr/share/package-licenses/kapidox/3130f127d410d33b06d00cf5ee0a28a921eb7f44
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
/usr/share/package-licenses/kapidox/3130f127d410d33b06d00cf5ee0a28a921eb7f44
/usr/share/package-licenses/kapidox/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
/usr/share/package-licenses/kapidox/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kapidox/8c29bbabd9e5f8751e29519f8913d4a8e3cf2146

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
