import keyboard
import eel

#? Interface Functions for python

@eel.expose
def PrintPyLog(*args):
  statement = ""
  for i in args: statement += str(i) + " "
  print(f"#JS-Log: {statement}")