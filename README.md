<h1 align="center">
    Workshop - AI Pacman
</h1>

<p align="center">
    <img width="1200" height="300" src="https://upload.wikimedia.org/wikipedia/fr/thumb/a/a2/Pac-Man_Logo.svg/1280px-Pac-Man_Logo.svg.png">
</p>
<br>

<h3 align="center">
    The goal of this workshop is to create the artificial intelligence of all pacman's ghost.
</h3>
<br><br>

### **What's Pacman?**

Pac-Man, an emblematic character in the history of video games, is a character in the shape of a yellow circle with a mouth. He has to eat pac-gums in a maze haunted by four ghosts.<br>

### **What's an AI?**

Artificial Intelligence (AI) is "the set of theories and techniques used to create machines capable of simulating intelligence".<br> 
Often classified in the cognitive sciences group, it involves computational neurobiology (particularly neural networks), mathematical logic (part of mathematics and philosophy) and computer science. She is looking for methods to solve problems with high logical or algorithmic complexity.<br><br>

# **Initialization**

In a first time, you need to clone the workshop repo with:
```
git clone git@github.com:nathan-hoche/WorkshopPacman.git
```

Now you can launch the game with:
```
python3 Pacman.py
```

> You need tkinter module for this workshop.<br>
> If you don't have him, install him with:
```python
sudo apt-get install python3-tk
or
sudo dnf install python3-tkinter
```
<br><br>

# **Command**

You can use all this command to program the AI:

> All of this commands is present in user module.

* This function returns the size of your screen
```python
get_size_screen()
```
* This function returns the position of player
```python
get_pos_player()
```
* This function returns map
```python
get_map()
```
* This function moves the ghost upwards ( set the color of ghost )
```python
move_ghost_up()
```
* This function moves the ghost down ( set the color of ghost )
```python
move_ghost_down()
```
* This function moves the ghost letf ( set the color of ghost )
```python
move_ghost_left()
```
* This function moves the ghost right ( set the color of ghost )
```python
move_ghost_right()
```

<br><br>

# **Objective**

The goal of the project is to code the artificial intelligence of a Pacman game which must win every time and for that it is necessary to modify the "IA.py". The particularity is that there are four different AI coded for each ghost independently.

Each ghost has its own behavior:

    Blinky (RED) attacks directly Pac Man. He follows Pac-Man like his shadow.
    Pinky tends (PINK) to ambush. She aims at where Pac-Man is going to be.
    Inky (BLUE) is capricious. From time to time, he leaves in the opposite direction to Pac-Man.
    Clyde (ORANGE) feigns indifference. From time to time, he chooses a direction at random (which can be that of Pac-Man).

> As for Clyde, the orange ghost, his movement seems purely random, but some clever guys who dissected the game's source code realized that he always leaves towards the lower left corner of the board when he's too close to Pac-Man.<br>

Like this example:<br>

## **Exemple**

```python
from src.user import user

class launch_ia():
    def __init__(self):
        self.info = user()
        self.x1 = 0
        return

    def main_ia(self):
        if (self.x1 == 0):
            self.info.move_ghost_up("Red")
            self.info.move_ghost_up("Blue")
            self.info.move_ghost_up("Orange")
            self.info.move_ghost_up("Pink")
            self.x1 = 1
        else:
            self.x1 = 0
            self.info.move_ghost_left("Red")
            self.info.move_ghost_left("Blue")
            self.info.move_ghost_left("Pink")
            self.info.move_ghost_left("Orange")
```
> Don't touch other file to programm the AI.

# **Tips**

Here is the size of the different elements:<br>
* The Arena: 760 x 840
* Block's size: 40 x 40

<br><br>


# **To go further**

Here are some examples to go further in the workshop:

* Continue the AI to beat all the players
* Complete and personalize the Pacman
* Recoded the AI of pacman
* Add effects ( musique, level, score... )
