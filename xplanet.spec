Summary:	Render a planetary image into an X window
Summary(pl):	Renderuje obrazek planety w okienku X window
Name:		xplanet
Version:	1.1.1
Release:	2
License:	GPL
Group:		X11/Amusements
Source0:	http://dl.sourceforge.net/xplanet/%{name}-%{version}.tar.gz
# Source0-md5:	13d7b2b3899c3af58668058ff951d1d9
URL:		http://xplanet.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	glut-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xplanet is similar to Xearth, where an image of the earth is rendered
into an X window. Azimuthal, Mercator, Mollweide, orthographic, or
rectangular projections can be displayed as well as a window with a
globe the user can rotate interactively. The other terrestrial planets
may also be displayed. The Xplanet home page has links to locations
with map files.

%description -l pl
Xplanet podobne jest do Xearth, gdzie obrazek ziemi jest wy�wietlany w
X window. Mog� by� tak�e wy�wietlane rzuty azymutalne, Mercatora,
Mollweide'a, ortograficzne lub prostok�tne, kiedy okienko z globem
jest interaktywnie obracane. Mog� by� tak�e wy�wietlane inne planety
l�dowe. Strona domowa Xplanet zawiera odno�niki do plik�w z mapami.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# force using nl_langinfo interface instead of libcharset
%configure \
	ac_cv_header_localcharset_h=no

%{__make} \
	CPPFLAGS="-I/usr/include/freetype2 -I/usr/X11R6/include -I`pwd`" \
	CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/xplanet
