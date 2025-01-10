#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
# autospec version: v21
# autospec commit: f4a13a5
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : kapidox
Version  : 6.10.0
Release  : 127
URL      : https://download.kde.org/stable/frameworks/6.10/kapidox-6.10.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.10/kapidox-6.10.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.10/kapidox-6.10.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 LGPL-3.0 MIT
Requires: kapidox-bin = %{version}-%{release}
Requires: kapidox-license = %{version}-%{release}
Requires: kapidox-man = %{version}-%{release}
Requires: kapidox-python = %{version}-%{release}
Requires: kapidox-python3 = %{version}-%{release}
Requires: pypi(doxypypy)
Requires: pypi(doxyqml)
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-kde
BuildRequires : gnupg
BuildRequires : pypi(jinja2)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(requests)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
Requires: pypi(doxypypy)
Requires: pypi(doxyqml)
Requires: pypi(jinja2)
Requires: pypi(pyyaml)
Requires: pypi(requests)

%description python3
python3 components for the kapidox package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n kapidox-6.10.0
cd %{_builddir}/kapidox-6.10.0
pushd ..
cp -a kapidox-6.10.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1736536403
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 setup.py build

popd
%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
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
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
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
