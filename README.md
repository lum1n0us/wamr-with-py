## Python to WebAssembly

### Install py2wasm from source code

*it is a self-modified version of [py2wasm](https://github.com/wasmerio/py2wasm).*

Download souce code

`$ git clone https://github.com/lum1n0us/Nuitka.git --branch dev/wasi_sync_upstream`

Switch to the repo directory

`$ cd Nuitka`

Install

`$ sudo python setup.py install`

or

`$ python setup.py install --user`

Check if the installation is successful

`$ py2wasm --version`

### Compile Python code to WebAssembly

`$ py2wasm -o test.wasm test.py`

> It'll download wasi-sdk automatically if it's not installed.

Then, you can run the WebAssembly file with a Wasm runtime. Usually it requires a bigger stack size and preopen the current directory.

`$ iwasm --dir=. --stack-size=134217728 test.wasm`

## LIMITATIONS

Currently, only supports Python 3.11. Not all Python features are supported. The following are some of the limitations:

### Network stack

don't support all networking related modules. like `socket`, `urllib` and so on. `requests` too.

### Concurrency

- don't support `threading`.
- don't support `multiprocessing`

### Asynchronous

- dont' support `concurrent.futures`, `asyncio`.
- support `yield`

### MetaProgramming

only support decorators
