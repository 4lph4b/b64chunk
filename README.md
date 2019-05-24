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
## Example
```
user@kali# python b64chunk.py --target powershell ./test.bin
$qcturmrs = @()
$qcturmrs += [System.Convert]::FromBase64String("O17jKOVg...0jSS1+4=")
$qcturmrs += [System.Convert]::FromBase64String("nQa7gkvB...kBQrwp0=")
$qcturmrs += [System.Convert]::FromBase64String("GK43JF6b...6suWCg==")
[Environment]::CurrentDirectory = (Get-Location -PSProvider FileSystem).ProviderPath
[System.IO.File]::WriteAllBytes("test.bin", $qcturmrs)
Remove-Variable qcturmrs
```
