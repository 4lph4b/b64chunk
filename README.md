# b64chunk
Create files using base64 encoding

Generates a series of shell commands to build a file using base64 encoding. Target shell can be bash, cmd.exe, or powershell (any version). Input file can be ascii or binary. Output from this script can be copy-and-pasted directly into a local or remote terminal session.

```
usage: b64chunk.py [-h] [-t TARGET] [-s CHUNK_SIZE] [-d DESTINATION] FILE

positional arguments:
    FILE            Local file

optional arguments:
    -h, --help      show this help message and exit
    -t TARGET       Target shell (bash, cmd, powershell - default: bash)
    -s CHUNK_SIZE   Split by chunk size (default: 5k)
    -d DESTINATION  Destination file name (default: same as local filename)
```
