#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kapidox
Version  : 5.49.0
Release  : 1
URL      : https://download.kde.org/stable/frameworks/5.49/kapidox-5.49.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.49/kapidox-5.49.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.49/kapidox-5.49.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: kapidox-bin
Requires: kapidox-python3
Requires: kapidox-license
Requires: kapidox-man
Requires: kapidox-python
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
Requires: kapidox-license
Requires: kapidox-man

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
Requires: kapidox-python3

%description python
python components for the kapidox package.


%package python3
Summary: python3 components for the kapidox package.
Group: Default
Requires: python3-core

%description python3
python3 components for the kapidox package.


%prep
%setup -q -n kapidox-5.49.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535142610
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1535142610
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/kapidox
cp src/kapidox/data/htmlresource/3rd-party/jquery/LICENSE.txt %{buildroot}/usr/share/doc/kapidox/src_kapidox_data_htmlresource_3rd-party_jquery_LICENSE.txt
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
%defattr(-,root,root,-)
/usr/share/doc/kapidox/src_kapidox_data_htmlresource_3rd-party_jquery_LICENSE.txt

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/depdiagram-generate-all.1
/usr/share/man/man1/depdiagram-generate.1
/usr/share/man/man1/depdiagram-prepare.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
