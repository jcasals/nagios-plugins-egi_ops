Name:       nagios-plugins-egi_ops
Version:    1.0.0
Release:    1%{?dist}
Summary:    EGI OPS Service Availability Monitoring

Group:      System/Monitoring
License:    GPLv2+
URL:        https://github.com/jcasals/
# Source0:  %{name}-%{version}-%{release}.tar.gz
Source0:    %{name}.tar.gz
# BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRoot:  %{_tmppath}/%{name}

Requires:   jq

%description
nagios-plugins-egi_ops is a generic plugin that checks EGI OPS Services Availability Monitoring

%prep
# %setup -q -n %{name}-%{version}-%{release}
%setup -q -n %{name}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/lib64/nagios/plugins
cp ./usr/lib64/nagios/plugins/check_egi_ops %{buildroot}/usr/lib64/nagios/plugins/check_egi_ops

%post
echo "===================================================="
echo ""
echo "Plugin installed succesfully!"
echo ""
echo "Please, take a look at the requirements in"
echo "the documentation to set up the plugin at:"
echo "http://jcasals.github.io/nagios-plugins-egi_ops"
echo ""
echo "Thank you and enjoy this plugin as much as we do :D"
echo ""
echo "===================================================="

%clean
rm -rf %{buildroot}

%files
%attr(0755, root,root) /usr/lib64/nagios/plugins/check_egi_ops
%defattr(-,root,root,-)
%doc

%changelog
* Fri Mar 18 2016 Jordi Casals <jcasals@pic.es> 1.0.0
- First Release!
