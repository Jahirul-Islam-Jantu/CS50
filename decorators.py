 # In python Function can be use as an value of another function, function can be use as value , can be use as parameter also.

def announce(f):
  def wrapper():
    print("About to run the function")
    f()
    print("Done with the function")
  return wrapper

@announce
def hello():
    print("Hello World!")
hello()

