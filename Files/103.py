__import__('102')   
def say_sup():
    print(f"Sup! my __name__ is {__name__}")

say_sup()

# HI! my __name__ is _102
# u are not in 102
# Sup! my __name__ is __main__


"""
When you use import
1) Tries to find the module (if it fails, it throws an error),
2) Runs the code inside of the module being imported,
3) Creates variables in the namespace of the file with the import statement.

"""