from math import sqrt
import Vortex

WIDTH_SCALING = 5


def on_simulation_start(extension):
    extension.sensor = extension.getInput('sensor').value
    extension.graphic_interface = extension.getInput('graphic_interface').value

def post_step(extension):


    intersected = extension.sensor.getOutput('Has Intersected').value
    if intersected:
        intersection_point = extension.sensor.getOutput('Intersection Point').value
        origin = extension.sensor.getOutput('Ray')['Origin'].value
        diff = intersection_point - origin
        distance = sqrt(diff.x**2 + diff.y**2 + diff.z**2)
        green = (distance/10.0)
        red = (10 - distance/10.0)
        local = extension.graphic_interface.getInput('Local Transform').value
        extension.graphic_interface.getInput('Local Transform').value = Vortex.scaleTo(local, Vortex.VxVector3(distance/10.0,
                                                                                                               WIDTH_SCALING,
                                                                                                               WIDTH_SCALING))

    else:
        green = 1
        red = 0
        local = extension.graphic_interface.getInput('Local Transform').value
        extension.graphic_interface.getInput('Local Transform').value = Vortex.scaleTo(local, Vortex.VxVector3(1, 
                                                                                                               WIDTH_SCALING,
                                                                                                               WIDTH_SCALING))

    extension.graphic_interface.getInput('Color').value = Vortex.VxColor(red, green, 0,1)

