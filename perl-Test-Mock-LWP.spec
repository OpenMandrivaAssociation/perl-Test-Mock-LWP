%define upstream_name    Test-Mock-LWP
%define upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Mocks LWP::UserAgent
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/Test-Mock-LWP-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::MockObject)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This package arises from duplicating the same code to mock LWP et al in
several different modules I've written. This version is very minimalist,
but works for my needs so far. I'm very open to new suggestions and
improvements.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.60.0-1mdv2011
+ Revision: 690328
- update to new version 0.06

* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.50.0-2
+ Revision: 655227
- rebuild for updated spec-helper

* Wed May 05 2010 Michael Scherer <misc@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 542636
- import perl-Test-Mock-LWP


* Wed May 05 2010 cpan2dist 0.05-1mdv
- initial mdv release, generated with cpan2dist

