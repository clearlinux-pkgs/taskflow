#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : taskflow
Version  : 3.3.1
Release  : 50
URL      : http://tarballs.openstack.org/taskflow/taskflow-3.3.1.tar.gz
Source0  : http://tarballs.openstack.org/taskflow/taskflow-3.3.1.tar.gz
Source99 : http://tarballs.openstack.org/taskflow/taskflow-3.3.1.tar.gz.asc
Summary  : Taskflow structured state management library.
Group    : Development/Tools
License  : Apache-2.0
Requires: taskflow-python3
Requires: taskflow-license
Requires: taskflow-python
Requires: PyMySQL
Requires: SQLAlchemy
Requires: SQLAlchemy-Utils
Requires: Sphinx
Requires: alembic
Requires: automaton
Requires: cachetools
Requires: contextlib2
Requires: debtcollector
Requires: doc8
Requires: enum34
Requires: eventlet
Requires: fasteners
Requires: futures
Requires: futurist
Requires: hacking
Requires: jsonschema
Requires: kazoo
Requires: kombu
Requires: networkx
Requires: openstackdocstheme
Requires: oslo.serialization
Requires: oslo.utils
Requires: oslotest
Requires: pbr
Requires: psycopg2
Requires: pydot
Requires: pydotplus
Requires: python-mock
Requires: redis
Requires: reno
Requires: six
Requires: stestr
Requires: stevedore
Requires: tenacity
Requires: testscenarios
Requires: testtools
Requires: zake
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : tenacity

%description
Team and repository tags
        ========================

%package license
Summary: license components for the taskflow package.
Group: Default

%description license
license components for the taskflow package.


%package python
Summary: python components for the taskflow package.
Group: Default
Requires: taskflow-python3 = %{version}-%{release}

%description python
python components for the taskflow package.


%package python3
Summary: python3 components for the taskflow package.
Group: Default
Requires: python3-core

%description python3
python3 components for the taskflow package.


%prep
%setup -q -n taskflow-3.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1537929583
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/taskflow
cp LICENSE %{buildroot}/usr/share/doc/taskflow/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/taskflow/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
