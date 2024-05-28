"""
to run every case(.py) in *demos*, use the following command:

- compile .py to .wasm
``` bash
$ py2wasm ABC.py -o ABC.wasm
``` 

- compile .wasm to .aot
``` bash
$ /opt/wamr/bin/wamrc -o ABC.aot ABC.wasm
```

- run .wasm with iwasm
``` bash
$ /opt/wamr/bin/iwasm ABC.wasm
```
- run .aot with iwasm
``` bash
$ /opt/wamr/bin/iwasm ABC.aot
```
"""
