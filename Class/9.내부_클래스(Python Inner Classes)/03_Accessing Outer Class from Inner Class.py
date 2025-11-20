class Outer:
    def __init__(self):
        self.name = "겨우리"
        
    class Inner:
        def __init__(self, outer):
            self.outer = outer
            
        def display(self):
            print(f"Outer class name : {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()