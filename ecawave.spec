Summary:	ecawave - graphical audio file editor
Summary(pl.UTF-8):   ecawave - graficzny edytor plików dźwiękowych
Name:		ecawave
Version:	0.6.1
Release:	5
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://ecasound.seul.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	19bbd69d52debe851fbfda4438aa5535
URL:		http://www.eca.cx/ecawave/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	ecasound-devel >= 2.2.0
BuildRequires:	libtool
BuildRequires:	qt-devel
Requires:	ecasound >= 2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ecawave is a simple graphical audio file editor. The user-interface is
based on Qt libraries, while almost all audio functionality is taken
directly from ecasound libraries. As ecawave is designed for editing
large audio files, all processing is done direct-to-disk. Simple
waveform caching is used to speed-up file operations. Ecawave supports
all audio file formats and effect algorithms provided by ecasound
libraries. This includes JACK, ALSA, OSS, aRts audio I/O (depending on
ecasound build options), over 20 file formats, over 30 effect types,
LADSPA plugins and multi-operator effect presets.

%description -l pl.UTF-8
ecawave to prosty graficzny edytor plików dźwiękowych. Interfejs
użytkownika bazuje na bibliotekach Qt, natomiast prawie cała
funkcjonalność związana z dźwiękiem pochodzi bezpośrednio z bibliotek
ecasound. Ponieważ ecawave jest przeznaczony do edycji dużych plików
dźwiękowych, całe przetwarzanie jest wykonywane bezpośrednio na dysk.
Wykorzystywane jest proste buforowanie próbek, aby przyspieszyć
operacje na plikach. ecawave obsługuje wszystkie formaty plików
dźwiękowych i algorytmy efektów udostępnione przez biblioteki
ecasound. Obejmuje to wejście/wyjście dźwięku JACK, ALSA, OSS i aRts
(zależnie od opcji, z jakimi było zbudowane ecasound), ponad 20
formatów plików, ponad 30 typów efektów, wtyczki LADSPA oraz
ustawienia efektu multi-operator.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--with-qt-libraries=/usr/%{_lib} \
	--with-qt-includes=%{_includedir}/qt

%{__make} \
	qt_libname="qt-mt"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS NEWS README TODO Documentation/users_guide.html
%attr(755,root,root) %{_bindir}/ecawave
%{_mandir}/man1/ecawave.1*
