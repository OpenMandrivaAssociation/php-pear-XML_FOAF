%define		_class		XML
%define		_subclass	FOAF
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - provides the ability to manipulate FOAF RDF/XML
Name:		php-pear-%{_pearname}
Version:	0.2
Release:	%mkrel 9
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
URL:		http://pear.php.net/package/XML_FOAF/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
XML_FOAF allows advanced users to create advanced FOAF files.
The FOAF Project can be found at http://www.foaf-project.org/ -
XML_FOAF_Parser and XML_FOAF_Lite will follow before 1.0.

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/FOAF/RAP/{model,rdql,syntax,util,vocabulary}

install %{_pearname}-%{version}/*.php %{buildroot}%{_datadir}/pear/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/RAP/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/RAP
install %{_pearname}-%{version}/%{_subclass}/RAP/model/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/RAP/model
install %{_pearname}-%{version}/%{_subclass}/RAP/rdql/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/RAP/rdql
install %{_pearname}-%{version}/%{_subclass}/RAP/syntax/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/RAP/syntax
install %{_pearname}-%{version}/%{_subclass}/RAP/util/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/RAP/util
install %{_pearname}-%{version}/%{_subclass}/RAP/vocabulary/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/RAP/vocabulary

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/%{_class}/%{_subclass}
%{_datadir}/pear/packages/%{_pearname}.xml


