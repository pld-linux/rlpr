Summary:	Remote printing utilities
Summary(pl):	Narzêdzia do zdalnego drukowania
Name:		rlpr
Version:	2.04
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narzêdzia
Group(pt_BR):	Rede/Utilitários
Source0:	ftp://truffula.com/pub/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
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

%build
mv -f aclocal.m4 acinclude.m4
aclocal
automake -a -c
autoconf
autoheader
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS NEWS README THANKS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
