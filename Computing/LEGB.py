# Namespace of Python
# LEGB

# dy/dx = f(x, y)

# global variable

x1 = "global"

def dy():

    x1 = 'enclosing'

    def dx():

        x1 = 'local'

        print(x1)
        return

    dx()

    return

dy()

