%define with_kpilot 1
%{?_with_kpilot: %{expand: %%global with_kpilot 1}}

%define with_kitchensync 0
%{?_with_kitchensync: %{expand: %%global with_kitchensync 1}}

Name: kmail-nepomuk
Summary: KMail enhanced with semantic capabilities
Version: 4.3.2
Release: %mkrel 3
Epoch: 2
Group: Graphical desktop/KDE
License: GPL
URL: http://pim.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdepim-%version.tar.bz2
# Mandriva "customization" patches
Patch0:   kdepim-4.2.95-kmail-first-message.patch 
Patch1:   kdepim-4.3.1-fix-desktop-files.patch
Patch2:   kdepim-4.3.2-kmail-nepomuk.patch
# Patches from branch
Patch100: kdepim-4.3.2-b1031050-fix-cmake-macro.patch
Patch101: kdepim-4.3.2-b1031051-fix-data-corruption.patch
Patch102: kdepim-4.3.2-b1031052-fix-show-old-event.patch
Patch103: kdepim-4.3.2-b1031053-fix-recursive-event.patch
Patch104: kdepim-4.3.2-b1031056-fix-data-corruption.patch
Patch105: kdepim-4.3.2-b1031560-fix-compile-commit1031056.patch
Patch106: kdepim-4.3.2-b1031368-load-catalogs.patch
Patch107: kdepim-4.3.2-b1031532-fix-cmake-macro.patch
Patch108: kdepim-4.3.2-b1031533-fix-cmake-macro.patch
Patch109: kdepim-4.3.2-b1031538-load-catalogs.patch
Patch110: kdepim-4.3.2-b1031716-load-catalogs.patch
Patch111: kdepim-4.3.2-b1032446-fix-template-export.patch
Patch112: kdepim-4.3.2-b1032449-use-grp2-grp3.patch
Patch113: kdepim-4.3.2-b1032418-fix-CPU-eating.patch
Patch114: kdepim-4.3.2-b1032499-fix-crash-with-shared-calendar.patch
Patch115: kdepim-4.3.2-b1032802-fix-missing-rename.patch
Patch116: kdepim-4.3.2-b1032874-fix-kolab-imap.patch
Patch117: kdepim-4.3.2-b1033121-fix-crash-with-empty-selecteddates.patch
Patch118: kdepim-4.3.2-b1033122-fix-identity-in-invitation.patch
Patch119: kdepim-4.3.2-b1033302-fix-ldap-crash.patch
Patch120: kdepim-4.3.2-b1033303-fix-setAttrs.patch
Patch121: kdepim-4.3.2-b1033304-fix-crash-in-setHolidayMasks.patch
Patch122: kdepim-4.3.2-b1033308-workaround-buildObjectTree-issue.patch
Patch123: kdepim-4.3.2-b1033311-fix-corruption.patch
Patch124: kdepim-4.3.2-b1033312-fix-pgp-mime.patch
Patch125: kdepim-4.3.2-b1033313-fix-signature-in-encryption.patch
Patch126: kdepim-4.3.2-b1033320-fix-trigger-conditions-for-store-unencrypted-feature.patch
Patch127: kdepim-4.3.2-b1033327-fix-recurrences.patch
Patch128: kdepim-4.3.2-b1033333-fix-namespace.patch
Patch129: kdepim-4.3.2-b1033377-fix-processing-time-calculating-for-archived-alarms.patch
Patch130: kdepim-4.3.2-b1033731-fix-whatsthis.patch
Patch131: kdepim-4.3.2-b1034078-use-ReplyAll-only-for-ML.patch

Buildroot: %_tmppath/%name-%version-%release-root
BuildRequires: kdelibs4-devel >= 2:4.2.98
BuildRequires: kdelibs4-experimental-devel >= 2:4.2.98
BuildRequires: kdepimlibs4-devel >= 2:4.2.98
BuildRequires: kdepim4-runtime-devel >= 4.2.98
BuildRequires: gpgme-devel
BuildRequires: X11-devel 
BuildRequires: flex 
BuildRequires: byacc 
BuildRequires: pam
BuildRequires: libncurses-devel
BuildRequires: readline-devel
BuildRequires: libgpg-error-devel
BuildRequires: gnokii-devel >= 0.6.18
BuildRequires: libxml2-utils
BuildRequires: gnupg
BuildRequires: bluez-devel 
BuildRequires: libsasl-devel
BuildRequires: pilot-link-devel
BuildRequires: libxslt-proc
BuildRequires: boost-devel
BuildRequires: qca2-devel
BuildRequires: glib2-devel
BuildRequires: libassuan-devel
BuildRequires: mysql-static-devel
BuildRequires: libmal-devel
BuildRequires: soprano-devel
BuildRequires: automoc
BuildRequires: nepomuk-scribo
BuildRequires: nepomuk-scribo-devel

%if %{with_kitchensync}
BuildRequires: libopensync-devel >= 0.30
%endif
BuildRequires: akonadi-devel
#FIXME: Remove later
BuildRequires: kdepimlibs4-core
Suggests:      akonadi-common
Suggests:      kleopatra
Suggests:      akregator
%if %{with_kitchensync}
Suggests:      kitchensync
%endif
Suggests: knode
Suggests: kaddressbook
Suggests: kalarm
Suggests: ktimetracker
Suggests: kmailcvt
Suggests: knotes
Suggests: kontact
Suggests: korganizer
Suggests: ksendemail
Suggests: kjots
%if %{with_kpilot}
Suggests: kpilot
%else
Obsoletes: kpilot < %epoch:%version
%endif
Obsoletes: korn <= 2:4.1.0
%if %mdkversion >= 200910
Obsoletes: kdepim-korn < 1:3.5.10-2
Obsoletes: kdepim-kandy < 1:3.5.10-2
Obsoletes: kdepim-ktnef < 1:3.5.10-2
Obsoletes: kdepim < 1:3.5.10-2
%endif
Obsoletes: ktnef
Requires: kdepim4-core = %epoch:%version
Requires: kdepimlibs4-core
Requires: sasl-plug-plain
Requires: sasl-plug-ntlm
Requires: sasl-plug-login
Requires: sasl-plug-digestmd5
Requires: kio4-pop3
Requires: kio4-smtp
Requires: kio4-mbox
Requires: kio4-imap
Requires: kio4-sieve
Requires: nepomuk-scribo
Suggests: kmailcvt
Suggests: pinentry-qt4
Suggests: openssh-askpass-qt4
Obsoletes: kde4-kmail < 2:4.0.68
Obsoletes: kdepim4-plugins <= 2:4.0.83
Obsoletes: %name-kmail < 1:3.93.0-1
%if %mdkversion >= 200910
Obsoletes: kdepim-kmail < 1:3.5.10-2
%endif
Conflicts: kontact < 2:4.0.83-2
Conflicts: kmail

%description
KMail KMail Nepomuk is an enhanced version of KMail providing 
semi-automatic annotation capabilities. 

%files
%defattr(-,root,root)
%doc README.urpmi
%_kde_bindir/kmail
%_kde_bindir/kmail_antivir.sh
%_kde_bindir/kmail_clamav.sh
%_kde_bindir/kmail_fprot.sh
%_kde_bindir/kmail_sav.sh
%_kde_appsdir/kmail
%_kde_datadir/kde4/services/kontact/kmailplugin.desktop
%_kde_datadir/applications/kde4/KMail.desktop
%_kde_datadir/applications/kde4/kmail_view.desktop
%_kde_appsdir/kconf_update/kmail*
%_kde_appsdir/kconf_update/upgrade-signature.pl
%_kde_appsdir/kconf_update/upgrade-transport.pl
%_kde_datadir/config.kcfg/custommimeheader.kcfg
%_kde_datadir/config.kcfg/customtemplates_kfg.kcfg
%_kde_datadir/config.kcfg/kmail.kcfg
%_kde_datadir/config.kcfg/replyphrases.kcfg
%_kde_datadir/config.kcfg/templatesconfiguration_kfg.kcfg
%_kde_datadir/config/kmail.antispamrc
%_kde_datadir/config/kmail.antivirusrc
%_kde_datadir/kde4/services/kmail_config_accounts.desktop
%_kde_datadir/kde4/services/kmail_config_appearance.desktop
%_kde_datadir/kde4/services/kmail_config_composer.desktop
%_kde_datadir/kde4/services/kmail_config_identity.desktop
%_kde_datadir/kde4/services/kmail_config_misc.desktop
%_kde_datadir/kde4/services/kmail_config_security.desktop
%_kde_datadir/kde4/servicetypes/dbusimap.desktop
%_kde_datadir/kde4/servicetypes/dbusmail.desktop
%_kde_libdir/kde4/kcm_kmail.so
%_kde_libdir/kde4/kmailpart.so
%_kde_libdir/kde4/kmail_bodypartformatter_*
%_kde_libdir/kde4/kcm_kmailsummary.so
%_kde_libdir/kde4/kontact_kmailplugin.so
%_kde_libdir/kde4/ktexteditorkabcbridge.so
%_kde_datadir/kde4/services/kcmkmailsummary.desktop
%_kde_docdir/HTML/en/kmail

%define libkmailnepomukprivate %mklibname kmailnepomukprivate 4

%package -n %libkmailnepomukprivate
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{mklibname kdepim42-common} < 1:3.93.0-1

%description -n %libkmailnepomukprivate
KDE 4 library.

%files -n %libkmailnepomukprivate
%defattr(-,root,root)
%_kde_libdir/libkmailnepomukprivate.so.*



%prep
%setup -q -n kdepim-%version
%patch0 -p0
%patch1 -p0
%patch2 -p1

%patch100 -p0
%patch101 -p0
%patch102 -p0
%patch103 -p0
%patch104 -p0
%patch105 -p0
%patch106 -p0
%patch107 -p0
%patch108 -p0
%patch109 -p0
%patch110 -p0
%patch111 -p0
%patch112 -p0
%patch113 -p0
%patch114 -p0
%patch115 -p0
%patch116 -p0
%patch117 -p0
%patch118 -p0
%patch119 -p0
%patch120 -p0
%patch121 -p0
%patch122 -p0
%patch123 -p0
%patch124 -p0
%patch125 -p0
%patch126 -p0
%patch127 -p0
%patch128 -p0
%patch129 -p0
%patch130 -p0
%patch131 -p0

# Remove extra icons already in oxygen
rm -f kmail/icons/ox*
rm -f kmail/icons/small/ox*

%build
%cmake_kde4

%make kmail

%install
#rm -fr %buildroot

%makeinstall_std -C build/kmail
%makeinstall_std -C build/kontact/plugins/kmail
%makeinstall_std -C build/plugins/ktexteditor
%makeinstall_std -C build/doc/kmail

rm -f %buildroot/usr/include/kmail/interfaces/bodypart.h
rm -f %buildroot/usr/include/kmail/interfaces/bodypartformatter.h
rm -f %buildroot/usr/include/kmail/interfaces/bodyparturlhandler.h
rm -f %buildroot/usr/include/kmail/interfaces/htmlwriter.h
rm -f %buildroot/usr/include/kmail/interfaces/observable.h
rm -f %buildroot/usr/include/kmail/interfaces/observer.h
rm -f %buildroot/usr/share/icons/hicolor/64x64/apps/kmail.png
rm -f %buildroot/usr/share/apps/kontact/ksettingsdialog/kmail.setdlg
rm -f %buildroot/usr/share/dbus-1/interfaces/org.kde.kmail.kmail.xml
rm -f %buildroot/usr/share/dbus-1/interfaces/org.kde.kmail.kmailpart.xml
rm -f %buildroot/usr/share/dbus-1/interfaces/org.kde.kmail.mailcomposer.xml
rm -f %buildroot/usr/share/icons/hicolor/128x128/apps/kmail.png
rm -f %buildroot/usr/share/icons/hicolor/16x16/apps/kmail.png
rm -f %buildroot/usr/share/icons/hicolor/22x22/apps/kmail.png
rm -f %buildroot/usr/share/icons/hicolor/32x32/apps/kmail.png
rm -f %buildroot/usr/share/icons/hicolor/48x48/apps/kmail.png
rm -f %buildroot/usr/share/icons/hicolor/scalable/apps/kmail.svgz

cat > README.urpmi <<EOF

KMail-Nepomuk has been introduced into the contrib media for
demonstration purpose only. It should by no means be used in a
production environment. The package can cause data loss. Mandriva
recommends the use of the standard KMail package.

EOF


 
%clean
#rm -fr %buildroot

