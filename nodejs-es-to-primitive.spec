%{?nodejs_find_provides_and_requires}
Name:                nodejs-es-to-primitive
Version:             1.2.0
Release:             2
Summary:             ECMAScript “ToPrimitive” algorithm
License:             MIT
URL:                 https://github.com/ljharb/es-to-primitive
Source0:             https://registry.npmjs.org/es-to-primitive/-/es-to-primitive-%{version}.tgz
Patch0:              nodejs-es-to-primitive-fpn.patch
BuildArch:           noarch
ExclusiveArch:       %{nodejs_arches} noarch
BuildRequires:       nodejs-packaging
BuildRequires:       npm(foreach) npm(is-callable) npm(is-date-object) npm(is-symbol) npm(object-is)
BuildRequires:       npm(tape)
%description
ECMAScript “ToPrimitive” algorithm. Provides ES5 and ES6 versions. When
different versions of the spec conflict, the default export will be the
latest version of the abstract operation. Alternative versions will also
be available under an es5/es6/es7 exported property if you require a
specific version.

%prep
%autosetup -p 1 -n package
%nodejs_fixdep is-symbol "^1.0.1"
rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/es-to-primitive
cp -pr package.json index.js es5.js es6.js es2015.js helpers %{buildroot}%{nodejs_sitelib}/es-to-primitive
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} --harmony --es-staging test/index.js

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/es-to-primitive

%changelog
* Thu 26 Nov 2020 leiju <leiju4@huawei.com> - 1.2.0-2
- delete nodejs-es-to-primitive.spec.old redundancy file

* Tue Aug 18 2020 Anan Fu <fuanan3@huawei.com> - 1.2.0-1
- package init
