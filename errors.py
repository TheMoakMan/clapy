DIM_ERR = "Input matrix does not match specified dimensions."

class DimError(Exception):
    def __init__(self, msg=DIM_ERR):
        pass