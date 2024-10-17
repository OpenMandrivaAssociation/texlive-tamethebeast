Name:		texlive-tamethebeast
Version:	15878
Release:	2
Summary:	A manual about bibliographies and especially BibTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/bibtex/tamethebeast
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tamethebeast.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tamethebeast.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
An (as-complete-as-possible) manual about bibliographies in
LaTeX, and thus mainly about BibTeX.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/bibtex/tamethebeast/CHANGES
%doc %{_texmfdistdir}/doc/bibtex/tamethebeast/Makefile
%doc %{_texmfdistdir}/doc/bibtex/tamethebeast/README
%doc %{_texmfdistdir}/doc/bibtex/tamethebeast/idxstyle.ist
%doc %{_texmfdistdir}/doc/bibtex/tamethebeast/local.bib
%doc %{_texmfdistdir}/doc/bibtex/tamethebeast/ttb_en.pdf
%doc %{_texmfdistdir}/doc/bibtex/tamethebeast/ttb_en.sec1.tex
%doc %{_texmfdistdir}/doc/bibtex/tamethebeast/ttb_en.sec2.tex
%doc %{_texmfdistdir}/doc/bibtex/tamethebeast/ttb_en.sec3.tex
%doc %{_texmfdistdir}/doc/bibtex/tamethebeast/ttb_en.sec4.tex
%doc %{_texmfdistdir}/doc/bibtex/tamethebeast/ttb_en.sec5.tex
%doc %{_texmfdistdir}/doc/bibtex/tamethebeast/ttb_en.tex
%doc %{_texmfdistdir}/doc/bibtex/tamethebeast/ttb_style.sty

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
