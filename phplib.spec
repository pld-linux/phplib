Summary:	A library for PHP development
Summary(pl.UTF-8):	Biblioteka do rozwijania aplikacji PHP
Name:		phplib
Version:	7.4a
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://dl.sourceforge.net/phplib/%{name}-%{version}.tar.gz
# Source0-md5:	0dfc72f77d1503d562fa3cbbad066b48
URL:		http://phplib.sourceforge.net/
Requires:	%{name}-template = %{version}-%{release}
Requires:	php-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/php

%description
PHPLIB is a library that will help you to write medium to large sized
data-driven web applications with PHP.

%description -l pl.UTF-8
PHPLIB to biblioteka, która ułatwi ci pisanie średnich i dużych
aplikacji web bazujących na PHP.

%package template
Summary:	PHPLIB template engine
Summary(pl.UTF-8):	Silnik szablonów PHPLIB
Group:		Development/Languages/PHP

%description template
The template class allows you to keep your HTML code in some external
files which are completely free of PHP code, but contain replacement
fields. The class provides you with functions which can fill in the
replacement fields with arbitrary strings. These strings can become
very large, e.g. entire tables.

%description template -l pl.UTF-8
Klasa szablonów pozwala przechowywać kod HTML w plikach zewnętrznych,
całkowicie wolnych od kodu PHP, ale zawierających pola zastępcze.
Klasa ta udostępnia funkcje, którymi można wypełniać pola zastępcze
dowolnymi łańcuchami znaków. Łańcuchy te mogą być bardzo duże, np.
całymi tabelami.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}/%{name}

install php/* $RPM_BUILD_ROOT%{_appdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.html doc/FAQ.ps doc/README* CHANGES CREDITS HELP TODO pages
%dir %{_appdir}/%{name}
%{_appdir}/%{name}/*
%exclude %{_appdir}/%{name}/template.inc

%files template
%defattr(644,root,root,755)
%dir %{_appdir}/%{name}
%{_appdir}/%{name}/template.inc
