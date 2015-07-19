# revision 15878
# category Package
# catalog-ctan /info/bibtex/tamethebeast
# catalog-date 2009-10-11 21:12:19 +0200
# catalog-license lppl1.3
# catalog-version 1.4
Name:		texlive-tamethebeast
Version:	1.4
Release:	10
Summary:	A manual about bibliographies and especially BibTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/bibtex/tamethebeast
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tamethebeast.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tamethebeast.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.4-2
+ Revision: 756509
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.4-1
+ Revision: 719653
- texlive-tamethebeast
- texlive-tamethebeast
- texlive-tamethebeast

