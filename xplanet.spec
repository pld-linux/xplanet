Summary:	render a planetary image into an X window
Summary(pl):	renderuje obrazek planety w okienku X window
Name:		xplanet
Version:	0.94
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	http://prdownloads.sourceforge.net/xplanet/%{name}-%{version}.tar.gz
URL:		http://xplanet.sourceforge.net
BuildRequires:	OpenGL-devel
BuildRequires:	glut-devel
BuildRequires:	libstdc++-devel	
BuildRequires:	kernel-headers
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libpng-devel
BuildRequires:	freetype-devel
Requires:	libpng
Requires:	libtiff
Requires:	libjpeg
Requires:	freetype

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Xplanet is similar to Xearth, where an image of the earth is rendered
into an X window. Azimuthal, Mercator, Mollweide, orthographic, or
rectangular projections can be displayed as well as a window with a
globe the user can rotate interactively. The other terrestrial planets
may also be displayed. The Xplanet home page has links to locations
with map files.

%description -l pl
Xplanet podobne jest do Xearth, gdzie obrazek ziemi jest wyświetlany w X window.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install prefix=$RPM_BUILD_ROOT/%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog COPYING CREDITS FAQ INSTALL README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/xplanet/*
