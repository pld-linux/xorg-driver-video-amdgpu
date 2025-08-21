#
# Conditional build:
%bcond_without	glamor		# glamor, new GL-based acceleration
#
%define	libdrm_ver	2.4.121
Summary:	X.org video driver for AMD Radeon GPUs
Summary(pl.UTF-8):	Sterowniki obrazu X.org do układów graficznych AMD Radeon
Name:		xorg-driver-video-amdgpu
Version:	25.0.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-video-amdgpu-%{version}.tar.xz
# Source0-md5:	0aaf63c28cdd7a198d7273cc683c73ed
URL:		https://xorg.freedesktop.org/
BuildRequires:	Mesa-libgbm-devel
BuildRequires:	OpenGL-devel
BuildRequires:	libdrm-devel >= %{libdrm_ver}
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 2.042
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
BuildRequires:	xorg-xserver-server-devel >= 1.18
BuildRequires:	xz
%{?requires_xorg_xserver_videodrv}
Requires:	libdrm >= %{libdrm_ver}
Requires:	xorg-xserver-libdri >= 1.18
Requires:	xorg-xserver-libglx >= 1.18
Requires:	xorg-xserver-server >= 1.18
Provides:	xorg-driver-video
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
amdgpu is an Xorg video driver for AMD RADEON-based video cards with
the following features:
- support for 8-, 15-, 16-, 24- and 32-bit pixel depth,
- RandR support up to version 1.4,
- 3D acceleration.

This driver supports SI and newer families' video cards.

%description -l pl.UTF-8
amdgpu to sterownik obrazu Xorg dla kart graficznych opartych na
układach AMD RADEON. Ma następujące możliwości:
- obsługa 8, 15, 16, 24, 30-bitowej głębi kolorów,
- obsługa RandR do wersji 1.4,
- akceleracja 3D.

Obsługuje karty graficzne z rodziny SI i nowszych.

%prep
%setup -q -n xf86-video-amdgpu-%{version}

%build
%meson \
	-Dglamor=%{__enabled_disabled glamor} \
	-Dudev=enabled

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README.md
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/amdgpu_drv.so
%{_datadir}/X11/xorg.conf.d/10-amdgpu.conf
%{_mandir}/man4/amdgpu.4*
