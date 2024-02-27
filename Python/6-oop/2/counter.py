class Counter:

    counters=0
    def __init__(self):
        self.count=0
    
    def increment(self):
        self.count+=1
    
    def display_count(self):
        print(f'Total: {self.count}')

    @staticmethod # This tells that the following function is a static method
    def counter_increment():
        Counter.counters+=1

    

# we are targeting the variable that is connected class not with object of class, so the value of variable will not change even we created a new class.
c1=Counter()
c1.counter_increment()
c1.counter_increment()
c1.counter_increment()
print(c1.counters)
c2=Counter()
print(c2.counters)