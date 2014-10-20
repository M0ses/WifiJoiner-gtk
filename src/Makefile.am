## Process this file with automake to produce Makefile.in
## Created by Anjuta

SUBDIRS = icons

uidir = $(pkgdatadir)/ui
ui_DATA = WifiJoiner-gtk.ui

## The main script
bin_SCRIPTS = wifi-joiner

## Directory where .class files will be installed
wifi_joiner_gtkdir = $(pythondir)/wifi_joiner_gtk


wifi_joiner_gtk_PYTHON = \
	wifi-joiner

desktopdir = $(prefix)/share/applications

desktop_DATA = wifijoiner-gtk.desktop

EXTRA_DIST = $(ui_DATA)


# Remove ui directory on uninstall
uninstall-local:

	-rm -r $(uidir)

	-rm -r $(pkgdatadir)

wifi-joiner: wifi-joiner.in
	-[ -f $@ ] && rm -f $@
	$(SED) -e "s:[@]uidir@:$(uidir):" $< > $@
	chmod 755 $@
