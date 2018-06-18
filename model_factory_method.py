from model_depth import ModelDepth
from model_time import ModelTime
from model_location import ModelLocation
from model_magnitude import ModelMagnitude


def model_create(which):
    if which == 'model_depth':
        return ModelDepth()

    if which == 'model_time':
        return ModelTime()

    if which == 'model_location':
        return ModelLocation()

    if which == 'model_magnitude':
        return ModelMagnitude()
