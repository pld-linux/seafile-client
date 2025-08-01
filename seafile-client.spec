Summary:	Seafile cloud storage desktop client
Name:		seafile-client
Version:	8.0.4
Release:	1
License:	Apache v2.0
Group:		Applications/Networking
Source0:	https://github.com/haiwen/seafile-client/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f1962a9033be781bf68acccc43c895ea
Patch0:		unknowwn-errors.patch
URL:		https://www.seafile.com/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	bash
BuildRequires:	ccnet-devel
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	jansson-devel
BuildRequires:	libsearpc-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libuuid-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	qt5-build
BuildRequires:	qt5-linguist
BuildRequires:	qt5-qmake
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	seafile-devel
BuildRequires:	sqlite3-devel
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Seafile is a next-generation open source cloud storage system, with
advanced support for file syncing, privacy protection and teamwork.

Seafile allows users to create groups with file syncing, wiki, and
discussion to enable easy collaboration around documents within a
team.

%prep
%setup -q
%patch -P0 -p1

%build
mkdir -p build
cd build
%cmake ../ \
	-DCMAKE_C_FLAGS="%{rpmcflags}" \
	-DCMAKE_CXX_FLAGS="%{rpmcxxflags}" \
	-Dqmake_executable:FILEPATH=/usr/bin/qmake-qt5 \
	-DUSE_QT5=ON \
	-DCMAKE_BUILD_TYPE=Release .

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/seafile.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%attr(755,root,root) %{_bindir}/seafile-applet
%{_desktopdir}/seafile.desktop
%{_pixmapsdir}/seafile.png
%{_iconsdir}/hicolor/scalable/apps/seafile.svg
%{_iconsdir}/hicolor/*/apps/seafile.png
