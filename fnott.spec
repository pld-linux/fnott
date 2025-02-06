Summary:	Keyboard driven and lightweight Wayland notification daemon
Name:		fnott
Version:	1.7.1
Release:	2
License:	MIT and Zlib
Group:		Applications
Source0:	https://codeberg.org/dnkl/fnott/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	655083997c9f3d8b97d6b63831d43692
URL:		https://codeberg.org/dnkl/fnott/
BuildRequires:	dbus-devel
BuildRequires:	fcft-devel < 4.0.0
BuildRequires:	fcft-devel >= 3.0.0
BuildRequires:	fontconfig-devel
BuildRequires:	libpng-devel
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja
BuildRequires:	pixman-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	scdoc
BuildRequires:	tllist-devel >= 1.0.1
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols >= 1.32
Requires(post,postun):	desktop-file-utils
Requires:	fcft < 4.0.0
Requires:	fcft >= 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fnott is a keyboard driven and lightweight notification daemon for
wlroots-based Wayland compositors.

%package -n zsh-completion-fnott
Summary:	ZSH completion for fnott command line
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	zsh
BuildArch:	noarch

%description -n zsh-completion-fnott
ZSH completion for fnott command line.

%prep
%setup -q

%build
%meson \
	-Dsystemd-units-dir="%{systemduserunitdir}"

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%systemd_user_post fnott.service

%preun
%systemd_user_preun fnott.service

%postun
%update_desktop_database_postun
%systemd_user_postun fnott.service

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md
%dir %{_sysconfdir}/xdg/fnott
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/fnott/fnott.ini
%attr(755,root,root) %{_bindir}/fnott
%attr(755,root,root) %{_bindir}/fnottctl
%{systemduserunitdir}/fnott.service
%{_datadir}/dbus-1/services/fnott.service
%{_desktopdir}/fnott.desktop
%{_mandir}/man1/fnott.1*
%{_mandir}/man1/fnottctl.1*
%{_mandir}/man5/fnott.ini.5*

%files -n zsh-completion-fnott
%defattr(644,root,root,755)
%{zsh_compdir}/_fnott
%{zsh_compdir}/_fnottctl
