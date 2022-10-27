FROM ubuntu:16.04

RUN apt update
RUN apt -y upgrade
RUN apt-get install -y wget curl build-essential python3-dev  python2.7-dev libssl-dev libffi-dev libtiff5-dev \
	libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk \
	libxml2-dev libxslt1-dev python-pip python3-software-properties software-properties-common libsasl2-dev \
	python-dev libldap2-dev libfreetype6 libfontconfig1-dev libfontconfig1 xvfb python2.7 libsqlite3-dev \
	vim libyaml-dev openssh-server git python-lxml libnss3-tools xdot python-gtk2 \
	python-gtksourceview2 ubuntu-artwork dmz-cursor-theme ca-certificates openjdk-8-jre zip unzip


RUN wget -q https://bootstrap.pypa.io/pip/2.7/get-pip.py && python2 get-pip.py && rm get-pip.py
RUN echo "Downloading and Installing FIREFOX" && cd /usr/local && \
	wget http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/89.0/linux-x86_64/en-US/firefox-89.0.tar.bz2 && \
	tar xvjf firefox-89.0.tar.bz2 && ln -s /usr/local/firefox/firefox /usr/bin/firefox && rm firefox-89.0.tar.bz2

RUN pip install --upgrade pip
RUN pip install robotframework-seleniumlibrary
RUN pip install RoboZap==1.2.8
RUN pip install --upgrade RESTinstance

RUN cd /
RUN wget https://github.com/zaproxy/zaproxy/releases/download/2.7.0/ZAP_2.7.0_Linux.tar.gz
RUN tar -xvzf /ZAP_2.7.0_Linux.tar.gz
RUN cd /ZAP_2.7.0/plugin && wget https://github.com/zaproxy/zap-extensions/releases/download/2.7/exportreport-alpha-5.zap
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
RUN tar -xvzf geckodriver-v0.26.0-linux64.tar.gz
RUN cp geckodriver /usr/local/bin

COPY /requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY /RoboZapImportScanPolicy.py RoboZapImportScanPolicy.py
CMD python RoboZapImportScanPolicy.py

RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"
RUN unzip awscli-bundle.zip
RUN ./awscli-bundle/install -b ~/bin/aws
