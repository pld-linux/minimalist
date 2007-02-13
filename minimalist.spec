%include        /usr/lib/rpm/macros.perl
Summary:	Minimalistic Mailing Lists Manager
Summary(pl.UTF-8):	Minimalistyczny zarządca list dyskusyjnych
Name:		minimalist
Version:	2.5.3
Release:	1
License:	BSD
Group:		Applications/Mail
Vendor:		Vladimir Litovka <doka@kiev.sovam.com>
Source0:	http://www.mml.org.ua/LIST/%{name}-%{version}.tar.gz
# Source0-md5:	69109fccbc3cca278f6d2a2ce630ee91
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

%description -l pl.UTF-8
Minimalist to skrót od Minimalistyczny Zarządca List Dyskusyjnych
(ang. Minimalistic Mailing Lists Manager). Jednak wbrew swojej nazwie
jest to program o wielu możliwościach, jak inne programy tego typu
(np. Majordomo). W odróżnieniu od nich jest mały, szybki, łatwy w
konfiguracji i utrzymaniu. Posiada także przejrzystą strukturę, a
znając Perla, można go rozszerzać wedle swoich potrzeb.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/mail/minimalist,%{_var}/{log,spool/minimalist/sample}}
install -D minimalist.pl $RPM_BUILD_ROOT%{_bindir}/minimalist.pl
install -D sample/lists.lst $RPM_BUILD_ROOT%{_var}/spool/minimalist/lists.lst
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/mail/minimalist/minimalist.conf
ln -s	%{_var}/spool/minimalist $RPM_BUILD_ROOT%{_sysconfdir}/mail/minimalist/lists
touch 	$RPM_BUILD_ROOT/var/log/Minimalist.log

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc minimalist.conf-sample docs sample
%attr(755,root,root) %{_bindir}/*
%attr(755,mail,mail) %dir %{_sysconfdir}/mail/minimalist
%attr(640,root,mail) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mail/minimalist/minimalist.conf
%attr(771,mail,mail) %dir %{_var}/spool/minimalist
%attr(640,root,mail) %config(noreplace) %verify(not md5 mtime size) %{_var}/spool/minimalist/lists.lst
%attr(660,mail,mail) %ghost /var/log/Minimalist.log
%{_sysconfdir}/mail/minimalist/lists
