# ENVIRONMENT
The Environment package handles the physics simulations for the VAL Simulator. This Package will become obsolete when VAL reaches her robothood. It handles all the information a real environment will, when we put VAL into the real world. For example it generates and handles the physical objects around the robot and checks for collisions between scanners and the walls.

It's important we seperate the environment from virtual things, as when we move into the real world, the environment won't know what's around it, it just reacts to other objects.