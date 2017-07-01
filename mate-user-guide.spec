%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE user file sharing
Name:		mate-user-guide
Version:	1.18.0
Release:	1
License:	GPLv2+
Group:		System/Servers
Url:		http://www.mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:  mate-common
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:	yelp-tools
BuildArch:	noarch

%description
End-users documentation for MATE desktop.

%prep
%setup -q

%build
#NOCONFIGURE=1 ./autogen.sh
%configure
%make

%install
%makeinstall_std

# locales
%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS COPYING README ChangeLog NEWS
%{_datadir}/applications/mate-user-guide.desktop

