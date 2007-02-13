Summary:	Universal steganographic tool
Summary(pl.UTF-8):	Uniwersalne narzędzie stenograficzne
Name:		outguess
Version:	0.2
Release:	2
License:	BSD
Group:		Applications/File
Source0:	http://www.outguess.org/%{name}-%{version}.tar.gz
# Source0-md5:	321f23dc0badaba4350fa66b59829064
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

%description -l pl.UTF-8
OutGuess to uniwersalne narzędzie stenograficzne pozwalające na
wstawianie ukrytych informacji do nadmiarowych bitów danych. Rodzaj
danych nie ma znaczenia dla serca OutGuess. Polega on na handlerach
obsługujących określone formaty danych, które odczytują nadmiarowe
bity i zapisują je z powrotem po modyfikacji. W tej wersji obsługiwane
są formaty PNM i JPEG. Dokumentacja jest pisana na przykładzie
obrazków, ale OutGuess może działać na dowolnych danych, do których ma
dostarczony handler.

%prep
%setup  -q -n %{name}

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install install_prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
