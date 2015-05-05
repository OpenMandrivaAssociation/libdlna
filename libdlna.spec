%define name libdlna
%define version 0.2.4
%define release 1.2

%define major   0
%define libname %mklibname dlna %major
%define develname %mklibname -d dlna

Summary: Implementation of DLNA (Digital Living Network Alliance)
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://libdlna.geexbox.org/releases/%{name}-%{version}.tar.bz2
License: LGPLv2+
Group: System/Libraries
Url: http://libdlna.geexbox.org/
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

%build
%setup_compile_flags
./configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-static --enable-shared
make

%install
%makeinstall_std


%files -n %{libname}
%doc AUTHORS COPYING ChangeLog README 
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*pc



%changelog
* Tue Apr 03 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.2.4-1
+ Revision: 788989
- patch removed
- version update 0.2.4

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-6mdv2011.0
+ Revision: 620115
- the mass rebuild of 2010.0 packages

* Sat Sep 12 2009 Thierry Vignaud <tv@mandriva.org> 0.2.3-5mdv2010.0
+ Revision: 438550
- rebuild

* Mon Oct 20 2008 Funda Wang <fwang@mandriva.org> 0.2.3-4mdv2009.1
+ Revision: 295484
- adopt to new ffmpeg file location
- use compile flags
- clearify license

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.2.3-2mdv2008.1
+ Revision: 170947
- rebuild

* Sat Jan 26 2008 Erwan Velu <erwan@mandriva.org> 0.2.3-1mdv2008.1
+ Revision: 158277
- import libdlna

