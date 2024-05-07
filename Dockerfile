FROM ubuntu:24.04
COPY repeat.sh /usr/local/bin/
COPY ubuntu.sources /etc/apt/sources.list.d/
WORKDIR /opt/code/
ENTRYPOINT ["/usr/local/bin/entry-point.py"]

RUN repeat.sh apt-get update
RUN DEBIAN_FRONTEND="noninteractive" repeat.sh apt-get install -y \
    tzdata fish \
    && apt-get clean

# user
ENV COLORTERM="truecolor" TERM="xterm-256color"
RUN usermod --append --groups sudo ubuntu \
    && usermod --shell /usr/bin/fish ubuntu
COPY --chown=1000:1000 config.fish /home/ubuntu/.config/fish/
COPY sudoers /etc/

RUN repeat.sh apt-get install -y \
    python3 poppler-utils \
    texlive texlive-lang-chinese texlive-pictures texlive-latex-extra \
    texlive-luatex texlive-xetex texlive-extra-utils \
    && apt-get clean \
    && su --command="luaotfload-tool --update" ubuntu
COPY src/fathom /usr/local/lib/python3.12/dist-packages/fathom
COPY src/entry-point.py /usr/local/bin/

