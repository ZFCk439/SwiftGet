#SwiftGet
It is an advanced Linux downloader, designed to provide an ultra-fast and easy-to-use download experience, and works seamlessly with various Linux distributions such as Termux, Kali, Arch, and Debian.

Requirements:
• Linux operating system.
• Python 3.6 or newer.

Steps for installing:

1.Clonning The reposity:

    git clone
    https://github.com/ZFCk/SwiftGet.git

    cd SwiftGet

2.Create a virtual environment (optional):

    python3 -m venv env source env/bin/activate

3.Installing Requirements:

    pip install -r requirements.txt
    
4.Run SwiftGet:

    python swiftget.py

Using:

•Download Files:
    
    python3 swiftget.py https://example.com/file.zip
    
•Download Double Files:
    
    python3 swiftget.py https://example.com/file1.zip https://example.com/file2.zip
    
•Select Max Speed for downloading:
    
    python3 swiftget.py --limit-rate 500k https://example.com/file.zip

License:

•SwiftGet is distributed under the MIT License.  See LICENSE for more details.

Image For The Tool:
![SwiftGet](https://github.com/ZFCk439/SwiftGet/assets/172911108/3dcdc8be-b5e8-4b00-8807-1c7bf9a5c52e)

