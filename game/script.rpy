# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
## Definitions moved to definitions.rpy

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
        "this is a temporary menu to test the game, you can jump to any chapter and play as intended"

        "introduction":
            jump sc0
            
        "breakfast":
            jump sc1

        "meeting":
            jump sc2

        "kink arrive":
            jump sc3

        "past of leila":
            jump sc4

        "figth":
            jump sc5

        "distance":
            jump sc6

        "nomoreBDSM":
            jump sc7

        "quit":
            return


    label sc0:
    call introduction

    label sc1:
    call breakfast

    label sc2:
    call meeting

    label sc3:
    call kinkArrive

    label sc4:
    call pastleila

    label sc5:
    call fight

    label sc6:
    call distance

    label sc7:
    call nomoreBDSM

    label sc8:
    call stayinghome

    return
