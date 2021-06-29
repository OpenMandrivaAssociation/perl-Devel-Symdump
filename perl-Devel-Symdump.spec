%define modname	Devel-Symdump
%define modver 2.18

# Avoid nasty build dependency loop
%define dont_gprintify 1

Summary:	Dump symbol names or the symbol table
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	5
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Devel::Symdump
Source0:	http://www.cpan.org/modules/by-module/Devel/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
This little package serves to access the symbol table of perl.

%prep
%autosetup -p1 -n %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%make_install
find %{buildroot} -name .packlist -o -name perllocal.pod |xargs rm -f

%files
%doc  README
%{perl_vendorlib}/Devel
%{_mandir}/man3/*
