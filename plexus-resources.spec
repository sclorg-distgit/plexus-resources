%global pkg_name plexus-resources
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%global parent plexus
%global subname resources
%global namedversion 1.0-alpha-7

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.0
Release:        0.15.a7.12%{?dist}
Summary:        Plexus Resource Manager
License:        MIT
URL:            http://plexus.codehaus.org/
# svn export http://svn.codehaus.org/plexus/plexus-components/tags/plexus-resources-1.0-alpha-7/
# tar caf plexus-resources-1.0-alpha-7-src.tar.xz plexus-resources-1.0-alpha-7
Source0:        %{pkg_name}-%{version}-alpha-7-src.tar.xz

BuildRequires:  %{?scl_prefix_java_common}javapackages-tools
BuildRequires:  %{?scl_prefix_java_common}ant >= 0:1.6
BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  maven30-maven-compiler-plugin
BuildRequires:  maven30-maven-install-plugin
BuildRequires:  maven30-maven-jar-plugin
BuildRequires:  maven30-maven-javadoc-plugin
BuildRequires:  maven30-maven-release-plugin
BuildRequires:  maven30-maven-resources-plugin
BuildRequires:  maven30-maven-surefire-plugin
BuildRequires:  maven30-maven-surefire-provider-junit
BuildRequires:  maven30-plexus-containers-container-default
BuildRequires:  maven30-plexus-utils

BuildArch:      noarch

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -q -n %{pkg_name}-%{namedversion}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_file  : %{parent}/%{subname}
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/plexus
%dir %{_javadir}/plexus

%files javadoc -f .mfiles-javadoc

%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.0-0.15.a7.12
- maven33 rebuild

* Fri Jan 16 2015 Michal Srb <msrb@redhat.com> - 1.0-0.15.a7.11
- Fix directory ownership

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.15.a7.10
- Rebuild to fix provides

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.0-0.15.a7.9
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.0-0.15.a7.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.15.a7.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.15.a7.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.15.a7.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.15.a7.4
- Remove requires on java

* Mon Feb 17 2014 Michal Srb <msrb@redhat.com> - 1.0-0.15.a7.3
- SCL-ize BR

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.15.a7.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.15.a7.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0-0.15.a7
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.14.a7
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Fri Feb 08 2013 Michal Srb <msrb@redhat.com> - 1.0-0.13.a7
- Remove unnecessary BR on maven-doxia and maven-doxia-sitetools

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0-0.12.a7
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 17 2013 Michal Srb <msrb@redhat.com> - 1.0-0.11.a7
- Build with xmvn

* Thu Nov 22 2012 Jaromir Capik <jcapik@redhat.com> - 1.0-0.10.a7
- Migration to plexus-containers-container-default

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.9.a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.8.a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-0.7.a7
- Rebuild for java 1.6.0 downgrade

* Wed Jul 27 2011 Jaromir Capik <jcapik@redhat.com> - 1.0-0.6.a7
- Removal of plexus-maven-plugin dependency (not needed)
- Minor spec file changes according to the latest guidelines

* Sun Jun 12 2011 Alexander Kurtakov <akurtako@redhat.com> 1.0-0.5.a7
- Build with maven 3.x

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 25 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0-0.3.a7
- Update to alpha 7.
- Apply patch to fix rhbz#621714.
- Use global instead of define.
- Drop ant build - broken after update.

* Wed Aug 26 2009 Andrew Overholt <overholt@redhat.com> 1.0-0.2.a4
- Fix release and defattr
- Make -javadoc description better

* Tue Aug 25 2009 Andrew Overholt <overholt@redhat.com> 1.0-0.1.a4.5
- Remove gcj support
- Fix license tag
- Improve source build instructions
- Remove "excalibur-" prefix from two BRs

* Thu Mar 20 2009 Yong Yang <yyang@redhat.com> 0:1.0-0.1.a4.4
- Build with maven2-2.0.8 built in non-bootstrap mode
- Add some missing BRs

* Thu Mar 20 2009 Yong Yang <yyang@redhat.com> 0:1.0-0.1.a10.3
- Build with maven2 2.0.8

* Tue Jan 20 2009 Yong Yang <yyang@redhat.com> 0:1.0-0.1.a4.2jpp.1
- Import from dbhole's maven 2.0.8 packages
- Merge with JPP-5

* Fri Sep 21 2007 Deepak Bhole <dbhole@redhat.com> 0:1.0-0.1.a4.2jpp.3
- ExcludeArch ppc64

* Tue Mar 20 2007 Deepak Bhole <dbhole@redhat.com> 0:1.0-0.1.a4.2jpp.2
- Enable gcj

* Tue Feb 20 2007 Tania Bento <tbento@redhat.com> 0:1.0-0.1.a4.2jpp.1
- Fixed %%Release.
- Fixed %%BuildRoot.
- Removed %%Vendor.
- Removed %%Distribution.
- Edited instructions on how to generate the source drops.
- Removed %%post and %%postun sections for javadoc.
- Added gcj support.

* Tue Oct 17 2006 Deepak Bhole <dbhole@redhat.com> 1.0-0.a4.2jpp
- Update for maven2 9jpp

* Mon Jun 12 2006 Deepak Bhole <dbhole@redhat.com> - 0:1.0-0.a4.1jpp
- Initial build
