import re

def execute_Illuvatar(code):
    lines = code.strip().split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("Illuvatar "):
            content = re.match(r'Illuvatar "(.*)"', line)
            if content:
                print(content.group(1))
            else:
                print("Syntax Error: Use Illuvatar \"message\"")
        else:
            print("Unknown Command: ", line)

# Example Usage
code = """
Illuvatar "Hello world!"
"""
execute_Illuvatar(code)
