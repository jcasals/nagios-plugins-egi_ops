Nagios Plugin for EGI OPS
=========================

### Overview
This is a Nagios plugin to check EGI OPS Test in the new ARGO platform.

This check uses the information from the ARGO API and parses it and prints out the status of the service with detailed views for every host and links to the hosts that have Warning or Critical status.

### Authors
Jordi Casals ([PIC](http://www.pic.es)).

Contact: jcasals@pic.es

### Changelog
*Mon Apr 10 2017*<br>
**1.1.0** Modified main script to make it work with new ARGO output.<br>
*Fri Mar 18 2016*<br>
**1.0.0** First Release!

### Requirements
It consists on a Bash script and the only requirement is to have [JQ](http://stedolan.github.io/jq/) package installed, a simple and flexible JSON processor for bash.

### Installation
You just have to install it via RPM and, if you don't have JQ on your server, it will install it as requirement.
```
$ yum install nagios-plugins-egi_ops
```

### Usage
```
$ /usr/lib64/nagios/plugins/check_egi_ops -s <site> -x <service1[,service2,...]> -r <report>
```
As you can see it has four parameters. 
- Site (-s), service(s) (-x) and report type (-r).

You can see an example of how it works by running it on your command line:
```
[user@host ]# /usr/lib64/nagios/plugins/check_egi_ops -s pic -x CREAM-CE,SRMv2 -r Critical
CREAM-CE: OK // SRMv2: OK

HOSTS
======
CREAM-CE
ce11.pic.es: OK
ce10.pic.es: OK
ce09.pic.es: OK
ce08.pic.es: OK
ce07.pic.es: OK

SRMv2
srmlhcb.pic.es: OK
srmcms.pic.es: OK
srmatlas.pic.es: OK
srm.pic.es: OK
```

### Setup for Nagios
To add the plugin to your Nagios System you just have to create a command as you usually do with other plugins. A sample of command line input on the NagiosQL setup can be:
```
$USER1$/check_lcgsam -v $ARG1$ -p $ARG2$ -s $ARG3$ -f $ARG4$
```
Or if you prefer, you can create this command on your *commands.cfg* file:
```
define command {
    command_name    check_lcgsam
    command_line    $USER1$/check_lcgsam -v $ARG1$ -p $ARG2$ -s $ARG3$ -f $ARG4$
}
```

#### Optional Setup for Nagios
We tried to add a little more information to the Nagios output, so we wanted to add links that points out to the errors, in case it was an error. We found there are some characters not admitted, and that the HTML is disabled in the output. 

To change this you have to modify two files.

***/usr/local/nagios/etc/cgi.cfg*** *or your equivalent cgi.cfg (icinga, thruk, etc)*
```
# escape_html_tags=1
escape_html_tags=0
```
***/usr/local/nagios/etc/nagios.cfg*** *or your equivalent nagios.cfg or icinga.cfg*
```
# illegal_object_name_chars=`~!$%^&*|'"<>?,()=
illegal_object_name_chars=`~!$%^&*|'"?,()=
```

