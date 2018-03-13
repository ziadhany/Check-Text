#check  http://www.wdylike.appspot.com/?q=
import urllib
import urllib.request
def Check_word(Text):
    Text = Text.split(' ')
    for word in Text :
     url = "http://www.wdylike.appspot.com/?q=" + str(word)
     conection = urllib.request.urlopen(url)
     output = conection.read()
     conection.close()
     if output == b'false':
        # word + "->false"
        pass
     else:
         return (True)
    return (False)
def Check_File(File):
  My_File = open(File,'r')
  for line in My_File:
     text = My_File.readline()
     if Check_word(text) == True:
        return True
  My_File.close()
  return False
