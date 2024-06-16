FROM mcr.microsoft.com/devcontainers/python:3.11-bookworm

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt upgrade -y

RUN apt install -y --no-install-recommends \
    bat build-essential file software-properties-common tree wget

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

#
# Install WAMR
COPY iwasm_binary/d3e89895b/iwasm_wasi_interp /opt/wamr/bin/iwasm_wasi_interp_d3e89895b
RUN ln -sf /opt/wamr/bin/iwasm_wasi_interp_d3e89895b /usr/local/bin/iwasm
