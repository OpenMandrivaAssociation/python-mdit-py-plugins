Summary:	A collection of plugins for markdown-it-py
Name:		mdit-py-plugins
Version:	0.3.3
Release:	2
Group:		Development/Python
License:	MIT
URL:		https://github.com/executablebooks/mdit-py-plugins
#Source0:	https://github.com/executablebooks/mdit-py-plugins/archive/%{version}/mdit-py-plugins-%{version}.tar.gz
Source0:	https://pypi.io/packages/source/m/mdit-py-plugins/mdit-py-plugins-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(wheel)

BuildArch:	noarch

%description
Collection of core plugins for markdown-it-py.

%files
%license LICENSE
%doc README.md
%{py_sitedir}/mdit_py_plugins
%{py_sitedir}/mdit_py_plugins-*.*-info

#--------------------------------------------------------------------

%prep
%autosetup -n mdit-py-plugins-%{version}

%build
%py_build
 
%install
%py_install

