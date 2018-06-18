class ModelFactory:
    """
    Abstract class which expects its subclasses to overload create_model method
    """

    def __init__(self, dim):
        self.dim = dim
        self.model = self.create()
 
    def create(self):
        pass

    @property
    def model(self):
        return self.model

