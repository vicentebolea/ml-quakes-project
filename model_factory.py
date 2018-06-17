class ModelFactory:
    """
    Abstract class which expects its subclasses to overload create_model method
    """

    def __init__(self, dim):
        self.model = create_model()
        self.dim = dim
 
    def create(self):
        pass

    @property
    def model(self):
        return self.model

