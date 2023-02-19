#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kapidox
Version  : 5.103.0
Release  : 93
URL      : https://download.kde.org/stable/frameworks/5.103/kapidox-5.103.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.103/kapidox-5.103.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.103/kapidox-5.103.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 LGPL-3.0 MIT
Requires: kapidox-bin = %{version}-%{release}
Requires: kapidox-license = %{version}-%{release}
Requires: kapidox-man = %{version}-%{release}
Requires: kapidox-python = %{version}-%{release}
Requires: kapidox-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-kde
BuildRequires : pypi(jinja2)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(requests)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
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
Requires: pypi(jinja2)
Requires: pypi(pyyaml)
Requires: pypi(requests)

%description python3
python3 components for the kapidox package.


%prep
%setup -q -n kapidox-5.103.0
cd %{_builddir}/kapidox-5.103.0
%patch1 -p1
pushd ..
cp -a kapidox-5.103.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676833377
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kapidox
cp %{_builddir}/kapidox-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kapidox/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e || :
cp %{_builddir}/kapidox-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kapidox/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kapidox-%{version}/LICENSES/LGPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/kapidox/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kapidox-%{version}/kapidox/data/htmlresource/3rd-party/jquery/LICENSE.txt %{buildroot}/usr/share/package-licenses/kapidox/1238983d71130d0d96aad2acc946818007c77734 || :
cp %{_builddir}/kapidox-%{version}/kapidox/data/htmlresource/icons/api-kde-org@1x.png.license %{buildroot}/usr/share/package-licenses/kapidox/3130f127d410d33b06d00cf5ee0a28a921eb7f44 || :
cp %{_builddir}/kapidox-%{version}/kapidox/data/htmlresource/icons/api-kde-org@2x.png.license %{buildroot}/usr/share/package-licenses/kapidox/3130f127d410d33b06d00cf5ee0a28a921eb7f44 || :
cp %{_builddir}/kapidox-%{version}/kapidox/data/htmlresource/icons/api-kde-org@3x.png.license %{buildroot}/usr/share/package-licenses/kapidox/3130f127d410d33b06d00cf5ee0a28a921eb7f44 || :
cp %{_builddir}/kapidox-%{version}/kapidox/data/htmlresource/icons/api-kde-org@4x.png.license %{buildroot}/usr/share/package-licenses/kapidox/3130f127d410d33b06d00cf5ee0a28a921eb7f44 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
## install_append content
dest=%{buildroot}/usr/share/man/man1
mkdir -p $dest
cp -a ./docs/*.1 $dest/
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/depdiagram_generate_all
/usr/bin/kapidox-depdiagram-generate
/usr/bin/kapidox-depdiagram-prepare
/usr/bin/kapidox-generate

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kapidox/1238983d71130d0d96aad2acc946818007c77734
/usr/share/package-licenses/kapidox/3130f127d410d33b06d00cf5ee0a28a921eb7f44
/usr/share/package-licenses/kapidox/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
/usr/share/package-licenses/kapidox/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kapidox/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0

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
