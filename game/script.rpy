# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define dom = Character(_("Leïla"), color="#30dada")
define sub = Character(_("Amélie"), color="#f24f4f")

# define positions.
transform right:
    xalign 0.95
    yalign 1.0

transform left:
    xalign 0.05
    yalign 1.0

define config.nvl_list_length = 10
define gui.nvl_height = None
define gui.nvl_borders = Borders(0, 100, 0, 0)

# List all chapter in order


# The game starts here.

label start:

    # scenes menu
    menu:
        "this is a temporary menu to test de game, you can jump to any chapter and play as intended"

        "introduction":
            jump sc0
            
        "breakfast":
            jump sc1

        "meeting":
            jump sc2


        "kink arrive":
            jump sc3

        "quit":
            return


    label sc0:
    call introduction

    label sc1:
    scene bg chapter with fade
    centered "{size=72}Chapter 1"
    call breakfast

    label sc2:
    scene bg chapter with fade
    centered "{size=72}Chapter 2"
    call meeting

    label sc3:
    scene bg chapter with fade
    centered "{size=72}Chapter 3"
    call kinkArrive

    return