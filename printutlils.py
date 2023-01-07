def colourstring(colour,instring):
  END = "\033[0m"
  if colour == "red":
    colourc = "\033[0;31m"
  elif colour == "green":
    colourc = "\033[0;32m"
  elif colour == "brown":
    colourc = "\033[0;33m"
  elif colour == "blue":
    colourc = "\033[0;34m"
  elif colour == "purple":
    colourc = "\033[0;35m"
  elif colour == "cyan":
    colourc = "\033[0;36m"
  else:
    colourc = "\033[0;30m"

  newstring = colourc + instring + END
  
  return newstring
