example = "Hello world" # Global scope


def local_ex():

    def inner_function():
        return "inner function"

    example = "this is a string" # Local scope
    return example


print(example)
print(local_ex())
