FROM ubuntu:20.04
COPY repeat.sh /usr/local/bin/
WORKDIR /opt/code/

RUN /usr/local/bin/repeat.sh apt-get update
RUN DEBIAN_FRONTEND="noninteractive" /usr/local/bin/repeat.sh apt-get install -y \
    tzdata  \
    && apt-get clean
RUN /usr/local/bin/repeat.sh apt-get install -y \
    python3 poppler-utils \
    texlive texlive-lang-chinese texlive-pictures texlive-latex-extra \
    texlive-luatex texlive-xetex texlive-extra-utils \
    && apt-get clean
COPY src/fathom /usr/local/lib/python3.8/dist-packages/fathom
COPY src/entry-point.py /usr/local/bin/
ENTRYPOINT ["/usr/local/bin/entry-point.py"]

