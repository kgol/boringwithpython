import traceback

def spam():
    bacon()
    
def bacon():
    raise Exception('This is the error message')

try:
    spam()
except:
    errorFile = open('errorinfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('tre traceback info was written to errorinfo.txt')