Name:		texlive-refstyle
Version:	69680
Release:	1
Summary:	Advanced formatting of cross references
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/refstyle
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/refstyle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/refstyle.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/refstyle.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

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

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
