import model_depth
import model_time
import model_location
import model_magnitude

def model_create(which):
    if which == 'model_depth':
        return mode_depth()

    if which == 'model_time':
        return mode_time()

    if which == 'model_location':
        return mode_location()

    if which == 'model_magnitude':
        return mode_magnitude()
