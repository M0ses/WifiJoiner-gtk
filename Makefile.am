## Process this file with automake to produce Makefile.in
## Created by Anjuta

SUBDIRS = src po

dist_doc_DATA = \
	README \
	COPYING \
	AUTHORS \
	ChangeLog \
	INSTALL \
	NEWS


INTLTOOL_FILES = intltool-extract.in \
	intltool-merge.in \
	intltool-update.in

EXTRA_DIST = \
	$(INTLTOOL_FILES)

DISTCLEANFILES = intltool-extract \
	intltool-merge \
	intltool-update \
	po/.intltool-merge-cache


# Remove doc directory on uninstall
uninstall-local:
	-rm -r $(docdir)

rpm:
	[ -d $(HOME)/rpmbuild/SOURCES/ ] || mkdir -p $(HOME)/rpmbuild/SOURCES/
	[ -d $(HOME)/rpmbuild/SPECS/ ] || mkdir -p $(HOME)/rpmbuild/SPECS/
	TEMPDIR="$(shell mktemp -d)"; \
	cp -av `pwd` $$TEMPDIR/wifijoiner-gtk-$(PACKAGE_VERSION); \
	tar -C $$TEMPDIR -cvjf $(HOME)/rpmbuild/SOURCES/wifijoiner-gtk-$(PACKAGE_VERSION).tar.bz2 wifijoiner-gtk-$(PACKAGE_VERSION) ; \
	rm -rf $$TEMPDIR
	install -m 644 RPM/WifiJoiner-gtk.spec $(HOME)/rpmbuild/SPECS/ 
	rpmbuild -ba $(HOME)/rpmbuild/SPECS/WifiJoiner-gtk.spec
