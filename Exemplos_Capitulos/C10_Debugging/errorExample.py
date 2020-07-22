import traceback


def spam():
    bacon()


def bacon():
    raise Exception('This is the error message')


try:
    spam()
except:
    with open('errorInfo.txt', 'w', encoding='UTF-8') as errorFile:
        errorFile.write(traceback.format_exc())
        print(f'The traceback info was written to errorInfo.txt')
