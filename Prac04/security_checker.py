"""
CP1404/CP5632 Practical
Bad security checker
"""


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
current_user = str(input("Enter username: "))
if current_user in usernames:
    print("Access granted")
else:
    print("Access denied")
