%define name cardpics
%define version 0.4
%define release 12

Summary: Some Card images
Name: %{name}
Version: 0.4
Release: 1%{release}
License: GPL
Group: Games/Cards
Source: http://download.savannah.nongnu.org/releases/cardpics/%{name}-%{version}.tar.bz2
URL: https://www.nongnu.org/cardpics
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch

%description
Cardpics is a set of free cards sets.

If you are programming a card game and are looking for free cards, Cardpics was
made for you! Get a set of cards and include them in your project, as soon as
your project is free.

%description -l fr
Cardpics est un jeu de cartes. Pour �viter l'ambiguit� sur le terme "jeu",
disons que c'est un ensemble d'images de cartes � jouer.

Si vous programmez un jeu de cartes et avez besoin d'un jeu d'images de cartes
libres, Cardpics est fait pour vous! R�cup�rez un jeu de ces cartes, et
incluez-le dans votre projet, � condition que votre projet soit libre.

%description -l es
Cardpics es una serie de juegos de cartas.

Si est� programando un juego de cartas y est� buscando cartas libres, Cardpics
fue hecho para usted! Obtenga un juego de cartas e incl�yalas en su proyecto,
mientras que este sea libre.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_datadir}/*




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4-11mdv2011.0
+ Revision: 616941
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.4-10mdv2010.0
+ Revision: 424748
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 0.4-9mdv2009.0
+ Revision: 240487
- rebuild
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Aug 19 2007 Olivier Thauvin <nanardon@mandriva.org> 0.4-7mdv2008.0
+ Revision: 66710
- rebuild


* Fri Aug 04 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/04/06 21:30:59 (52914)
- rebuild

* Fri Aug 04 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/04/06 21:30:01 (52913)
Import cardpics

* Mon Apr 17 2006 Olivier Thauvin <nanardon@mandriva.org> 0.4-5mdk
- rebuild

* Tue Mar 29 2005 Olivier Thauvin <nanardon@mandrake.org> 0.4-4mdk
- %%mkrel && rebuild

* Sat Jan 03 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.4-3mdk
- birthday rebuild

