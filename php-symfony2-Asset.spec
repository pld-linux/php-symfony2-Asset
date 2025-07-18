%define		package	Asset
%define		php_min_version 5.3.9
Summary:	Symfony2 Asset Component
Name:		php-symfony2-%{package}
Version:	2.8.52
Release:	2
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	918417574f26e7e618cdc5d1d2a1ca82
Patch0:		https://github.com/symfony/asset/compare/2.8...glensc:2.8.patch?/JsonManifestVersionStrategy.patch
# Patch0-md5:	23bffda6937a66550e73e24320c8fd46
URL:		https://symfony.com/doc/2.8/components/asset.html
BuildRequires:	phpab
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(hash)
Requires:	php(spl)
Requires:	php-dirs >= 1.6
Suggests:	php-symfony2-HttpFoundation
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Asset component manages URL generation and versioning of web
assets such as CSS stylesheets, JavaScript files and image files.

%prep
%setup -q -n asset-%{version}
%patch -P0 -p1

%build
phpab -n -e '*/Tests/*' -o autoloader.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%{php_data_dir}/Symfony/Component/Asset
