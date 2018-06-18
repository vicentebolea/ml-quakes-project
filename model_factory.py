class ModelFactory:
    """
    Abstract class which expects its subclasses to overload create_model method
    """

    def __init__(self, dim):
        self.model = self.create()
        self.dim = dim

    def create(self):
        pass

    @property
    def model(self):
        return self.model

