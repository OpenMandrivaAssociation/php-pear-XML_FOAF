%define		_class		XML
%define		_subclass	FOAF
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.3.0
Release:	8
Summary:	Provides the ability to manipulate FOAF RDF/XML
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/XML_FOAF/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
XML_FOAF allows advanced users to create advanced FOAF files.
The FOAF Project can be found at http://www.foaf-project.org/ -
XML_FOAF_Parser and XML_FOAF_Lite will follow before 1.0.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-6mdv2012.0
+ Revision: 742299
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-5
+ Revision: 679603
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-4mdv2011.0
+ Revision: 613789
- the mass rebuild of 2010.1 packages

* Wed Nov 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.0-3mdv2010.1
+ Revision: 464951
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.3.0-2mdv2010.0
+ Revision: 441715
- rebuild

* Mon Apr 20 2009 Raphaël Gertz <rapsys@mandriva.org> 0.3.0-1mdv2009.1
+ Revision: 368294
- Update php pear XML_FOAF to 0.3.0 version

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.2-9mdv2009.1
+ Revision: 322796
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2-8mdv2009.0
+ Revision: 237160
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2-7mdv2007.0
+ Revision: 82848
- Import php-pear-XML_FOAF

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2-1mdk
- initial Mandriva package (PLD import)

