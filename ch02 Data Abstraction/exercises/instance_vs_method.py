class InstanceVsMethod(object):

    def __init__(self):
        # self.fruit = 'banana'
        pass

    def fruit(self):
        return 'banana'


c = InstanceVsMethod()

print(c.fruit())
