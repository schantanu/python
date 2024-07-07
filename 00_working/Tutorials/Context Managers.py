# %%

# with <context-manager>(<args>) as <variable-name>:
### Run your code here
### This code is running "inside the context"

# This code runs after the context is removed


with open("my_file.txt") as my_file:
    text = my_file.read()
    length = len(text)

print("The file is {} characters long".format(length))


with open("my_file.txt") as file:
    text = file.read()

n = 0
for word in text.split():
    if word.lower() in ["text", "texts"]:
        n += 1

print(f'Lewis Carroll uses the word "cat" {n} times')


# You may have noticed there was no as <variable name> at the end of the with statement
# in timer() context manager. That is because timer() is a context manager that does not
# return a value, so the as <variable name> at the end of the with statement isn't necessary.
# In the next lesson, you'll learn how to write your own context managers like timer().

with timer():
    print("Pytorch version")
    process_with_pytorch(image)


# %%

# How to create context manager
from contextlib import contextmanager


# @contextlib.contextmanager
# def my_context():
#     # Add any setup code you need (optional)
#     yield
#     # Add any teardown code you need (optional)


# For example
@contextmanager
def my_context():
    print("Hello")
    yield 42
    print("Goodbye")


with my_context() as foo:
    print("foo is {}".format(foo))


# %%
import time
import contextlib

# Add a decorator that will make timer() a context manager
@contextlib.contextmanager
def timer():
    """Time the execution of a context block.

  Yields:
    None
  """
    start = time.time()
    # Send control back to the context block
    yield
    end = time.time()
    print("Elapsed: {:.2f}s".format(end - start))


with timer():
    print("This should take approximately 0.25 seconds")
    time.sleep(0.25)

# image = get_image_from_instagram()

# # Time how long process_with_numpy(image) takes to run
# with timer():
#   print('Numpy version')
#   process_with_numpy(image)

# # Time how long process_with_pytorch(image) takes to run
# with timer():
#   print('Pytorch version')
#   process_with_pytorch(image)

# %%
import contextlib


@contextlib.contextmanager
def open_read_only(filename):
    """Open a file in read-only mode.

  Args:
    filename (str): The location of the file to read

  Yields:
    file object
  """
    read_only_file = open(filename, mode="r")
    # Yield read_only_file so it can be assigned to my_file
    yield read_only_file
    # Close read_only_file
    read_only_file.close()


with open_read_only("my_file.txt") as my_file:
    print(my_file.read())


# %%
