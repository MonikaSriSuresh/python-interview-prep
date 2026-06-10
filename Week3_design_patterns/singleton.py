class Logger:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            print("Creating Logger Object")
            cls._instance = super().__new__(cls)

        return cls._instance


logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)
print(id(logger1))
print(id(logger2))
