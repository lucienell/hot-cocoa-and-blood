init -1 python:
    def callback_fn(event, what, interact=True, character="narrator", **kwargs):
        global speaker
        speaker = character

layeredimage sub:
    xzoom -1.0
    zoom 1.1
    attribute base default
    attribute naked:
      Null()
    group clothes auto:
      attribute pyjama default:
        when not naked
    group eyes auto:
      attribute neutral default
    group eyebrows auto:
      attribute neutral default
    group mouth auto:
      attribute smile default
    attribute blush
    attribute blindfold
    attribute ring_gag
    attribute hair default
    attribute hand default
    attribute collier
    attribute harnais_naked
    attribute harnais_blouse

layeredimage dom:
    xzoom -1.0
    zoom 1.1
    crop (0,0,1.0, 830)
    attribute work:
      Null()
    attribute outside:
      Null()
    attribute base default
    group clothes auto:
      attribute pyjama default:
        when not work
      attribute blouse default:
        when work or outside
    group eyes auto:
      attribute neutral default
    group eyebrows auto:
      attribute neutral default
    group mouth auto:
      attribute simplesmile default:
        when not work
      attribute mask default:
        when work
    attribute blush
    attribute sadism
    attribute hair default
    attribute knife
    attribute gloves default:
      when work
    attribute arm_chamber default:
      when not (outside or knife or work)

layeredimage letter:
    zoom 0.61
    attribute image default

layeredimage depressedsub:
    xzoom -1.0
    zoom 1.1
    attribute beginning
    attribute leilaarrive
    attribute grimace
    attribute tears
    

default speaker = "narrator"
define letter = Character(image="letter")
define depressedsub = Character(_("Amélie"), who_color="#d11e02", callback=callback_fn, cb_character="depressedsub", image="depressedsub")
define dom = Character(_("Leïla"), who_color="#60afff", callback=callback_fn, cb_character="dom", image="dom")
define sub = Character(_("Amélie"), who_color="#d11e02", callback=callback_fn, cb_character="sub", image="sub")
define narrator = Character(None, callback=callback_fn, cb_character="narrator")

image txt_narrator = Image("gui/textbox_narrator.png", xalign=0.5, yalign=1.0)
image txt_dom = Image("gui/textbox_dom.png", xalign=0.5, yalign=1.0)
image txt_sub = Image("gui/textbox_sub.png", xalign=0.5, yalign=1.0)
