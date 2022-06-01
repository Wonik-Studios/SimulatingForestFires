from Simulation import Simulation

# the ignition is the probability for which a nearby tree will catch on fire
# burnout is the probability that a tree will completely burnout in a single generation
# the density is the probability that a cell will contain vegetation at the start of the simulation
# Please read the study at: https://iopscience.iop.org/article/10.1088/1742-6596/285/1/012038/pdf#:~:text=The%20cellular%20automata%20model%20is,as%20the%20burning%20cells%20persist.
# for more context.

# 
settings = {"ignition": 0.5, "burnout": 0.2, "density": 0.7, "wind-angle": 30, "wind-power": 0.3}

simulation = Simulation(800, 600, 2, settings)
simulation.run()
