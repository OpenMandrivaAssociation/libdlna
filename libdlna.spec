%define name libdlna
%define version 0.2.3 
%define release %mkrel 5

%define major   0
%define libname %mklibname dlna %major
%define develname %mklibname -d dlna

Summary: Implementation of DLNA (Digital Living Network Alliance)
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch0: libdlna-0.2.3-newffmpeg.patch
License: LGPLv2+
Group: System/Libraries
Url: http://libdlna.geexbox.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: ffmpeg-devel

%description
libdlna aims at being the reference open-source implementation of DLNA
(Digital Living Network Alliance) standards.
Its primary goal is to provide DLNA support to uShare, an embedded DLNA & 
UPnP A/V Media Server, but it will be used to build both DLNA servers
and players in the long term.

%package -n     %{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries

%description -n %{libname}
Dynamic libraries from %name.

%package -n     %{develname}
Summary:        Header files and static libraries from %name
Group:          Development/C
Requires:       %{libname} >= %{version}
Provides:       %{name}-devel = %{version}-%{release}
Obsoletes:      %name-devel < %{version}-%{release}
Obsoletes:	%{_lib}dlna0-devel

%description -n %{develname}
Libraries and includes files for developing programs based on %name.

%prep
%setup -q
%patch0 -p0

%build
%setup_compile_flags
./configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-static --enable-shared
make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README 
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*pc

