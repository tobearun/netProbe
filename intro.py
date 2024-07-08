from colorama import init, Fore, Style
import time

# Initialize colorama for cross-platform ANSI color support
init(autoreset=True)


def show_splash_screen():
    # ASCII art banner
    print(Fore.YELLOW + r"""
 _   _      _    ______          _          
| \ | |    | |   | ___ \        | |         
|  \| | ___| |_  | |_/ / __ ___ | |__   ___ 
| . ` |/ _ \ __| |  __/ '__/ _ \| '_ \ / _ \
| |\  |  __/ |_  | |  | | | (_) | |_) |  __/
\_| \_/\___|\__| \_|  |_|  \___/|_.__/ \___|


    """ + Style.RESET_ALL)

    print(Fore.GREEN + "Welcome to NetProbe - Your Network Packet Sniffer" + Style.RESET_ALL)
    print("Version 1.0\n")
    print("Initializing...")
    time.sleep(2)  # Simulate initialization delay


# Example usage
if __name__ == "__main__":
    show_splash_screen()
    # Your main program logic follows here
