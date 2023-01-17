from os import system, name
from signal import signal, SIGINT
from sys import exit
from time import sleep
try:
    from colorama import Fore, Back, Style, init
except:
    system('pip install colorama')
    from colorama import Fore, Back, Style, init
try:
    from termcolor import colored
except:
    system('pip install termcolor')
    from termcolor import colored
try:
    from cursor import hide, show
except:
    system('pip install cursor')
    from cursor import hide, show
init(autoreset=True, convert=True)



#   Author: Cloud
#   Version: 1.0
#   Name: Cloud Tools
#   Description: Bunch of Tools for Cloud
#   Site: cloudzik.cc
#   Github: github.com/Cloudzik1337
#   Year: 2023


class CloudTools:
    """Bunch of Tools for Cloud
    Tools Avaible: 
    cls() 
    banner(title, author, version, site, github, year) 
    exit_timer() 
    set_title(title) 
    color(color, text)

    """
    def __init__(self):
        
        self.author = "Cloud"
        self.version = "1.0"
        self.name = "Cloud Tools"
        self.description = "Tools for Cloud"
        self.site = "cloudzik.cc"
        self.github = "github.com/Cloudzik1337"
        self.exit_timer = 5
    
    def cls(self):
        """Clears the screen."""
        clear = lambda: system('cls' if name == 'nt' else 'clear')
        clear()
    
    def banner(self, title='', author='', version='', site='', github='', year='2023'):
        """Prints a banner with the given parameters.
        Usage: banner(title, author, version, site, github, year)  """
            
        self.cls()
        if site !=  '':
            site = ' | ' + site
        ascii_art = f"""     
{Fore.LIGHTCYAN_EX}     .-----.     
{Fore.LIGHTCYAN_EX}   .' -   - '.      
{Fore.LIGHTCYAN_EX}  /  .-. .-.  \     
{Fore.LIGHTCYAN_EX}  |  | | | |  |     
{Fore.LIGHTCYAN_EX}   \ \o/ \o/ /      {title}
{Fore.LIGHTCYAN_EX}  _/    ^    \_     Author:{Fore.YELLOW} {author}{site} {Fore.RESET}
{Fore.LIGHTCYAN_EX} | \  '---'  / |    Version: {Fore.LIGHTBLUE_EX}{version}{Fore.RESET}
{Fore.LIGHTCYAN_EX} / /`--. .--`\ \    Created: {Fore.LIGHTBLUE_EX}{year}{Fore.RESET}
{Fore.LIGHTCYAN_EX}/ /'---` `---'\ \   Github: {Fore.LIGHTBLUE_EX}{github}{Fore.RESET}
{Fore.LIGHTCYAN_EX}'.__.       .__.'   
{Fore.LIGHTCYAN_EX}    `|     |`       
{Fore.LIGHTCYAN_EX}     |     \        Press {Fore.LIGHTRED_EX}ctrl+c{Fore.LIGHTCYAN_EX} to exit{Fore.RESET} 
{Fore.LIGHTCYAN_EX}     \      '--.        
{Fore.LIGHTCYAN_EX}      '.        `\      
{Fore.LIGHTCYAN_EX}        `'---.   |      
{Fore.LIGHTCYAN_EX}              ) /       
{Fore.LIGHTCYAN_EX}              \/ """
        print(ascii_art)
        sleep(0.5)
        self.cls()
    
    
    def exit_handler(self):
        """Handles exiting the program (ctrl+c)"""
        signal(SIGINT, self.handle_exit)

    def handle_exit(self, signal_received=None, frame=None):
        """Handles exiting the program
        Usage: handle_exit()
        Default exit timer is 5 seconds edit it by changing self.exit_timer """
        self.cls()
        for i in range(self.exit_timer):
            print(Fore.LIGHTRED_EX+f'Exiting in {self.exit_timer-i} seconds'+Fore.RESET, end='\r')
            sleep(1)
        exit(0)
    
    def set_title(self, title):
        """Set Tittle Of Console"""
        system(f'title "{title}"')
    
    def hide_cursor(self):
        """Hide Cursor From Console"""
        hide()

    def show_cursor(self):
        """Show Cursor From Console"""
        show()

    def color(self, text, color):
        """Prints a colored text.
        Usage: color(text, color)"""
        print(colored(text, color))

            
Cloud = CloudTools()