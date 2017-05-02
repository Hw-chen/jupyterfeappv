FROM ubuntu
FROM jupyter/base-notebook

USER root

RUN apt-get update && apt-get install -yq --no-install-recommends \
    git \
    vim \
    jed \
    emacs \
    build-essential \
    python-dev \
    libsm6 \
    pandoc \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-fonts-extra \
    texlive-fonts-recommended \
    texlive-generic-recommended \
    texlive-xetex \
    lmodern \
    libxrender1 \
    inkscape \
    gcc \
    gfortran \
    unzip \
    wget \
    xserver-xorg-dev \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*


ENV FEAPPVHOME3_1 /feappv/ver31
WORKDIR /feappv
ADD http://www.ce.berkeley.edu/projects/feap/feappv/feappv31.zip .
COPY makefile.in .

RUN unzip feappv31.zip \
 && mkdir -p decks \
 && cp makefile.in ver31/ \
 && cd ver31 \
 && make install

WORKDIR /home/jovyan/work
COPY server.py server.py
COPY client.py client.py









