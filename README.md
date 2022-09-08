# python-calculator

1. This is a command-line executable, written in Python 3.10.

2. The calculator supports 8 operations: + (addition), - (subtraction), * (multiplication), / (division), ** (power), % (modulo), √ (square root) and 3√ (cube root).

3. If needed, use PyInstaller to publish your copy of the software as an executable.

4. You might wonder why there hasn't been a new release for a long time. Well it's because this calculator is just a project born out of impulse and thus won't be in active development. I'll release a new version when it's ready.

5. Recommended for use in a terminal instance, since the `again()` function is currently broken, as of release 1.7. An issue has been created in the repository. 

6. WARNING: DO NOT DOWNLOAD OLD VERSIONS UNLESS ASKED TO, AS THEY MAY CONTAIN UNDETECTED/UNINTENTIONALLY DEVELOPED MALWARE. Always check the downloaded files' integrity before opening. SHA256 file hashes are only available for the current release in this Readme markdown file.

Main calculator executable: `f79cad2f0f9e3f19706ec855b0d2afa02904cded1cc4ad3ce620c97507033a50`

Main calculator source: `75ffbb767abab662ee7cbd36a5caebdab8a8051bfab05e511615d5bb0fcb1130`

Pi digit calculator executable: `529f3a2105c3c07cd7ee4e4b2d23bb4a436d879fa8d716a9a629d93126591c4e`

Pi digit calculator source: `d07cd890f3a05f1a41e573188b1eec1e1185847b9ce22d698d0b527e5b83869d`

Use a hash calculator like 7-Zip's CRC SHA or PowerShell (see below). For 7-Zip just right click the file, hover to its context menu, then CRC SHA, and choose SHA256.

For PowerShell it's a bit more complicated but the command syntax goes like this:

`Get-FileHash [-Path] <String[]> [[-Algorithm] <String>] [<CommonParameters>]`

Example: `PS C:\> Get-FileHash C:\pi.py -Algorithm SHA256 | Format-List` will print the SHA256 value of the `pi.py` file which, as stated above, should be `aeba56c9d9e5a2c796df31cab5d1d02060dd8901b06863e68266fe3f2b90100e`.
