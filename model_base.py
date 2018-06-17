class model_base:
    def __init__(self):
        self.model = create_model()

    def create_mode(self):
        pass

    @property
    def model(self):
        return self.model

