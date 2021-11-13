%define		kdeplasmaver	5.23.3
%define		qtver		5.11.0
%define		kpname		plasma-browser-integration

Summary:	KDE Plasma Browser Integration
Name:		kp5-%{kpname}
Version:	5.23.3
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	bf0dee43861a33fc38893e8139ce111f
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules
BuildRequires:	kf5-kactivities-devel
BuildRequires:	kf5-kauth-devel
BuildRequires:	kf5-kcodecs-devel
BuildRequires:	kf5-kcompletion-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kcrash-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kfilemetadata-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kitemviews-devel
BuildRequires:	kf5-kjobwidgets-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-kpackage-devel
BuildRequires:	kf5-krunner-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	kf5-plasma-framework-devel
BuildRequires:	kf5-purpose-devel
BuildRequires:	kf5-solid-devel
BuildRequires:	kp5-plasma-workspace-devel >= %{kdeplasmaver}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KDE Plasma Browser Integration.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%dir %{_sysconfdir}/chromium
%dir %{_sysconfdir}/chromium/native-messaging-hosts
%{_sysconfdir}/chromium/native-messaging-hosts/org.kde.plasma.browser_integration.json
%dir %{_sysconfdir}/opt/chrome
%dir %{_sysconfdir}/opt/chrome/native-messaging-hosts
%{_sysconfdir}/opt/chrome/native-messaging-hosts/org.kde.plasma.browser_integration.json
%attr(755,root,root) %{_bindir}/plasma-browser-integration-host
%dir %{_prefix}/lib/mozilla
%dir %{_prefix}/lib/mozilla/native-messaging-hosts
%{_prefix}/lib/mozilla/native-messaging-hosts/org.kde.plasma.browser_integration.json
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/browserintegrationreminder.so
%dir %{_sysconfdir}/opt/edge
%dir %{_sysconfdir}/opt/edge/native-messaging-hosts
%{_sysconfdir}/opt/edge/native-messaging-hosts/org.kde.plasma.browser_integration.json
%{_datadir}/krunner/dbusplugins/plasma-runner-browserhistory.desktop
%{_datadir}/krunner/dbusplugins/plasma-runner-browsertabs.desktop
%{_desktopdir}/org.kde.plasma.browser_integration.host.desktop
