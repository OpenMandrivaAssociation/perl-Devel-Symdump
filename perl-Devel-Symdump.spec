%define upstream_name 	 Devel-Symdump
%define upstream_version 2.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Dump symbol names or the symbol table
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This little package serves to access the symbol table of perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
