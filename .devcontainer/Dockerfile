FROM mcr.microsoft.com/devcontainers/python:3.11-bookworm

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt upgrade -y

RUN apt install -y --no-install-recommends \
    bat build-essential file software-properties-common tree wget

#
# Install WAMR
WORKDIR /opt
RUN mkdir -p wamr/bin
WORKDIR /opt/wamr/bin
RUN wget https://github.com/bytecodealliance/wasm-micro-runtime/releases/download/WAMR-2.0.0/iwasm-2.0.0-x86_64-ubuntu-22.04.tar.gz
RUN tar xf iwasm-2.0.0-x86_64-ubuntu-22.04.tar.gz \
  && rm iwasm-2.0.0-x86_64-ubuntu-22.04.tar.gz

RUN wget https://github.com/bytecodealliance/wasm-micro-runtime/releases/download/WAMR-2.0.0/wamrc-2.0.0-x86_64-ubuntu-22.04.tar.gz
RUN tar xf wamrc-2.0.0-x86_64-ubuntu-22.04.tar.gz \
  && rm wamrc-2.0.0-x86_64-ubuntu-22.04.tar.gz

#
# Install wabt
WORKDIR /opt
RUN wget https://github.com/WebAssembly/wabt/releases/download/1.0.35/wabt-1.0.35-ubuntu-20.04.tar.gz
RUN tar xf wabt-1.0.35-ubuntu-20.04.tar.gz \
  && rm wabt-1.0.35-ubuntu-20.04.tar.gz

#
# Install binaryen
WORKDIR /opt
RUN wget https://github.com/WebAssembly/binaryen/releases/download/version_117/binaryen-version_117-x86_64-linux.tar.gz
RUN tar xf binaryen-version_117-x86_64-linux.tar.gz \
  && rm binaryen-version_117-x86_64-linux.tar.gz

#
# Install wasmer
WORKDIR /opt
RUN wget https://github.com/wasmerio/wasmer/releases/download/v4.3.0/wasmer-linux-amd64.tar.gz
RUN mkdir wasmer-4.3.0 \
  && tar xf wasmer-linux-amd64.tar.gz -C wasmer-4.3.0 \
  && rm wasmer-linux-amd64.tar.gz
