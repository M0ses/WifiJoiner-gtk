dnl Process this file with autoconf to produce a configure script.
dnl Created by Anjuta application wizard.

AC_INIT(WifiJoiner-gtk, 0.0.1)

AC_CONFIG_HEADERS([config.h])

AM_INIT_AUTOMAKE([1.11])

AM_PATH_PYTHON

AC_PROG_SED

dnl ***************************************************************************
dnl Internationalization
dnl ***************************************************************************
IT_PROG_INTLTOOL([0.35.0])

GETTEXT_PACKAGE=WifiJoiner-gtk
AC_SUBST(GETTEXT_PACKAGE)
AC_DEFINE_UNQUOTED(GETTEXT_PACKAGE,"$GETTEXT_PACKAGE", [GETTEXT package name])
AM_GLIB_GNU_GETTEXT






AC_OUTPUT([
Makefile
src/Makefile
src/icons/Makefile
src/icons/36x36/Makefile
src/icons/48x48/Makefile
src/icons/72x72/Makefile
po/Makefile.in
])
