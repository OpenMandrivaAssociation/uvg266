%define libname %mklibname uvg266
%define devname %mklibname -d uvg266

Name:           uvg266
Version:        0.8.1
Release:        1
Summary:        An open-source VVC encoder based on Kvazaar 
License:        BSD-3-Clause
URL:            https://github.com/ultravideo/uvg266
Source0:        https://github.com/ultravideo/uvg266/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake

%description
uvg266 is a VVC encoder that is based on our Kvazaar. The development of uvg266 started in 2018 by starting to convert the CABAC and intra prediction of Kvazaar to VVC. 
Originally only the planar, DC, and 33 angular modes from VVC were supported. Though that was quickly extended to the full 65 intra modes included in VVC.
The development work continued by adding support for the rest of the tools included in HEVC that were copied to VVC. 
The focus was put on intra tools with the intention of implementing all of the intra VVC tools before statring to implement the inter tools. 
Currently, uvg266 supports all of the intra tools included in VVC; intra sub partition (ISP), cross-component linear model (CCLM), 
multi reference line (MRL), matrix intra prediction (MIP), multiple transform selection (MTS), low-frequence non-separable transform (LFNST), 
adaptive loop filter (ALF), and intra block copy (IBC). Additionally, uvg266 supports dual tree and multi type tree (MTT) for intra slices.

In the future we plan on developping methods to reduce the massive complexity of the VVC encoder and start working on the inter tools. 
The goal is to have a fully functional VVC encoder that is fast and efficient.

%prep
%autosetup -p1

%build
export CC=gcc
export CXX=g++
%cmake \
       -DBUILD_SHARED_LIBS=ON \
       -DBUILD_TESTS=OFF \
       -DUVG_DEFAULT_BUILD_TYPE="Release"
       
%make_build

%install
%make_install -C build

%files
