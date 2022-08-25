# python-calculator

1. This is a command-line executable, written in Python 3.10.

2. The calculator supports 6 operations: + (addition), - (subtraction), * (multiplication), / (division), ** (power), % (modulo) and √ (square root).

3. Code available in a Python source file. Python IDLE is the ideal editor, but you can also use Visual Studio Code(with Python extension), Notepad++, Kate, etc.

4. If needed, use PyInstaller to publish your copy of the software as an executable.

5. You might wonder why there hasn't been a new release for a long time. Well it's because this calculator is just a project born out of impulse and thus won't be in active development. I'll release a new version when it's ready.

6. Recommended for use in a terminal instance, since the `again()` function is currently broken, as of release 1.7. An issue has been created in the repository. 

7. WARNING: DO NOT DOWNLOAD OLD VERSIONS UNLESS ASKED TO, AS THEY MAY CONTAIN UNDETECTED/UNINTENTIONALLY DEVELOPED MALWARE. Always check the downloaded files' integrity before opening. SHA256 file hashes are only available for the current release in this Readme markdown file.

Main calculator executable: `f1bb8706ef7e42488dbd6d08fe288ba399e6ebcfc83916c832cae10517f3555b`

Main calculator source: `4be9096e58069339d03e33f04203f83d1851776c0838abb1b19cdca917b8e3e5`

Pi digit calculator executable: `529f3a2105c3c07cd7ee4e4b2d23bb4a436d879fa8d716a9a629d93126591c4e`

Pi digit calculator source: `aeba56c9d9e5a2c796df31cab5d1d02060dd8901b06863e68266fe3f2b90100e`

Use a hash calculator like 7-Zip's CRC SHA or PowerShell (see below). For 7-Zip just right click the file, hover to its context menu, then CRC SHA, and choose SHA256.

For PowerShell it's a bit more complicated but the command syntax goes like this:

`Get-FileHash [-Path] <String[]> [[-Algorithm] <String>] [<CommonParameters>]`

Example: `PS C:\> Get-FileHash C:\pi.py -Algorithm SHA256 | Format-List` will print the SHA256 value of the `pi.py` file which, as stated above, should be `aeba56c9d9e5a2c796df31cab5d1d02060dd8901b06863e68266fe3f2b90100e`.
