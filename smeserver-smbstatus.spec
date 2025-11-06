Summary: SME server smbstatus
%define name smeserver-smbstatus
Name: %{name}
%define version 1.2
%define release 6
Version: %{version}
Release: %{release}%{?dist}
#Copyright: Freely distributable
Group: Apache/php/caching
Source: %{name}-%{version}.tar.xz

License: GNU GPL version 2
Packager: Michel Van hees <michel@vanhees.cc>
BuildRoot: /var/tmp/e-smith-buildroot
BuildRequires: smeserver-devtools
BuildArchitectures: noarch
Requires: smeserver-release >= 8
AutoReqProv: no

%changelog
* Thu Nov 06 2025 Brian Read <brianr@koozali.org> 1.2-6.sme
- Make sure rpm has .el8.sme in name [SME: 13275]

* Sun Sep 08 2024 fix-e-smith-pkg.sh by Trevor Batley <trevor@batley.id.au> 1.2-5.sme
- Fix e-smith references in smeserver-smbstatus [SME: 12732]

* Sat Sep 07 2024 cvs2git.sh aka Brian Read <brianr@koozali.org> 1.2-4.sme
- Roll up patches and move to git repo [SME: 12338]

* Sat Sep 07 2024 BogusDateBot
- Eliminated rpmbuild "bogus date" warnings due to inconsistent weekday,
  by assuming the date is correct and changing the weekday.

* Sun Mar 28 2021 Brian Read <brianr@bjsystems.co.uk> 1.2-3.sme
- Add Update event to createlinks [SME: 11037]

* Sun Mar 28 2021 BogusDateBot
- Eliminated rpmbuild "bogus date" warnings due to inconsistent weekday,
  by assuming the date is correct and changing the weekday.

* Wed Oct 14 2020 BogusDateBot
- Eliminated rpmbuild "bogus date" warnings due to inconsistent weekday,
  by assuming the date is correct and changing the weekday.
  Mon Mar 21 2006 --> Mon Mar 20 2006 or Tue Mar 21 2006 or Mon Mar 27 2006 or ....

* Tue Oct 13 2020 Brian Read <brianr@bjsystems.co.uk> 1.2-2.sme
- Initial import into SME10 tree [SME: 11037
- Add link to wrapper in createlinks]

* Thu Sep 24 2015 stephane de Labrusse <stephdl@de-labrusse.fr> 1.2-1.sme
- Initial release to contribs9

* Thu Sep 24 2015 stephane de Labrusse <stephdl@de-labrusse.fr> 1.0-7.sme
- Initial release to contribs8

* Sat Feb 08 2014 Stephane de Labrusse <stephdl@de-labrusse.fr> smeserver-smbstatus-1.0-6
- change menu heading

* Wed Feb 05 2014 Stephane de Labrusse <stephdl@de-labrusse.fr> smeserver-smbstatus-1.0-5
- adaptation to new build protocol
 
* Mon Jan 07 2008 Michel Van hees <michel@vanhees.cc>
- Thanks to Sylvain Gomez for his fix with french traduction

* Tue Mar 21 2006 Michel Van hees <michel@vanhees.cc>
  Mon Mar 21 2006 --> Mon Mar 20 2006 or Tue Mar 21 2006 or Mon Mar 27 2006 or ....
- start developpement

%description
Display samba status in server-manager

%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING"          >> %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%pre
%preun
%post
/etc/e-smith/events/actions/navigation-conf > /dev/null 2>&1

%postun
/etc/e-smith/events/actions/navigation-conf > /dev/null 2>&1

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
