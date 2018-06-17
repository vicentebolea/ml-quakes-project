from model_depth     import ModelDepth
from model_time      import ModelTime
from model_location  import ModelLocation
from model_magnitude import ModelMagnitude

def model_create(which):
    if which == 'model_depth':
        return ModeDepth()

    if which == 'model_time':
        return ModeTime()

    if which == 'model_location':
        return ModeLocation()

    if which == 'model_magnitude':
        return ModeMagnitude()
