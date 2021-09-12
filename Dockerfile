FROM ubuntu:20.04
COPY repeat.py /usr/local/bin/
WORKDIR /opt/code/

RUN apt-get update
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y tzdata python3 \
    && apt-get clean
RUN /usr/local/bin/repeat.py apt-get install -y \
    poppler-utils \
    texlive texlive-lang-chinese texlive-pictures texlive-latex-extra \
    texlive-luatex texlive-xetex texlive-extra-utils \
    && apt-get clean
COPY src/fathom /usr/local/lib/python3.8/dist-packages/fathom
COPY src/entry-point.py /usr/local/bin/
ENTRYPOINT ["/usr/local/bin/entry-point.py"]

