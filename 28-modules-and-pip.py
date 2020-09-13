# Can't use normal import because of hyphens and filename starting with a number
# import useful_tools
import importlib

useful_tools = importlib.import_module("28-module-useful-tools")

print(useful_tools.roll_die(12))
print(useful_tools.beatles)
print(useful_tools.get_file_ext("my_script.py"))
