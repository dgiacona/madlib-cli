print("Welcome to Madlib")

def read_template(filepath):
  with open(filepath) as file:
    cont = file.read().strip()
    return cont

def parse_template():
  with open(filepath) as file:
    cont = file.read().strip()
    cont_arr = list(cont.split())
    cont_arr = cont_arr.replace("{Adjective}", "{}")
    cont_arr = cont_arr.replace("{Noun}", "{}")
  return cont_arr

def merge(string, madlibs):
  return string.format(madlibs[0], madlibs[1], madlibs[2])

with open("assets/dark_and_stormy_night_template.txt", 'r') as file:
  charlie = file.read().strip()
  print(list(charlie.split()))