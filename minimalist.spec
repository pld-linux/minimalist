%include        /usr/lib/rpm/macros.perl
Summary:	Minimalistic Mailing Lists Manager
Summary(pl):	Minimalistyczny zarz±dca list dyskusyjnych
Name:		minimalist
Version:	2.3
Release:	1
License:	GPL
Group:		Applications/Mail
Vendor:		Vladimir Litovka <doka@kiev.sovam.com>
Source0:	http://www.mml.org.ua/%{name}.tar.gz
Source1:	%{name}.conf
Patch0:		%{name}-conf.patch
URL:		http://www.mml.org.ua/
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Minimalist stands for Minimalistic Mailing Lists Manager. Although it
is declared as minimalistic, it has many features as his eldest
brothers, such as Majordomo and so on, but in contrast to them it is
very small, fast, simple for setup and maintenance. Also it has very
clean internal structure and if you are familiar with Perl, you can
add as many additional features, as you need.

%description -l pl
Minimalist to skrót od Minimalistyczny Zarz±dca List Dyskusyjnych
(ang. Minimalistic Mailing Lists Manager). Jednak wbrew swojej nazwie
jest to program o wielu mo¿liwo¶ciach, jak inne programy tego typu
(np. Majordomo). W odró¿nieniu od nich jest ma³y, szybki, ³atwy w
konfiguracji i utrzymaniu. Posiada tak¿e przejrzyst± strukturê, i
je¶li znasz Perla, mo¿esz go rozszerzaæ wedle swoich potrzeb.

%prep
%setup -q -n %{name}-%{version}-1
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_var}/{log,spool/minimalist/sample}}
install -D minimalist.pl $RPM_BUILD_ROOT/%{_bindir}/minimalist.pl
install -D sample/lists.lst	$RPM_BUILD_ROOT/%{_var}/spool/minimalist/lists.lst
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/minimalist.conf
touch 	$RPM_BUILD_ROOT/var/log/Minimalist.log

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc minimalist.conf-sample docs sample
%attr(755,root,root) %{_bindir}/*
%attr(771,mail,mail) %dir %{_var}/spool/minimalist
%attr(640,root,mail) %{_var}/spool/minimalist/lists.lst
%attr(640,root,mail) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/minimalist.conf
%attr(660,mail,mail) %ghost /var/log/Minimalist.log
