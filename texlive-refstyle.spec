%global tl_name refstyle
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6b
Release:	%{tl_revision}.1
Summary:	Advanced formatting of cross references
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/refstyle
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/refstyle.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/refstyle.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/refstyle.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a consistent way of producing references throughout
a project. Enough flexibility is provided to make local changes to a
single reference. The user can configure their own setup. The package
offers a direct interface to varioref (for use, for example, in large
projects such as a series of books, or a multivolume thesis written as a
series of documents), and name references from the nameref package may
be incorporated with ease. For large projects such as a series of books
or a multi volume thesis, written as freestanding documents, a facility
is provided to interface to the xr package for external document
references.

