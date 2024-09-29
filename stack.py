class Stack:
    def __init__(self) -> None:
        #YOU CAN (AND SHOULD!) MODIFY THIS FUNCTION
        self.li=[]
        pass
    def isempty(self) -> bool:
        if(len(self.li)==0):
            return True
        else:
            return False
        pass
    def top(self):
        if not self.isempty():
            return self.li[-1]
    def pop(self):
        if not self.isempty():
            return self.li.pop()
        pass
    def push(self, element):
        self.li.append(element)
        pass
    # You can implement this class however you like