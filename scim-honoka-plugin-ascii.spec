%define version  0.9.1
%define release  %mkrel 2
%define src_name honoka-plugin-ascii

%define honoka_version   0.9.0

Name:       scim-honoka-plugin-ascii
Summary:    An ASCII input plugin for honoka
Version:    %{version}
Release:    %{release}
Group:      System/Internationalization
License:    GPL
URL:        http://nop.net-p.org/modules/pukiwiki/index.php?%5B%5Bhonoka%5D%5D
Source0:    http://nop.net-p.org/files/honoka/%{src_name}-%{version}.tar.bz2
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: scim-honoka-devel >= %{honoka_version}
BuildRequires: automake
BuildRequires: libltdl-devel

%description
An ASCII input plugin for honoka.

%prep
%setup -q -n %{src_name}-%{version}

%build
# force to regenerate configure
./bootstrap
%configure2_5x
# (tv) parallel build is broken:
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove devel files
rm -f $RPM_BUILD_ROOT/%{scim_plugins_dir}/honoka/*.{a,la}

%find_lang honoka-plugin-ascii

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f honoka-plugin-ascii.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README.jp
%{scim_plugins_dir}/honoka/*.so
