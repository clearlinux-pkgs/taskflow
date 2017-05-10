#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEB6CCA1483FA74EC (infra-root@openstack.org)
#
Name     : taskflow
Version  : 2.11.0
Release  : 48
URL      : http://tarballs.openstack.org/taskflow/taskflow-2.11.0.tar.gz
Source0  : http://tarballs.openstack.org/taskflow/taskflow-2.11.0.tar.gz
Source99 : http://tarballs.openstack.org/taskflow/taskflow-2.11.0.tar.gz.asc
Summary  : Taskflow structured state management library.
Group    : Development/Tools
License  : Apache-2.0
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
Requires: oslo.serialization
Requires: oslo.utils
Requires: oslosphinx
Requires: oslotest
Requires: pbr
Requires: psycopg2
Requires: pydotplus
Requires: python-mock
Requires: redis
Requires: reno
Requires: six
Requires: stevedore
Requires: tenacity
Requires: testscenarios
Requires: testtools
Requires: zake
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tenacity

%description
Please see https://alembic.readthedocs.org/en/latest/index.html for general documentation

%package python
Summary: python components for the taskflow package.
Group: Default

%description python
python components for the taskflow package.


%prep
%setup -q -n taskflow-2.11.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1494444953
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1494444953
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
