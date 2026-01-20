## Nested functions
## Scopes / Closure
def first():
    ###third() <-- fails
    def second():
        data = 333
        def third():
            return data
        return third()
    return second()
    #data #### <-- wont exist
print(first())
