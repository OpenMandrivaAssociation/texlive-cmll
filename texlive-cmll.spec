%global tl_name cmll
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Symbols for linear logic
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cmll
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmll.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmll.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmll.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a very small font set that contain some symbols useful in linear
logic, which are apparently not available elsewhere. Variants are
included for use with Computer Modern serif and sans-serif and with the
AMS Euler series. The font is provided both as Metafont source, and in
Adobe Type 1 format. LaTeX support is provided.

