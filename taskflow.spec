#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : taskflow
Version  : 1.28.0
Release  : 29
URL      : http://tarballs.openstack.org/taskflow/taskflow-1.28.0.tar.gz
Source0  : http://tarballs.openstack.org/taskflow/taskflow-1.28.0.tar.gz
Summary  : Taskflow structured state management library.
Group    : Development/Tools
License  : Apache-2.0
Requires: taskflow-python
BuildRequires : Babel-python
BuildRequires : Jinja2
BuildRequires : Mako-python
BuildRequires : MarkupSafe-python
BuildRequires : Pygments
BuildRequires : SQLAlchemy-Utils-python
BuildRequires : SQLAlchemy-python
BuildRequires : Sphinx-python
BuildRequires : alembic-python
BuildRequires : amqp-python
BuildRequires : anyjson-python
BuildRequires : automaton-python
BuildRequires : cachetools-python
BuildRequires : decorator-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : enum34-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fasteners-python
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : futures-python
BuildRequires : futurist-python
BuildRequires : hacking
BuildRequires : iso8601-python
BuildRequires : jsonschema-python
BuildRequires : kazoo-python
BuildRequires : kombu-python
BuildRequires : linecache2-python
BuildRequires : mccabe-python
BuildRequires : mox3-python
BuildRequires : msgpack-python-python
BuildRequires : netaddr
BuildRequires : netifaces-python
BuildRequires : networkx-python
BuildRequires : ordereddict-python
BuildRequires : oslo.i18n-python
BuildRequires : oslo.serialization-python
BuildRequires : oslo.utils-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : psycopg2-python
BuildRequires : py-python
BuildRequires : pyflakes-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : redis-python
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : stevedore
BuildRequires : taskflow
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv
BuildRequires : zake-python

%description
Please see https://alembic.readthedocs.org/en/latest/index.html for general documentation

%package python
Summary: python components for the taskflow package.
Group: Default
Requires: automaton-python
Requires: cachetools-python
Requires: enum34-python
Requires: fasteners-python
Requires: futures-python
Requires: futurist-python
Requires: jsonschema-python
Requires: networkx-python
Requires: oslo.serialization-python
Requires: oslo.utils-python
Requires: six-python
Requires: stevedore

%description python
python components for the taskflow package.


%prep
%setup -q -n taskflow-1.28.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
