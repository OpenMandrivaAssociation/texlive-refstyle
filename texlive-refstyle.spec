# revision 20318
# category Package
# catalog-ctan /macros/latex/contrib/refstyle
# catalog-date 2010-11-03 15:55:25 +0100
# catalog-license lppl
# catalog-version 0.5
Name:		texlive-refstyle
Version:	0.5
Release:	1
Summary:	Advanced formatting of cross references
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/refstyle
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/refstyle.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/refstyle.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/refstyle.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The refstyle provides a consistent way of producing references
throughout a project. Enough flexibility is provided to make
local changes to a single reference. The user can configure
their own setup. refstyle has a direct interface to varioref,
and namerefs from the nameref package can easily be
incorporated (if needed). For large projects such as a series
of books or a multi volume thesis, written as freestanding
documents, a facility is provided to interface to the xr
package for external document references.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/refstyle/refstyle.cfg
%{_texmfdistdir}/tex/latex/refstyle/refstyle.sty
%doc %{_texmfdistdir}/doc/latex/refstyle/README
%doc %{_texmfdistdir}/doc/latex/refstyle/refconfig.pdf
%doc %{_texmfdistdir}/doc/latex/refstyle/refstyle.pdf
#- source
%doc %{_texmfdistdir}/source/latex/refstyle/refconfig.dtx
%doc %{_texmfdistdir}/source/latex/refstyle/refstyle.dtx
%doc %{_texmfdistdir}/source/latex/refstyle/refstyle.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
