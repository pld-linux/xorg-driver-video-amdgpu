#
# Conditional build:
%bcond_without	glamor		# glamor, new GL-based acceleration
#
%define	libdrm_ver	2.4.89
Summary:	X.org video driver for AMD Radeon GPUs
Summary(pl.UTF-8):	Sterowniki obrazu X.org do układów graficznych AMD Radeon
Name:		xorg-driver-video-amdgpu
Version:	22.0.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-video-amdgpu-%{version}.tar.xz
# Source0-md5:	6c907b44d32a0112e1a4788bab727f79
URL:		https://xorg.freedesktop.org/
BuildRequires:	Mesa-libgbm-devel
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libdrm-devel >= %{libdrm_ver}
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-devel
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.1
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.13
%{?with_glamor:BuildRequires:	xorg-xserver-server-devel >= 1.16.0}
BuildRequires:	xz
%{?requires_xorg_xserver_videodrv}
Requires:	libdrm >= %{libdrm_ver}
Requires:	xorg-xserver-libdri >= 1.13
Requires:	xorg-xserver-libglx >= 1.13
Requires:	xorg-xserver-server >= 1.13
%{?with_glamor:Requires:	xorg-xserver-server >= 1.16.0}
Provides:	xorg-driver-video
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
amdgpu is an Xorg video driver for AMD RADEON-based video cards with
the following features:
- support for 8-, 15-, 16-, 24- and 32-bit pixel depth,
- RandR support up to version 1.4,
- 3D acceleration.

This driver supports SI and newer families' video cards.

%description
amdgpu to sterownik obraz uXorg dla kart graficznych opartych na
układach AMD RADEON. Ma następujące możliwości:
- obsługa 8, 15, 16, 24, 30-bitowej głębi kolorów,
- obsługa RandR do wersji 1.4,
- akceleracja 3D.

Obsługuje karty graficzne z rodziny SI i nowszych.

%prep
%setup -q -n xf86-video-amdgpu-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_glamor:--disable-glamor}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/amdgpu_drv.so
%{_datadir}/X11/xorg.conf.d/10-amdgpu.conf
%{_mandir}/man4/amdgpu.4*
