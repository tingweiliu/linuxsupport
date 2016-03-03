Summary: Hitv support utils
Name: hitvsupport
Version: 2.0
Release: CentOS7
Source: hitvsupport.tar.gz
License: GPL
Requires: iotop
Packager: Tony
Group: Application
URL: http://www.hisense.com
Buildroot:/usr/src/packages/BUILDROOT/supportutils
Vendor: Hisense Electric co.,ltd
Distribution: CentOS 7.1

%description 
Cpu utils:
	mpstat: Multi processor status
	perf: Kernel and User func status
	likwid-topology: Cpu physical topology

Disk utils:
	dstat: Disk status
	iostat: Disk status
	fio: Disk benchmark
	iotop: Disk usage per process

Network utils:
	udpsendutil: Udp packets send util
	iftop: Network bandwith usage(backport from iftop-0.17)
	netperf/netserver: Network benchmark
	tcputilclient/tcputilserver: Tcp packets send and receive util

Memeory utils:
	vmtouch: Pagecache util

Benchmark utils:
	fio: Disk benchmark
	benchmark: System benchmark
	ramsmp: Memory and cache benchmark
	netperf/netserver: Network benchmark

Security utils:
	rootkitcheck: Rootkit check(rkhunter,chkrootkit)
	unhide-linux: Check hidden processes
	unhide-tcp: Check hidden port
	z-m-e-u-check: zmeu trojan horse attack

Bottleneck utils:
	gethighprocess: Get the highest utilization processes
	perf: Get the highest utilization function
	processperf: Use perf and FlameGraph analyse program function utilization(https://github.com/brendangregg/FlameGraph)

Debug utils:
	processlimit: Change running process limits (core file size, open files, ...)
	generatedebuginfo: Split program with it's debug information for security
	snapshot: Dump the process to file for debug, while keep program running

Other utils:
	parseseconds: Make dmesg seconds to readable format
	supportutils: Collect System Informations for support or analysis
	nmon: Monitor system memory

Documents:
	fio_test: fio benchmark conf demo
	fio_HOWTO: fio HOWTO

Author:
-------
	Tony <tingw.liu@gmail.com>
	http://forever.blog.chinaunix.net

%prep
%setup -c

%build
gcc -o debug/processlimit debug/processlimits.c
gcc -o performance/nmon performance/lmon14a.c -D LARGEMEM -lcurses

#tcpsendutil
cd network/tcpsendutil/
make
cd -

#

%install
mkdir -p  ${RPM_BUILD_ROOT}/usr/local/share/hitv
mkdir -p  ${RPM_BUILD_ROOT}/var/lib/rkhunter
mkdir -p  ${RPM_BUILD_ROOT}/usr/local/lib64/rkhunter
mkdir -p  ${RPM_BUILD_ROOT}/usr/local/bin
mkdir -p  ${RPM_BUILD_ROOT}/etc
mkdir -p  ${RPM_BUILD_ROOT}/var/lib/


install -m 755 performance/perfscript/processperf ${RPM_BUILD_ROOT}/usr/local/bin/processperf
install -m 755 performance/perfscript/flamegraph.pl ${RPM_BUILD_ROOT}/usr/local/bin/flamegraph.pl
install -m 755 performance/perfscript/stackcollapse-perf.pl ${RPM_BUILD_ROOT}/usr/local/bin/stackcollapse-perf.pl

install -m 755 performance/nmon ${RPM_BUILD_ROOT}/usr/local/bin/nmon

install -m 755 network/tcpsendutil/tcputilclient ${RPM_BUILD_ROOT}/usr/local/bin/tcputilclient
install -m 755 network/tcpsendutil/tcputilserver ${RPM_BUILD_ROOT}/usr/local/bin/tcputilserver

install -m 755 debug/generatedebuginfo ${RPM_BUILD_ROOT}/usr/local/bin/generatedebuginfo
install -m 755 debug/processlimit ${RPM_BUILD_ROOT}/usr/local/bin/processlimit
install -m 755 debug/gdb ${RPM_BUILD_ROOT}/usr/local/bin/gdb
install -m 755 debug/snapshot ${RPM_BUILD_ROOT}/usr/local/bin/snapshot

install -m 755 others/parseseconds ${RPM_BUILD_ROOT}/usr/local/bin/parseseconds
install -m 755 performance/netperf ${RPM_BUILD_ROOT}/usr/local/bin/netperf
install -m 755 performance/netserver ${RPM_BUILD_ROOT}/usr/local/bin/netserver
install -m 755 others/supportutils  ${RPM_BUILD_ROOT}/usr/local/bin/supportutils
install -m 755 disk/dstat  ${RPM_BUILD_ROOT}/usr/local/bin/dstat
install -m 755 cpu/perf  ${RPM_BUILD_ROOT}/usr/local/bin/perf
install -m 755 network/udpsendutil  ${RPM_BUILD_ROOT}/usr/local/bin/udpsendutil
install -m 755 memory/vmtouch  ${RPM_BUILD_ROOT}/usr/local/bin/vmtouch
install -m 755 disk/iostat  ${RPM_BUILD_ROOT}/usr/local/bin/iostat
install -m 755 cpu/mpstat  ${RPM_BUILD_ROOT}/usr/local/bin/mpstat
install -m 755 disk/fio  ${RPM_BUILD_ROOT}/usr/local/bin/fio
install -m 755 performance/benchmark  ${RPM_BUILD_ROOT}/usr/local/bin/benchmark
install -m 755 performance/ramsmp  ${RPM_BUILD_ROOT}/usr/local/bin/ramsmp
install -m 755 disk/fio_test  ${RPM_BUILD_ROOT}/usr/local/share/hitv/fio_test
install -m 755 disk/fio_HOWTO  ${RPM_BUILD_ROOT}/usr/local/share/hitv/fio_HOWTO
install -m 755 cpu/likwid-topology  ${RPM_BUILD_ROOT}/usr/local/bin/likwid-topology
install -m 755 security/rootkitcheck  ${RPM_BUILD_ROOT}/usr/local/bin/rootkitcheck
install -m 755 security/z-m-e-u-check  ${RPM_BUILD_ROOT}/usr/local/bin/z-m-e-u-check
install -m 755 security/unhide-linux  ${RPM_BUILD_ROOT}/usr/local/bin/unhide-linux
install -m 755 security/unhide-tcp  ${RPM_BUILD_ROOT}/usr/local/bin/unhide-tcp
install -m 755 performance/gethighprocess  ${RPM_BUILD_ROOT}/usr/local/bin/gethighprocess
cp -ar performance/lmbench3   ${RPM_BUILD_ROOT}/usr/local/bin/lmbench3
cp -ar security/rkhunter_install/usr/local/bin/rkhunter  ${RPM_BUILD_ROOT}/usr/local/bin/rkhunter
cp -ar security/rkhunter_install/etc/rkhunter.conf  ${RPM_BUILD_ROOT}/etc/rkhunter.conf
cp -ar security/rkhunter_install/var/lib/rkhunter/db  ${RPM_BUILD_ROOT}/var/lib/rkhunter/db
cp -ar security/rkhunter_install/var/lib/rkhunter/tmp  ${RPM_BUILD_ROOT}/var/lib/rkhunter/tmp
cp -ar security/rkhunter_install/usr/local/lib64/rkhunter/scripts  ${RPM_BUILD_ROOT}/usr/local/lib64/rkhunter/scripts
cp -ar security/chkrootkit-0.49  ${RPM_BUILD_ROOT}/usr/local/bin/chkrootkit-0.49

#Next for backport iftop
mkdir -p  ${RPM_BUILD_ROOT}/usr/share/man/man8/
mkdir -p  ${RPM_BUILD_ROOT}/usr/share/man/man1/
cp -ar network/iftop.8.gz  ${RPM_BUILD_ROOT}/usr/share/man/man8/iftop.8.gz
install -m 755 network/iftop  ${RPM_BUILD_ROOT}/usr/local/bin/iftop




%clean
rm -rf ${RPM_BUILD_DIR}/*
rm -rf ${RPM_BUILD_ROOT}
%files
/usr/local/bin/processlimit
/usr/local/bin/generatedebuginfo
/usr/local/bin/snapshot
/usr/local/bin/gdb

/usr/local/bin/netperf
/usr/local/bin/netserver

/usr/local/bin/parseseconds

/usr/local/bin/dstat

/usr/local/bin/supportutils

/usr/local/bin/perf


/usr/local/bin/udpsendutil

/usr/local/bin/vmtouch


/usr/local/bin/likwid-topology

/usr/local/bin/iostat

/usr/local/bin/mpstat

/usr/local/bin/lmbench3
/usr/local/bin/benchmark

/usr/local/bin/ramsmp

/usr/local/bin/fio
/usr/local/share/hitv/fio_test
/usr/local/share/hitv/fio_HOWTO

/usr/local/bin/rkhunter
/usr/local/bin/rootkitcheck
/usr/local/bin/z-m-e-u-check
/var/lib/rkhunter
/usr/local/lib64/rkhunter
/etc/rkhunter.conf
/usr/local/bin/chkrootkit-0.49
/usr/local/bin/unhide-linux
/usr/local/bin/unhide-tcp

/usr/local/bin/gethighprocess

/usr/local/bin/nmon
#Next for iftop
/usr/local/bin/iftop
/usr/share/man/man8/iftop.8.gz




/usr/local/bin/tcputilclient
/usr/local/bin/tcputilserver


/usr/local/bin/processperf
/usr/local/bin/flamegraph.pl
/usr/local/bin/stackcollapse-perf.pl
%changelog


* Wed Dec 16 2015 tingw.liu@gmail.com
-Remove iotop from code, requires iotop
-Add nmon
* Tue Sep 16 2014 tingw.liu@gmail.com
-Add ramsmp for memory and cache benchmark
* Wed Apr 23 2014 tingw.liu@gmail.com
-Add snapshot to dump process memory to file for gdb debug.(Keep program running...)
* Mon Oct 21 2013 tingw.liu@gmail.com
-Add processperf for analysis function performance
* Wed Oct 10 2013 tingw.liu@gmail.com
-Add tcputilclient and tcputilserver
* Wed Oct 9 2013 tingw.liu@gmail.com
-Add processlimit debug util
-Add generatedebuginfo debug util
* Fri Aug 23 2013 tingw.liu@gmail.com
-Add netperf/netserver network benchmark util 
* Thu Aug 15 2013 tingw.liu@gmail.com
-Add zmeu attack check
* Tue Jul 23 2013 tingw.liu@gmail.com
-Add parseseconds utils to make dmesg time readable
* Mon Jul  1 2013 tingw.liu@gmail.com
-Add maxprocesstime support
-Add Qdisc level skb drop check
* Tue Mar 26 2013 tingw.liu@gmail.com
-Add iotop, disk usage tool
-Add iftop, network bandwidth usage tool
-Add python-curses, used by iotop
* Wed Mar 6 2013 tingw.liu@gmail.com
-Add "rootkitcheck",linux kernel rootkit check tool
-Change supportutils, add to  gathering security information
-Change "udpsendutil", support broadcast address
-Add "unhide-linux",Find hidden process on linux
-Add "unhide-tcp",Find hidden socket
* Tue Jan 29 2013 tingw.liu@gmail.com <0.89>
-Change supportutils, Doesn't gathering iptables nat table. Because iptables -t nat -L will install conntrack module with nf_conntrack_max, maybe result in can't create new connection with connection table full
-Add "hostscan,udpsendutil,nbtscan" network tools
-Add "vmtouch" pagecache manage tool
-Add "perf,benchmark,fio performance" stat tools
-Add "likwid-topology" physical topology tool
* Mon Dec 24 2012 tingw.liu@gmail.com <0.88>
-Initial version for gathering system status
