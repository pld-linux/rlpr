Summary:	Remote printing utilities
Summary(pl):	Narz�dzia do zdalnego drukowania
Name:		rlpr
Version:	2.04
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narz�dzia
Group(pt_BR):	Rede/Utilit�rios
Source0:	ftp://truffula.com/pub/%{name}-%{version}.tar.gz
Patch0:		%{name}-no_libnsl.patch
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
Rlpr jest pakietem kt�ry umo�liwia (lub co najmniej u�atwia)
drukowanie plik�w ze zdalnych komputer�w na lokalnej drukarce. Pakiet
rlpr zawiera zast�pniki dla 'lpr', 'lpq' i 'lprm', kt�rych funkcje s�
nadzbiorem BSDowych odpowiednik�w. Inaczej m�wi�c oznacza to, �e
mo�esz nimi robi� to wszystko co oryginalnymi komendami BSD i jeszcze
wi�cej. Programy z pakietu rlpr s� wszystkie na licencji GPL, s�
mniejsze, czystsze i bardziej bezpieczne ni� ich BSDowe zast�pniki.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing acinclude.m4
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS NEWS README THANKS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
