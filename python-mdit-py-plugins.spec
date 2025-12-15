Summary:	A collection of plugins for markdown-it-py
Name:		mdit-py-plugins
Version:	0.5.0
Release:	1
Group:		Development/Python
License:	MIT
URL:		https://github.com/executablebooks/mdit-py-plugins
#Source0:	https://github.com/executablebooks/mdit-py-plugins/archive/%{version}/mdit-py-plugins-%{version}.tar.gz
Source0:	https://pypi.io/packages/source/m/mdit-py-plugins/mdit_py_plugins-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

BuildArch:	noarch

%description
Collection of core plugins for markdown-it-py.

%files
%license LICENSE
%doc README.md
%{py_sitedir}/mdit_py_plugins
%{py_sitedir}/mdit_py_plugins-*.*-info
