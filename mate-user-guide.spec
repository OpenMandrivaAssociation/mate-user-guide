%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE user file sharing
Name:		mate-user-guide
Version:	1.18.0
Release:	2
License:	GPLv2+
Group:		System/Servers
Url:		https://www.mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:  desktop-file-utils
BuildRequires:	intltool
BuildRequires:  mate-common
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:	yelp-tools

Requires:       mate-desktop
Requires:	yelp

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package provide documents which will be packaged together and shipped
as mate-user-guide in the core MATE distribution.

%files -f %{name}.lang
%doc AUTHORS COPYING README ChangeLog NEWS
%{_datadir}/applications/mate-user-guide.desktop

#---------------------------------------------------------------------------

%prep
%setup -q

%build
#NOCONFIGURE=1 ./autogen.sh
%configure
%make

%install
%makeinstall_std

# locales
%find_lang %{name} --with-gnome --all-name

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
