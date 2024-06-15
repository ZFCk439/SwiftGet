from pyfiglet import figlet_format as figlet
from wget import download
import urllib.error
import os

def main():
    os.system("clear")
    print(figlet("SwiftGet", font="slant"))

    while True:
        try:
            wget_input = input("\033[32m"+"URL: ")
            print("\n" + "\033[33m[+] Downloading The File\n")
            Downlod_url = download(wget_input) + "\n"
            print(f"\033[32m[+] File downloaded successfully: {Downlod_url}\n")
        except urllib.error.HTTPError:
            print("\033[31mURL is unknown or invalid. Please try again.\n")
        except urllib.error.URLError:
            print("\033[31mFailed to reach the server. Please check your internet connection and try again.\n")
        except ValueError:
            print("\033[31mInvalid value encountered. Please enter a valid URL.\n")
        except OSError:
            print("\033[31mFailed to Connected in Internet")

if __name__ == "__main__":
    main()
      
