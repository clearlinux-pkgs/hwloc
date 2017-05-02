#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hwloc
Version  : 1.11.3
Release  : 7
URL      : https://www.open-mpi.org/software/hwloc/v1.11/downloads/hwloc-1.11.3.tar.gz
Source0  : https://www.open-mpi.org/software/hwloc/v1.11/downloads/hwloc-1.11.3.tar.gz
Summary  : Hardware locality detection and management library
Group    : Development/Tools
License  : BSD-3-Clause Intel
Requires: hwloc-bin
Requires: hwloc-lib
Requires: hwloc-data
Requires: hwloc-doc
BuildRequires : cairo-dev
BuildRequires : doxygen
BuildRequires : libpciaccess-dev
BuildRequires : libxml2-dev
BuildRequires : ncurses-dev
BuildRequires : numactl-dev
BuildRequires : pciutils-dev
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(x11)
BuildRequires : systemd-dev

%description
Introduction
hwloc provides command line tools and a C API to obtain the hierarchical map of
key computing elements, such as: NUMA memory nodes, shared caches, processor
packages, processor cores, processing units (logical processors or "threads")
and even I/O devices. hwloc also gathers various attributes such as cache and
memory information, and is portable across a variety of different operating
systems and platforms. Additionally it may assemble the topologies of multiple
machines into a single one so as to let applications consult the topology of an
entire fabric or cluster at once.

%package bin
Summary: bin components for the hwloc package.
Group: Binaries
Requires: hwloc-data

%description bin
bin components for the hwloc package.


%package data
Summary: data components for the hwloc package.
Group: Data

%description data
data components for the hwloc package.


%package dev
Summary: dev components for the hwloc package.
Group: Development
Requires: hwloc-lib
Requires: hwloc-bin
Requires: hwloc-data
Provides: hwloc-devel

%description dev
dev components for the hwloc package.


%package doc
Summary: doc components for the hwloc package.
Group: Documentation

%description doc
doc components for the hwloc package.


%package lib
Summary: lib components for the hwloc package.
Group: Libraries
Requires: hwloc-data

%description lib
lib components for the hwloc package.


%prep
%setup -q -n hwloc-1.11.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1493487099
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1493487099
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hwloc-annotate
/usr/bin/hwloc-assembler
/usr/bin/hwloc-assembler-remote
/usr/bin/hwloc-bind
/usr/bin/hwloc-calc
/usr/bin/hwloc-compress-dir
/usr/bin/hwloc-diff
/usr/bin/hwloc-distances
/usr/bin/hwloc-distrib
/usr/bin/hwloc-dump-hwdata
/usr/bin/hwloc-gather-topology
/usr/bin/hwloc-info
/usr/bin/hwloc-ls
/usr/bin/hwloc-patch
/usr/bin/hwloc-ps
/usr/bin/lstopo
/usr/bin/lstopo-no-graphics

%files data
%defattr(-,root,root,-)
/usr/share/applications/lstopo.desktop
/usr/share/hwloc/hwloc-dump-hwdata.service
/usr/share/hwloc/hwloc-valgrind.supp
/usr/share/hwloc/hwloc.dtd

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/hwloc/autogen/config.h
/usr/include/hwloc/bitmap.h
/usr/include/hwloc/cuda.h
/usr/include/hwloc/cudart.h
/usr/include/hwloc/deprecated.h
/usr/include/hwloc/diff.h
/usr/include/hwloc/gl.h
/usr/include/hwloc/glibc-sched.h
/usr/include/hwloc/helper.h
/usr/include/hwloc/inlines.h
/usr/include/hwloc/intel-mic.h
/usr/include/hwloc/linux-libnuma.h
/usr/include/hwloc/linux.h
/usr/include/hwloc/myriexpress.h
/usr/include/hwloc/nvml.h
/usr/include/hwloc/opencl.h
/usr/include/hwloc/openfabrics-verbs.h
/usr/include/hwloc/plugins.h
/usr/include/hwloc/rename.h
/usr/lib64/libhwloc.so
/usr/lib64/pkgconfig/hwloc.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/hwloc/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man7/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libhwloc.so.5
/usr/lib64/libhwloc.so.5.7.0
