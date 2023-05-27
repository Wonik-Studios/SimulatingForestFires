from Simulation import Simulation

# Made by Wonik
# https://wonik.tech
# Notable Developers: Nathan Kim, Joshua Gallinger, Aryan Zafer

# the ignition is the probability for which a nearby tree will catch on fire
# burnout is the probability that a tree will completely burnout in a single generation
# the density is the probability that a cell will contain vegetation at the start of the simulation
# Please read the study at: https://iopscience.iop.org/article/10.1088/1742-6596/285/1/012038/pdf#:~:text=The%20cellular%20automata%20model%20is,as%20the%20burning%20cells%20persist.
# for more context.

# The wind-power should be a value that ranges from 0-100 where 100 is maximumm wind and 0 is when
# there is no wind in an environment. This is a demo of how to run the simulation:
settings = {}
prompts = (
("ignition", "Input the Ignition [0, 1]", 0, 1),
("burnout", "Input the burnout [0, 1]", 0, 1),
("density", "Input the density [0, 1]", 0, 1),
("wind-angle", "Input the wind-angle [0, 360]", 0, 360),
("wind-power", "Input the wind-power [0, 100]", 0, 100)
)


def getInput(key, msg, lower, upper):
    print(msg)
    while(True):
        try:
            result = float(input(">>"))
        except ValueError:
            print("Sorry, your input wasn't formatted properly")
            continue

        if result >= lower and result <= upper:
            break
        else:
            print("Sorry, your input was not within the appropriate bounds.")
    settings[key] = result


for prompt in prompts:
    getInput(prompt[0], prompt[1], prompt[2], prompt[3])

print("Starting Simulation...")

simulation = Simulation(800, 600, 2, settings)
simulation.run()
