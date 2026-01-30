Name:       libmdbx
Version:    0.13.11
Release:    %autorelease
Summary:    An amazingly fast key-value database library
License:    Apache-2.0
URL:        https://libmdbx.dqdkfa.ru
VCS:	    git:https://sourcecraft.dev/dqdkfa/libmdbx.git
Source0:    %{url}/release/%{name}-amalgamated-%{version}.tar.xz
Patch:      libmdbx-0001-Set-soversion.patch
BuildRequires: binutils
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++

%description
MDBX is an extremely fast, compact, powerful, embedded, transactional key-value
store database, with permissive license. MDBX has a specific set of properties
and capabilities, focused on creating unique lightweight solutions with
extraordinary performance.

%package    devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package    utils
Summary:    Utilities for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description    utils
The %{name}-utils package contains utilities for maintaining %{name} data files.

%prep
%autosetup -c

%build
%cmake -DMDBX_BUILD_TIMESTAMP:STRING=unknown .
%cmake_build --config Release

%install
%cmake_install --config Release

%files
%license LICENSE
%doc README.md ChangeLog.md
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/*
%{_libdir}/%{name}.so

%files utils
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
