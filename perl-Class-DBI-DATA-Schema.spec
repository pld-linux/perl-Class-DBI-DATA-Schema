#
# Conditional build:
%bcond_with	tests		# perform "make test"

%define	pdir	Class
%define	pnam	DBI-DATA-Schema
Summary:	Class::DBI::DATA::Schema - execute Class::DBI SQL from DATA sections
Summary(pl.UTF-8):	Class::DBI::DATA::Schema - wykonanie SQL-a w oparciu o Class::DBI z sekcji DATA
Name:		perl-Class-DBI-DATA-Schema
Version:	1.00
Release:	4
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fb5b44fefc7095dde22c752f43691f54
URL:		http://search.cpan.org/dist/Class-DBI-DATA-Schema/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-DBI >= 0.94
BuildRequires:	perl-Test-Simple >= 0.45
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an extension to Class::DBI which injects a method into your
class to find and execute all SQL statements in the DATA section of
the package.

%description -l pl.UTF-8
Ta klasa jest rozszerzeniem Class::DBI umieszczającym w dziedziczącej
klasie metodę do znajdywania i wykonywania wszystkich instrukcji SQL-a
z sekcji DATA pakietu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Class/DBI/DATA
%{perl_vendorlib}/Class/DBI/DATA/*.pm
%{_mandir}/man3/*
