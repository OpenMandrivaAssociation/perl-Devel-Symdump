%define upstream_name 	 Devel-Symdump
%define upstream_version 2.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Dump symbol names or the symbol table
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This little package serves to access the symbol table of perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{perl_vendorlib}/Devel
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.80.0-4mdv2012.0
+ Revision: 765184
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.80.0-3
+ Revision: 763700
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.80.0-2
+ Revision: 667118
- mass rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 2.80.0-1mdv2010.1
+ Revision: 406982
- rebuild using %%perl_convert_version

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 2.08-4mdv2010.0
+ Revision: 374673
- rebuild

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 2.08-3mdv2010.0
+ Revision: 374658
- fix error in macro - wtf was up with this package?
- update to 2.08 (for real this time)

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.08-2mdv2009.0
+ Revision: 223637
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.08-1mdv2008.1
+ Revision: 97493
- update to new version 2.08


* Sat Jan 06 2007 Olivier Thauvin <nanardon@mandriva.org> 2.07.00-1mdv2007.0
+ Revision: 104857
- 2.07

* Tue Dec 12 2006 Olivier Thauvin <nanardon@mandriva.org> 2.06.02-1mdv2007.1
+ Revision: 95136
- Import perl-Devel-Symdump

* Thu Aug 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.06.02-1mdv2007.0
- New version (upstream version 2.0602)

* Sat Jun 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.06.01-1mdv2007.0
- new version (upstream version 2.0601)

* Mon Jan 30 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.06-1mdk
- 2.06

* Tue Jan 03 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.05-1mdk
- 2.05
- Update description and url, remove hardcoded packager, use mkrel

