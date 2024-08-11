Name:           dhewm3
Version:        1.5.4
Release:        1
Summary:        DOOM 3 source port
Group:          Games/FPS
License:        GPL-3.0-only
URL:            https://github.com/dhewm/dhewm3
Source0:        https://github.com/dhewm/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  cmake(sdl2)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(zlib)

%description
dhewm3 is a DOOM 3 GPL source port.
Unlike the original DOOM 3, dhewm3 uses:

- SDL for low level OS support, OpenGL and input handling
- OpenAL for audio output, all OS specific audio backends are gone
- OpenAL EFX for EAX reverb effects
- Better support for widescreen (and arbitrary display resolutions)

%prep
%autosetup -p1
%build
cd neo
%cmake -DREPRODUCIBLE_BUILD=ON ..
%make_build

%install
cd neo
%make_install -C build

%files
%doc README.md
%license COPYING.txt
%{_bindir}/%{name}
%{_libdir}/%{name}
