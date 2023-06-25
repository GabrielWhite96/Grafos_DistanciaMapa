import os
import time

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def timer(seconds):
    time.sleep(seconds)
    
def imprimeLinha():
    print("================================")