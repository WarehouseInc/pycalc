# python-calculator

my new python calculator

1.This is a command-line executable, written in Python 3.10.

2.The calculator supports 6 operations: +(addition), -(subtraction), *(multiplication), /(division), **(power), %(modulo).

3.Only numbers are supported. If you enter anything other than numbers, the app will send an error message, then terminate.


4.The source code is available in a Python source file.

Python IDLE is the ideal editor, but you can also use Visual Studio Code(with Python extension), Notepad++, Vim, etc.

5.If needed, use PyInstaller to publish your copy of the software with .EXE extension.

6.The GNU GPLv3 license is published in another DOCX file. This file is named “GPLv3.docx” with a SHA512 hash of 

a77455e6b9a2391755b0eba326b7165a85ffcf9a70d88c5995911af8dc28ff1c60c76c499d2b36fe9ba2204b6c3f5e3d141c5c39aa634ee85c3345d7b513e1fc

Please check its integrity before opening.

Release Notes:

v1.5:

-Added an error message when invalid input is received in the number input field

v1.4

-Added an error message when a divide/modulo by zero exception is encountered and is not properly handled

v1.3

-Added modulo function

v1.2:

-Changed error message when entering anything other than operators

v1.1:

-Added welcome and exit text

-Compressed for better portability

-Fixed an issue where some antiviruses may flag the executable as a trojan

v1.0:

-Original release

Known bugs:

-When using the + operation, entering the 1st number but not the 2nd number can give the UnboundLocalError exception. The app automatically terminates after this.

-If receiving any input other than numbers, the app will send an error message, then terminate. This issue is now resolved in update v1.5.

I always appreciate any feedback and suggestions for this software, especially about the auto-termination error which wasn't noticed until v1.5.
