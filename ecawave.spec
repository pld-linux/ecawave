Summary:	ecawave - graphical audio file editor
Summary(pl):	ecawave - graficzny edytor plików d¼wiêkowych
Name:		ecawave
Version:	0.6.0
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://ecasound.seul.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	72a3245cc9326c47fa3ee6251f3b0a4c
BuildRequires:	ecasound-devel >= 2.2.0
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

%description -l pl
ecawave to prosty graficzny edytor plików d¼wiêkosych. Interfejs
u¿ytkownika bazuje na bibliotekach Qt, natomiast prawie ca³a
funkcjonalno¶æ zwi±zana z d¼wiêkiem pochodzi bezpo¶rednio z bibliotek
ecasound. Poniewa¿ ecawave jest przeznaczony do edycji du¿ych plików
d¼wiêkowych, ca³e przetwarzanie jest wykonywane bezpo¶rednio na dysk.
Wykorzystywane jest proste buforowanie próbek, aby przyspieszyæ
operacje na plikach. ecawave obs³uguje wszystkie formaty plików
d¼wiêkowych i algorytmy efektów udostêpnione przez biblioteki
ecasound. Obejmuje to wej¶cie/wyj¶cie d¼wiêku JACK, ALSA, OSS i aRts
(zale¿nie od opcji, z jakimi by³o zbudowane ecasound), ponad 20
formatów plików, ponad 30 typów efektów, wtyczki LADSPA oraz
ustawienia efektu multi-operator.

%prep
%setup -q

%build
%configure2_13

%{__make}

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
