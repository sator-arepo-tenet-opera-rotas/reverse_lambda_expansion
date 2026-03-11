import pip
from functools import wraps

def install(package):
    if hasattr(pip, "main"):
        pip.main(["install", package])
    else:
        pip._internal.main(["install", package])

def requires(package):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            install(package)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@requires("argh")
def main():
    import argh
    print("argh imported successfully")

if __name__ == "__main__":
    main()
