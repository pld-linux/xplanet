Summary:	Render a planetary image into an X window
Summary(pl.UTF-8):	Renderuje obrazek planety w okienku X window
Name:		xplanet
Version:	1.3.1
Release:	1
License:	GPL v2
Group:		X11/Amusements
Source0:	http://downloads.sourceforge.net/xplanet/%{name}-%{version}.tar.gz
# Source0-md5:	9797dbd9697d10205ca1671f728ea30d
Patch0:		%{name}-c++.patch
Patch1:		%{name}-giflib.patch
URL:		http://xplanet.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	cspice-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	gettext-tools
BuildRequires:	giflib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	netpbm-devel
BuildRequires:	pango-devel >= 1:1.2.0
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXext-devel
Requires:	pango >= 1:1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xplanet is similar to Xearth, where an image of the earth is rendered
into an X window. Azimuthal, Mercator, Mollweide, orthographic, or
rectangular projections can be displayed as well as a window with a
globe the user can rotate interactively. The other terrestrial planets
may also be displayed. The Xplanet home page has links to locations
with map files.

%description -l pl.UTF-8
Xplanet podobne jest do Xearth, gdzie obrazek ziemi jest wyświetlany w
X window. Mogą być także wyświetlane rzuty azymutalne, Mercatora,
Mollweide'a, ortograficzne lub prostokątne, kiedy okienko z globem
jest interaktywnie obracane. Mogą być także wyświetlane inne planety
lądowe. Strona domowa Xplanet zawiera odnośniki do plików z mapami.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# current code doesn't build in C++11 mode
CXXFLAGS="%{rpmcxxflags} -std=gnu++98"
# force using nl_langinfo interface instead of libcharset
%configure \
	ac_cv_header_localcharset_h=no

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/xplanet
%{_mandir}/man1/xplanet.1*
%{_datadir}/xplanet
