# AI-Generated Repository

This repository was created entirely by LLMs. The application was generated using Goose using only the free trier of ChatGPT 4-o, and the README.md file was written by Cursor.

## Prompts Used in Goose

**Initial Prompt**

"Create a simple game of life simulation in a new folder. Upon starting the program, the user should be able to edit the initial state of the field by toggling the "pixels" (they should be enlarged to be visible). Once the user is ready, he clicks the "run simulation" button, and the Game of Life simulation starts according to Conway's famous rules. One iteration is 1 second long so it's followable. When the simulation is running, the user can press a "pause" button, and can step forward or back in time between iterations with a back and forward arrow button. The STOP button stops the simulation and switches back to the initial state editing mode. When the simulation is running, there's a counter that shows the current iteration's number."

**Refinements and Bug Fixes**

* "Add the control interface so i don't need to use the keyboard"
* "Buttons don't seem to work"
* "Remove the step back button for now, and add the iteration counter display, starting from 0"
* "There's no counter at the bottom (or anywhere)"
* "Try again"
* "Still no counter displayed"
* "Check my Game of Life window, there's no counter displayed" *(Goose can have access to running apps' windows)*
* "Everything works great! now, last task, make it look BEAUTIFUL, sleek, modern, colorful interface, everything. it should look like a well polished apple app."
* "Check out how it looks now, and fix the problem"
* "Uh oh, error message.
``python game_of_life/game_of_life.py
pygame 2.6.1 (SDL 2.28.4, Python 3.12.8)
Hello from the pygame community. https://www.pygame.org/contribute.html
Traceback (most recent call last):
  File "/Users/eszpee/projects/goose/game_of_life/game_of_life.py", line 161, in <module>
    main()
  File "/Users/eszpee/projects/goose/game_of_life/game_of_life.py", line 134, in main
    draw_control_panel()
  File "/Users/eszpee/projects/goose/game_of_life/game_of_life.py", line 80, in draw_control_panel
    window.blit(iteration_text, (WIDTH - 250, WINDOW_SIZE + 70))
                                 ^^^^^
NameError: name 'WIDTH' is not defin`` " *(yes, I accidentally left out the end of the error)*
* "Improving, but the text is still too big for the buttons, check my screen"

And that's it, after the last message Goose could figure out proper sizing. 

## Prompt used in Cursor

Once I had the game_of_life.py file ready, I only used one command in Cursor: 

* "create a readme file in the repo"

## Software Used

* [Goose](https://block.github.io/goose/)
* [Cursor](https://www.cursor.com/)

This is the only manually edited file in the repository, but even formatting adjustments were made by Cursor's LLM integration.
