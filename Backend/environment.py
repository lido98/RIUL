# from backend.Trie.trie import Trie, VectorialMatrix
import os

def clean_screen():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

class Environment:
    trie: object
    matrix: object
    console: list   

    def reset_console():
        clean_screen()
        for line in Environment.console:
            print(line, end="")