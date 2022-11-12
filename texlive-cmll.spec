Name:		texlive-cmll
Version:	17964
Release:	1
Summary:	Symbols for linear logic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/cmll
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmll.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmll.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmll.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a very small font set that contain some symbols useful
in linear logic, which are apparently not available elsewhere.
Variants are included for use with Computer Modern serif and
sans-serif and with the AMS Euler series. The font is provided
both as MetaFont source, and in Adobe Type 1 format. LaTeX
support is provided. format.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/cmll/cmll.map
%{_texmfdistdir}/fonts/source/public/cmll/cmllbx10.mf
%{_texmfdistdir}/fonts/source/public/cmll/cmllbx12.mf
%{_texmfdistdir}/fonts/source/public/cmll/cmllbx5.mf
%{_texmfdistdir}/fonts/source/public/cmll/cmllbx6.mf
%{_texmfdistdir}/fonts/source/public/cmll/cmllbx7.mf
%{_texmfdistdir}/fonts/source/public/cmll/cmllbx8.mf
%{_texmfdistdir}/fonts/source/public/cmll/cmllbx9.mf
%{_texmfdistdir}/fonts/source/public/cmll/cmllr10.mf
%{_texmfdistdir}/fonts/source/public/cmll/cmllr12.mf
%{_texmfdistdir}/fonts/source/public/cmll/cmllr17.mf
%{_texmfdistdir}/fonts/source/public/cmll/cmllr5.mf
%{_texmfdistdir}/fonts/source/public/cmll/cmllr6.mf
%{_texmfdistdir}/fonts/source/public/cmll/cmllr7.mf
%{_texmfdistdir}/fonts/source/public/cmll/cmllr8.mf
%{_texmfdistdir}/fonts/source/public/cmll/cmllr9.mf
%{_texmfdistdir}/fonts/source/public/cmll/cmllss10.mf
%{_texmfdistdir}/fonts/source/public/cmll/cmllss12.mf
%{_texmfdistdir}/fonts/source/public/cmll/cmllss17.mf
%{_texmfdistdir}/fonts/source/public/cmll/cmllss8.mf
%{_texmfdistdir}/fonts/source/public/cmll/cmllss9.mf
%{_texmfdistdir}/fonts/source/public/cmll/cmllssbx10.mf
%{_texmfdistdir}/fonts/source/public/cmll/eullbx10.mf
%{_texmfdistdir}/fonts/source/public/cmll/eullbx5.mf
%{_texmfdistdir}/fonts/source/public/cmll/eullbx6.mf
%{_texmfdistdir}/fonts/source/public/cmll/eullbx7.mf
%{_texmfdistdir}/fonts/source/public/cmll/eullbx8.mf
%{_texmfdistdir}/fonts/source/public/cmll/eullbx9.mf
%{_texmfdistdir}/fonts/source/public/cmll/eullr10.mf
%{_texmfdistdir}/fonts/source/public/cmll/eullr5.mf
%{_texmfdistdir}/fonts/source/public/cmll/eullr6.mf
%{_texmfdistdir}/fonts/source/public/cmll/eullr7.mf
%{_texmfdistdir}/fonts/source/public/cmll/eullr8.mf
%{_texmfdistdir}/fonts/source/public/cmll/eullr9.mf
%{_texmfdistdir}/fonts/source/public/cmll/llcommon.mf
%{_texmfdistdir}/fonts/source/public/cmll/lleusym.mf
%{_texmfdistdir}/fonts/source/public/cmll/llsymbols.mf
%{_texmfdistdir}/fonts/tfm/public/cmll/cmllbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/cmllbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/cmllbx5.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/cmllbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/cmllbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/cmllbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/cmllbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/cmllr10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/cmllr12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/cmllr17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/cmllr5.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/cmllr6.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/cmllr7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/cmllr8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/cmllr9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/cmllss10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/cmllss12.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/cmllss17.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/cmllss8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/cmllss9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/cmllssbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/eullbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/eullbx5.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/eullbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/eullbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/eullbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/eullbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/eullr10.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/eullr5.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/eullr6.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/eullr7.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/eullr8.tfm
%{_texmfdistdir}/fonts/tfm/public/cmll/eullr9.tfm
%{_texmfdistdir}/fonts/type1/public/cmll/cmllbx10.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/cmllbx12.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/cmllbx5.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/cmllbx6.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/cmllbx7.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/cmllbx8.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/cmllbx9.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/cmllr10.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/cmllr12.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/cmllr17.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/cmllr5.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/cmllr6.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/cmllr7.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/cmllr8.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/cmllr9.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/cmllss10.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/cmllss12.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/cmllss17.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/cmllss8.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/cmllss9.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/cmllssbx10.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/eullbx10.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/eullbx5.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/eullbx6.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/eullbx7.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/eullbx8.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/eullbx9.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/eullr10.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/eullr5.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/eullr6.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/eullr7.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/eullr8.pfb
%{_texmfdistdir}/fonts/type1/public/cmll/eullr9.pfb
%{_texmfdistdir}/tex/latex/cmll/cmll.sty
%{_texmfdistdir}/tex/latex/cmll/ucmllr.fd
%{_texmfdistdir}/tex/latex/cmll/ucmllss.fd
%{_texmfdistdir}/tex/latex/cmll/ueull.fd
%doc %{_texmfdistdir}/doc/fonts/cmll/README
%doc %{_texmfdistdir}/doc/fonts/cmll/cmll.pdf
#- source
%doc %{_texmfdistdir}/source/latex/cmll/cmll.dtx
%doc %{_texmfdistdir}/source/latex/cmll/cmll.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
