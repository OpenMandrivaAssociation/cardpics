%define name cardpics
%define version 0.4
%define release %mkrel 9

Summary: Some Card images
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Games/Cards
Source: http://download.savannah.nongnu.org/releases/cardpics/%{name}-%{version}.tar.bz2
URL: http://www.nongnu.org/cardpics
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch

%description
Cardpics is a set of free cards sets.

If you are programming a card game and are looking for free cards, Cardpics was
made for you! Get a set of cards and include them in your project, as soon as
your project is free.

%description -l fr
Cardpics est un jeu de cartes. Pour éviter l'ambiguité sur le terme "jeu",
disons que c'est un ensemble d'images de cartes à jouer.

Si vous programmez un jeu de cartes et avez besoin d'un jeu d'images de cartes
libres, Cardpics est fait pour vous! Récupérez un jeu de ces cartes, et
incluez-le dans votre projet, à condition que votre projet soit libre.

%description -l es
Cardpics es una serie de juegos de cartas.

Si está programando un juego de cartas y está buscando cartas libres, Cardpics
fue hecho para usted! Obtenga un juego de cartas e inclúyalas en su proyecto,
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


