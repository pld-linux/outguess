Summary:	Universal steganographic tool
Summary(pl);	Uniwersalne narz�dzie stenograficzne
Name:		outguess
Version:	0.2
Release:	2
License:	BSD
Group:		Applications/File
Group(de):	Applikationen/Datei
Group(pl):	Aplikacje/Pliki
Source0:	http://www.outguess.org/%{name}-%{version}.tar.gz
URL:		http://www.outguess.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OutGuess is a universal steganographic tool that allows the insertion
of hidden information into the redundant bits of data sources. The
nature of the data source is irrelevant to the core of OutGuess. The
program relies on data specific handlers that will extract redundant
bits and write them back after modification. In this version the PNM
and JPEG image formats are supported. In the next paragraphs, images
will be used as concrete example of data objects, though OutGuess can
use any kind of data, as long as a handler is provided.

%description -l pl
OutGuess to uniwersalne narz�dzie stenograficzne pozwalaj�ce na
wstawianie ukrytych informacji do nadmiarowych bit�w danych. Rodzaj
danych nie ma znaczenia dla serca OutGuess. Polega on na handlerach
obs�uguj�cych okre�lone formaty danych, kt�re odczytuj� nadmiarowe
bity i zapisuj� je z powrotem po modyfikacji. W tej wersji obs�ugiwane
s� formaty PNM i JPEG. Dokumentacja jest pisana na przyk�adzie
obrazk�w, ale OutGuess mo�e dzia�a� na dowolnych danych, do kt�rych ma
dostarczony handler.

%prep
%setup  -q -n %{name}

%build
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install install_prefix=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
