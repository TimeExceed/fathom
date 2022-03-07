FROM ubuntu:20.04
COPY repeat.sh /usr/local/bin/
COPY sources.list /etc/apt/
WORKDIR /opt/code/
ENTRYPOINT ["/usr/local/bin/entry-point.py"]
# user
ENV COLORTERM="truecolor" TERM="xterm-256color"
RUN groupadd --gid 1000 dockeruser \
    && useradd --uid 1000 --gid 1000 --shell /bin/bash --create-home --system dockeruser \
    && usermod --append --groups sudo dockeruser
COPY --chown=1000:1000 bashrc /home/dockeruser/.bash_profile
COPY --chown=1000:1000 bashrc /home/dockeruser/.bashrc
COPY sudoers /etc/

# install fathom
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

