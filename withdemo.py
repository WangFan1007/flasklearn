class WithDemo:

    def __init__(self,name):
        self.name = name


    def __enter__(self):
        print('enter')
        return self

    def __exit__(self,exc_type,exc_value,traceback):
        print('exit')

    def doSomeThing(self):
        print('do something',self.name)


with WithDemo("王凡") as demo:
    demo.doSomeThing()


print(__name__)