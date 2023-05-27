# Simulating Forest Fires
![FFS Preview Image](https://resources.wonik.info/projectmedia/forestfiresim/preview.gif)


This README file will only focus of the usage of the software. If you are looking for writing about the project vision, please refer to the project at https://wonik.info/projects/forest-fire-simulation.

Forest Fire Simulator is a program that uses Cellular Automaton to simulate forest fires with surprising accuracy. This project was the result of our attempt to try to improve a similar study that simulates forest fires.

# Installation
The repository can be cloned by cloning the repository from https://github.com/Wonik-Studios/SimulatingForestFires or by running the following commands in the terminal:

  ```
  git clone "https://github.com/Wonik-Studios/SimulatingForestFires.git"
  ```
then you can download all the requirements from “requirements.txt” with:

  ```
  pip install -r SimulatingForestFires/requirements.txt
  ```
Now, to run the code you can do:

  ```
  python SimulatingForestFires/Main.py
  ```
You will be prompted for the parameters before the simulation starts. Also, do note that you will have to have python and pip installed to run the code.

If instead, you would like to run the code in a program, you’ll have to set the parameters in a dictionary, import the Simulation class from the Simulation.py file, create an instance of the Simulation class and call the run function on it.

The Simulation object’s parameters are (xPixels, yPixels, cellPixelWidth, settings). The settings variable should be a dictionary with “ignition”, “burnout”, “density”, “wind-angle”, “wind-power” as keys.

Example
```python
  settings = {"ignition": 0.5, "burnout": 0.2, "density": 0.7, "wind-angle": 180, "wind-power": 50}
  simulation = Simulation(800, 600, 2, settings)
  simulation.run()
```

# Developers

These are the lead Wonik team members who worked on this project:

Nathan Kim: https://github.com/MobBarley2021

rts4: https://github.com/rts4

Aryan Zafer: https://github.com/petal-person
