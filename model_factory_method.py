from model_depth import ModelDepth
from model_time import ModelTime
from model_location import ModelLocation
from model_magnitude import ModelMagnitude


def model_create(which, dim):
    if which == 'model_depth':
        return ModelDepth(dim)

    if which == 'model_time':
        return ModelTime(dim)

    if which == 'model_location':
        return ModelLocation(dim)

    if which == 'model_magnitude':
        return ModelMagnitude(dim)
