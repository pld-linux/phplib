Summary:	A library for PHP development
Summary(pl):	Biblioteka do rozwijania aplikacji PHP
Name:		phplib
Version:	7.2d
Release:	1
Group:		Libraries
License:	LGPL
Source0:	http://prdownloads.sourceforge.net/phplib/%{name}-%{version}.tar.bz2
URL:		http://phplib.sourceforge.net/
Requires:	php-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpsharedir	%{_datadir}/php

%description
phplib is a library that will help you to write medium to large sized
data-driven web applications with PHP.

%description -l pl
phplib to biblioteka, która u³atwi ci pisanie ¶rednich i du¿ych
aplikacji web bazuj±cych na PHP.

%prep
%setup  -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phpsharedir}/%{name}

install php/*		$RPM_BUILD_ROOT%{_phpsharedir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.html doc/FAQ.ps doc/README* CHANGES CREDITS HELP TODO pages
%{_phpsharedir}/%{name}
