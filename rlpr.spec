Summary:	Remote printing utilities
Summary(pl):	Narzêdzia do zdalnego drukowania
Name:		rlpr
Version:	2.04
Release:	2
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://truffula.com/pub/%{name}-%{version}.tar.gz
# Source0-md5:	d4560cad31b0f031796a260b6d6b7123
Patch0:		%{name}-no_libnsl.patch
Patch1:		%{name}-ac25x.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rlpr is a package that makes it possible (or at the very least,
easier), to print files on remote sites to your local printer. The
rlpr package includes BSD-compatible replacements for `lpr', `lpq',
and `lprm', whose functionality is a superset of their BSD
counterparts. In other words, with the rlpr package, you can do
everything you can do with the BSD printing commands, and more. The
programs contained within the rlpr package are all GPL'd, and are more
lightweight, cleaner and more secure than their BSD counterparts.

%description -l pl
Rlpr jest pakietem który umo¿liwia (lub co najmniej u³atwia)
drukowanie plików ze zdalnych komputerów na lokalnej drukarce. Pakiet
rlpr zawiera zastêpniki dla 'lpr', 'lpq' i 'lprm', których funkcje s±
nadzbiorem BSDowych odpowiedników. Inaczej mówi±c oznacza to, ¿e
mo¿esz nimi robiæ to wszystko co oryginalnymi komendami BSD i jeszcze
wiêcej. Programy z pakietu rlpr s± wszystkie na licencji GPL, s±
mniejsze, czystsze i bardziej bezpieczne ni¿ ich BSDowe zastêpniki.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing acinclude.m4
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
