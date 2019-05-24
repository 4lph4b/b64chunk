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
## Bash Example
```
user@kali# python b64chunk.py --target bash ./test.bin
rm test.bin
echo -n 'O17jKOVg...0jSS1+4=' | base64 -d >> test.bin
echo -n 'nQa7gkvB...kBQrwp0=' | base64 -d >> test.bin
echo -n 'GK43JF6b...6suWCg==' | base64 -d >> test.bin
```
## Cmd Example
```
user@kali# python b64chunk.py --target cmd ./test.bin
del /Q test.bin
del /Q kfkjubmg
echo|set /p="O17jKOVg...r5J8fz1H" >> kfkjubmg
echo|set /p="YzDOG1XA...4WXvKprN" >> kfkjubmg
echo|set /p="c7TsEQEx...3gPDO9A+" >> kfkjubmg
echo|set /p="RDoV+R+O...yerLlgo=" >> kfkjubmg
certutil -decode kfkjubmg test.bin
del /Q kfkjubmg
```
## Powershell Example
```
user@kali# python b64chunk.py --target powershell ./test.bin
del test.bin
$qcturmrs = @()
$qcturmrs += [System.Convert]::FromBase64String("O17jKOVg...0jSS1+4=")
$qcturmrs += [System.Convert]::FromBase64String("nQa7gkvB...kBQrwp0=")
$qcturmrs += [System.Convert]::FromBase64String("GK43JF6b...6suWCg==")
[Environment]::CurrentDirectory = (Get-Location -PSProvider FileSystem).ProviderPath
[System.IO.File]::WriteAllBytes("test.bin", $qcturmrs)
Remove-Variable qcturmrs
```
