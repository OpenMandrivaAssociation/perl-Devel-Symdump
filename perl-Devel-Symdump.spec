%define module		Devel-Symdump
%define name		perl-%{module}
%define version 	2.08
%define release		%mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Dump symbol names or the symbol table
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:		http://www.cpan.org/modules/by-module/Devel/%{module}-%{revision}.tar.gz
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This little package serves to access the symbol table of perl.

%prep
%setup -q -n %{module}-%{revision}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorlib}/Devel
%{_mandir}/*/*


