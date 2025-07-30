def func():
    print("This is a function in module.py")
if __name__ == "__main__":
    print("Module is being run directly")
    func()
    print("name of file:",__name__)  # This will print "__main__" if run directly, or the module name if imported   