#
# spec file for package WifiJoiner-gtk
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           WifiJoiner-gtk
Version:        0.0.1
Release:        0.1
License:        GPL-3.0
Summary:        A tool to create QR-Codes containing WIFI credentials
Url:            https://github.com/M0ses/WifiJoiner-gtk
Group:          Productivity/Networking/Other 
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  python
BuildRequires:  intltool
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  glib2-devel
Requires:       python-qrcode
Requires:       python-Pillow

# PreReq:
# Provides:
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%description
A tool to create QR-Codes containing your WIFI credentials, which can be read
by WifiJoiner, an android app which you can find under

https://play.google.com/store/apps/details?id=com.proj.wifijoiner&hl=de


%prep
%setup -q

%build
# %configure --prefix=/usr
./autogen.sh --prefix=/usr
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}

%post

%postun

%files
%defattr(-,root,root)
%dir /usr/bin
%dir /usr/lib
%dir /usr/lib/python2.7/
%dir /usr/lib/python2.7/site-packages/
%dir /usr/lib/python2.7/site-packages/wifi_joiner_gtk
%dir /usr/share/doc/wifijoiner-gtk
%dir /usr/share/wifijoiner-gtk
%dir /usr/share/wifijoiner-gtk/ui
%dir /usr/share/wifijoiner-gtk/ui/icons
%dir /usr/share/wifijoiner-gtk/ui/icons/36x36
%dir /usr/share/wifijoiner-gtk/ui/icons/48x48
%dir /usr/share/wifijoiner-gtk/ui/icons/72x72
/usr/bin/wifi-joiner
/usr/lib/python2.7/site-packages/wifi_joiner_gtk/wifi-joiner
/usr/share/wifijoiner-gtk/ui/WifiJoiner-gtk.ui
/usr/share/wifijoiner-gtk/ui/icons/36x36/WifiJoiner-gtk.png
/usr/share/wifijoiner-gtk/ui/icons/48x48/WifiJoiner-gtk.png
/usr/share/wifijoiner-gtk/ui/icons/72x72/WifiJoiner-gtk.png
/usr/share/doc/wifijoiner-gtk/AUTHORS
/usr/share/doc/wifijoiner-gtk/COPYING
/usr/share/doc/wifijoiner-gtk/ChangeLog
/usr/share/doc/wifijoiner-gtk/INSTALL
/usr/share/doc/wifijoiner-gtk/NEWS
/usr/share/doc/wifijoiner-gtk/README

