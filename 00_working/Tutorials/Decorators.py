#%%

printmystring = print

printmystring("Test")
print("Test")
print(print)
print(print())


# %%


def get_function():
    def print_me(s):
        print(s)

    return print_me


new_func = get_function()
new_func("This is a sentence.")


# %%
