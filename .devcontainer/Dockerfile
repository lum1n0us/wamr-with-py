FROM mcr.microsoft.com/devcontainers/python:3.11-bookworm

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt upgrade -y

RUN apt update \
  && apt install -y --no-install-recommends \
    bat build-essential clang file llvm software-properties-common tree wget

RUN apt update \
  && apt install -y clang-tools clang-tidy clang-format clangd \
  && apt install -y lldb python3-lldb

#
# Install wasi-sdk
ARG WASI_SDK_VER=22
WORKDIR /opt
RUN wget -c --progress=dot:giga https://github.com/WebAssembly/wasi-sdk/releases/download/wasi-sdk-${WASI_SDK_VER}/wasi-sdk-${WASI_SDK_VER}.0-linux.tar.gz -P /opt \
  && tar xf /opt/wasi-sdk-${WASI_SDK_VER}.0-linux.tar.gz -C /opt \
  && rm /opt/wasi-sdk-${WASI_SDK_VER}.0-linux.tar.gz

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
# Install WAMR stuff
ARG IWASM_VER=0d8ffebd
COPY from_wamr_repo/iwasm_binary/${IWASM_VER}/iwasm /opt/wamr/bin/iwasm_${IWASM_VER}
COPY from_wamr_repo/iwasm_binary/${IWASM_VER}/iwasm.dbg /opt/wamr/bin/iwasm_${IWASM_VER}.dbg
RUN ln -sf /opt/wamr/bin/iwasm_${IWASM_VER} /usr/local/bin/iwasm \
  && ln -sf /opt/wamr/bin/iwasm_${IWASM_VER}.dbg /usr/local/bin/iwasm.dbg

COPY from_wamr_repo/addr2line.py /opt/wamr/bin/addr2line.py
RUN ln -sf /opt/wamr/bin/addr2line.py /usr/local/bin/addr2line
