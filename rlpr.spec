Summary:	Remote printing utilities
Summary(pl.UTF-8):	Narzędzia do zdalnego drukowania
Name:		rlpr
Version:	2.06
Release:	1
License:	GPL
Group:		Networking/Utilities
# Source0ActiveFTP
Source0:	ftp://truffula.com/pub/%{name}-%{version}.tar.gz
# Source0-md5:	c3192d0e84ccae432e754640f6003478
Patch0:		%{name}-no_libnsl.patch
Patch1:		%{name}-ac25x.patch
URL:		http://truffula.com/rlpr/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
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

%description -l pl.UTF-8
Rlpr jest pakietem który umożliwia (lub co najmniej ułatwia)
drukowanie plików ze zdalnych komputerów na lokalnej drukarce. Pakiet
rlpr zawiera zastępniki dla 'lpr', 'lpq' i 'lprm', których funkcje są
nadzbiorem odpowiedników z BSD. Inaczej mówiąc oznacza to, że można
nimi robić to wszystko co oryginalnymi komendami BSD i jeszcze więcej.
Programy z pakietu rlpr są wszystkie na licencji GPL, są mniejsze,
czystsze i bardziej bezpieczne niż ich odpowieniki z BSD.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
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
