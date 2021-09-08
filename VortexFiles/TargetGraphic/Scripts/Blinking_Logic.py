import math


def on_simulation_start(self):
    pass


def pre_step(self):
    time_step = self.getApplicationContext().getSimulationTime()
    self.outputs.Opacity_Factor.value = abs(2 * math.sin(time_step*3))
    pass