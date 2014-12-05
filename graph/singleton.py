class Singleton:

    def __init__(self, decorated_class):
        self._decorated = decorated_class

    def get_instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Instance must be accessed using "get_instance()"')
