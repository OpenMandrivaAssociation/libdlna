%define major   0
%define libname %mklibname dlna %{major}
%define devname %mklibname dlna -d

Summary:	Implementation of DLNA (Digital Living Network Alliance)
Name:		libdlna
Version:	0.2.4
Release:	4
License:	LGPLv2.1+
Group:		System/Libraries
Url:		http://libdlna.geexbox.org/
Source0:	http://libdlna.geexbox.org/releases/%{name}-%{version}.tar.bz2
Patch0:		libdlna-0.2.4-ffmpeg-2.4.patch
BuildRequires:	ffmpeg-devel >= 2.5.4

%description
libdlna aims at being the reference open-source implementation of DLNA
(Digital Living Network Alliance) standards.

Its primary goal is to provide DLNA support to uShare, an embedded DLNA & 
UPnP A/V Media Server, but it will be used to build both DLNA servers
and players in the long term.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries

%description -n %{libname}
Dynamic libraries from %{name}.

%files -n %{libname}
%doc AUTHORS COPYING ChangeLog README 
%{_libdir}/libdlna.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Libraries and includes files for developing programs based on %{name}.

%files -n %{devname}
%{_includedir}/dlna.h
%{_libdir}/libdlna.so
%{_libdir}/libdlna.a
%{_libdir}/pkgconfig/libdlna.pc

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%setup_compile_flags
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--enable-static \
	--enable-shared
make

%install
%makeinstall_std

