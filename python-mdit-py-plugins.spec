%define module mdit-py-plugins
%define oname mdit_py_plugins

Name:		python-mdit-py-plugins
Summary:	A collection of plugins for markdown-it-py
Version:	0.6.1
Release:	1
Group:		Development/Python
License:	MIT
URL:		https://github.com/executablebooks/mdit-py-plugins
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz
# rename the package to match the repo
%rename mdit-py-plugins

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(wheel)

%description
Collection of core plugins for markdown-it-py.

%files
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
