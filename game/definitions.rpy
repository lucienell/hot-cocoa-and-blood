init -1 python:
    def callback_fn(event, what, interact=True, character="narrator", **kwargs):
        global speaker
        speaker = character

default speaker = "narrator"
define dom = Character(_("Leïla"), who_color="#60afff", callback=callback_fn, cb_character="dom")
define sub = Character(_("Amélie"), who_color="#d11e02", callback=callback_fn, cb_character="sub")
define narrator = Character(None, callback=callback_fn, cb_character="narrator")

image txt_narrator = Image("gui/textbox_narrator.png", xalign=0.5, yalign=1.0)
image txt_dom = Image("gui/textbox_dom.png", xalign=0.5, yalign=1.0)
image txt_sub = Image("gui/textbox_sub.png", xalign=0.5, yalign=1.0)