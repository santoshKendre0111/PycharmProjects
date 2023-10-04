
# try - except: if try fails, we can continue excepttion part

class Try_Expect:

    def try_exception(self):

        try:
            with open('file.txt', 'r') as reader:
                reader.read()

        except Exception as e:
            print(e)
clobj = Try_Expect()
clobj.try_exception()