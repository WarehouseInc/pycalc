# python-calculator

1. This is a command-line executable, written in Python 3.11.

2. The calculator supports 8 operations: + (addition), - (subtraction), * (multiplication), / (division), ** (power), % (modulo), √ (square root) and 3√ (cube root).

3. Always check the downloaded files' integrity before opening. SHA256 file hashes are only available for the current release in this Readme markdown file.

Main calculator executable: `7300380b21bd390190875093c8a55f871cd0a5f4bc3a0b6f51366a12633ba5b0`

Main calculator source: `1858921975bc96861911b517291eef183815b6283484315112a54092d3149a3d`

Pi digit calculator executable: `7399cc5766a0da98d8213fe047322f0530898faadab8307ad29dc6e9a2ca8763`

Pi digit calculator source: `d07cd890f3a05f1a41e573188b1eec1e1185847b9ce22d698d0b527e5b83869d`

Use a hash calculator like 7-Zip's CRC SHA or PowerShell (see below). For 7-Zip just right click the file, hover to its context menu, then CRC SHA, and choose SHA256.

For PowerShell it's a bit more complicated but the command syntax goes like this:

`Get-FileHash [-Path] <FileName> [[-Algorithm] <AlgoName>] [<CommonParameters>]`

(`CommonParameters` is denoted in [Microsoft's guide about hashing in PS](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-filehash?view=powershell-7.3))

Example: `PS C:\> Get-FileHash C:\pi.py -Algorithm SHA256 | Format-List` will print the SHA256 value of the `pi.py` file which, as stated above, should be `d07cd890f3a05f1a41e573188b1eec1e1185847b9ce22d698d0b527e5b83869d`.
![Screenshot 2022-12-08 174809](https://user-images.githubusercontent.com/70247964/206427757-a2589044-d667-46c3-90d0-243cca3917af.png)
