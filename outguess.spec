Summary:	Universal steganographic tool
Name:		outguess
Version:	0.2
Release:	1
License:	BSD
Group:		Applications/File
Group(de):	Applikationen/Datei
Group(pl):	Aplikacje/Pliki
Source0:	http://www.outguess.org/%{name}-%{version}.tar.gz
URL:		http://www.outguess.org
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

#%description -l pl

%prep
%setup  -q -n %{name}

%build
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
