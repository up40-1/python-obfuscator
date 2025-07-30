import marshal
import random
import string
import sys
import os
import datetime
import colorama
import shutil
import time
import requests as r
import tkinter as tk
from tkinter import filedialog
import ctypes

color = colorama.Fore
red = color.RED
white = color.WHITE
green = color.GREEN
reset = color.RESET
BEFORE = f'{red}[{white}'
AFTER = f'{red}]'
INPUT = f'{BEFORE}>{AFTER} |'
INFO = f'{BEFORE}!{AFTER} |'
ERROR = f'{BEFORE}x{AFTER} |'
ADD = f'{BEFORE}+{AFTER} |'
WAIT = f'{BEFORE}~{AFTER} |'

ws = 'https://fakecrime.bio/up40'
github = 'https://github.com/up40-1'
discord = 'https://discord.com/users/1248748238555713641'
by = 'up40'
version = '1.2 Release'
title = f'up40 v{version} - Obfuscator Tool'
folder = 'up40-Obfuscator'
output_folder_1 = folder + '/Script-Obfuscate'
script_folder = folder + '/Script'

ascii_art = f"""
                                                               _  _    ___  
                                                              | || |  / _ \ 
                                                    _   _ _ __| || |_| | | |
                                                   | | | | '_ \__   _| | | |
                                                   | |_| | |_) | | | | |_| |
                                                    \__,_| .__/  |_|  \___/ 
                                                         | |                
                                                         |_|                                                                                
                        ┌──────────────────────────────────────────────────────────────────────────┐
                        ├─ Website  : {ws}                                   │
                        ├─ Discord  : {discord}                │
                        ├─ GitHub   : {github}                                   │
                        ├─ Made by  : {by}                                                         │
                        ├─ Version  : {version}                                                  │
                        └──────────────────────────────────────────────────────────────────────────┘
"""

def current_time_hour():
    return datetime.datetime.now().strftime('%H:%M:%S')

def Title(title_choice):
    if sys.platform.startswith('win'):
        ctypes.windll.kernel32.SetConsoleTitleW(f'{title} | {title_choice}')
    elif sys.platform.startswith('linux'):
        sys.stdout.write(f'up40 - Obfuscator Tool | {title_choice}\a')

def Clear():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def ChoosePythonFile():
    try:
        print(f'{BEFORE + current_time_hour() + AFTER} {INPUT} Choose a python file -> {reset}')
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        python_file = filedialog.askopenfilename(parent=root, title=f'{title} | Choose a python file (.py)', filetypes=[('PYTHON files', '*.py')])
    except Exception as e:
        print(f'{ERROR} {str(e)}')
        return None
    else:
        return python_file

def random_var(used_vars, number=10):
    while True:
        rdm_var = ''.join(random.choices(string.ascii_letters, k=number))
        if rdm_var not in used_vars:
            used_vars.add(rdm_var)
            return rdm_var

def layer_1(script):
    anti_kids_code = '\ntry:\n    up40\n    up40\n    _up40_\nexcept:\n    import sys\n    input("ERROR: The obfuscated code was modified. To avoid reproducing an error, please do not modify the obfuscated code.")\n    sys.exit()\n'
    script = anti_kids_code + script
    return script

def layer_2(script, size_1, size_2):
    used_vars = set()
    for i in range(random.randint(size_1, size_2)):
        var_1 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_2 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_3 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_4 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_5 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_6 = random_var(used_vars, number=random.randint(size_1, size_2))
        script = script + f'\nclass {var_1}:\n def {var_2}({var_3}):\n  {var_4} = {var_3}\n  {var_5} = {var_4}\n  return {var_5}\n {var_3} = \'{var_6}\'\n {var_5} = {var_2}({var_3})\n{var_1}()\n'
    return script

def layer_3(script):
    used_vars = set()
    key = random.randint(1, 10)
    var_1 = random_var(used_vars)
    var_2 = random_var(used_vars)
    var_3 = random_var(used_vars)
    obfuscated_script = ''.join((chr(ord(c) + key) for c in script))
    script = f'{var_1} = {repr(obfuscated_script)}\n{var_3} = {key}\n{var_2} = \'\'.join(chr(ord(c) - {var_3}) for c in {var_1})\nexec({var_2})'
    return script

def layer_4(script):
    compiled_code = marshal.dumps(compile(script, '<string>', 'exec'))
    script = f'_up40_ = {repr(compiled_code)}\nexec(up40.loads(_up40_))'
    return script

def layer_5(script):
    chunks = [script[i:i + 1000] for i in range(0, len(script), 1000)]
    used_vars = set()
    vars = {random_var(used_vars): repr(chunk) for chunk in chunks}
    code_vars = '\n    '.join((f'{k} = {v}' for k, v in vars.items()))
    script = f"\nclass up40:\n    {code_vars}\n\nimport marshal as up40\nexec(''.join([up40.{', up40.'.join(vars.keys())}]))"
    return script

def obfuscate(script, size_1, size_2):
    script = layer_1(script)
    script = layer_2(script, size_1, size_2)
    script = layer_3(script)
    script = layer_4(script)
    script = layer_5(script)
    return script

def up40_Obfuscator():
    Clear()
    Title(f'By: {by}')
    print(ascii_art)

    file_python = ChoosePythonFile()
    if not file_python:
        print(f'{ERROR} No file chosen.')
        return

    print(f'{BEFORE + current_time_hour() + AFTER} {INPUT} Enter obfuscation strength (1-4):')
    obfuscation_force = input(f'{BEFORE + current_time_hour() + AFTER} {INPUT} Obfuscation Force -> {reset}')
    
    try:
        obfuscation_force = int(obfuscation_force)
    except ValueError:
        print(f'{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid input. Please enter a number between 1 and 4.')
        return
    
    size_1, size_2 = 8, 15
    if obfuscation_force == 2:
        size_1, size_2 = 10, 25
    elif obfuscation_force == 3:
        size_1, size_2 = 30, 50
    elif obfuscation_force == 4:
        size_1, size_2 = 50, 100
    else:
        print(f'{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid number. Please choose between 1-4.')
        return

    if not os.path.exists(output_folder_1):
        os.makedirs(output_folder_1)

    with open(file_python, 'r', encoding='utf-8') as file:
        script = file.read()
    
    script = obfuscate(script, size_1, size_2)

    output_path = f'{output_folder_1}/{file_python.split("/")[-1]}'
    with open(output_path, 'w', encoding='utf-8') as obfuscated_file:
        obfuscated_file.write(script)
    
    print(f'{INFO} {green}Obfuscation completed! {white}File saved at: {output_path}')
    input(f'{BEFORE + current_time_hour() + AFTER} Press any key to exit.')

if __name__ == '__main__':
    up40_Obfuscator()
