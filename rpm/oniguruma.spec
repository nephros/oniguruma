# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       oniguruma

# >> macros
# << macros
%define short_name onig

Summary:    A modern and flexible regular expressions library
Version:    6.9.7.1
Release:    1
Group:      Development/Libraries
License:    BSD
URL:        https://github.com/kkos/oniguruma
Source0:    %{short_name}-%{version}.tar.gz
Source100:  oniguruma.yaml
BuildRequires:  cmake

%description
%{summary}.

%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name}-libs = %{version}

%description devel
%{summary}.

%package libs
Summary:    A modern and flexible regular expressions library
Group:      Development/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description libs
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig


%files devel
%defattr(-,root,root,-)
%{_bindir}/onig-config
%{_includedir}/oniggnu.h
%{_includedir}/oniguruma.h
%{_libdir}/libonig.so
%{_libdir}/pkgconfig/oniguruma.pc
# >> files devel
# << files devel

%files libs
%defattr(-,root,root,-)
%{_libdir}/libonig.so.*
# >> files libs
# << files libs
