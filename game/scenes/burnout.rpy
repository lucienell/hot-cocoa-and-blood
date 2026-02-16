label burnout:

    # Music.
    play music "track 04 - introspection.ogg"

    # Show a background
    scene bg mainroom
    with fade
    nvl show dissolve

#Depression - Using BDSM as a crutch.
#Awkward period
#nvl
    nvl_narrator "We tried to patch things up, afterwards.{w} The tension in the air hadn’t entirely dissipated, but it weighed less."
    nvl_narrator "Amélie eventually told me about the events she organised at her bar.{w} I could hear the weariness in her voice:{w} there was none of the excitement she usually displayed when she broached the topic.{w} Furthermore, she often stopped talking in the middle of a sentence."

# Transparent sprite of Amélie, exhausted, in the middle. Play/Bar outfit.
# Background: inspired by Cris et Chuchotements
# Night club music?
    nvl clear
    play music "track 02 - bar.ogg"
    scene bg bar
    with fade

    nvl_narrator "I had seen her behave this way before, when we went to play parties:{w} once they were over, back when it was time to go home and rest,{w} her attitude changed.{w} She would grow exhausted and stop emoting altogether,{w} speaking slowly in a monocorde voice,{w} wholly unlike how she talked but five minutes ago."
# The sprite is euphoric
    nvl_narrator "Throughout the party, she had danced and flirted,{w} made pun after pun,{w} had run from place to place with such excitement;{w} she had spoken to strangers like they were old friends of hers,{w} and she had played again and again,{w} laughing the whole time."

    nvl clear

    nvl_narrator "She felt so happy."
    nvl_narrator "Receiving blows, being tied up, serving, basking in the ambiance…{w} she felt at home."
# Sprite tired
    nvl_narrator "But once the party was over… she was spent, and none of her energy remained."

    play music "track 04 - introspection.ogg"
    scene bg bedroom night
    with fade

    nvl clear

    nvl_narrator """ 
      Despite our talk, we didn’t end up having any sex on that day off, nor on the morrow.{w} We cuddled and we watched a movie, Grave.{w} We cleaned, we cooked, and we played some video games.

      Before we knew it, it was time to go back to work.
    """

    nvl clear

    nvl_narrator """ 
      This week was especially hard.{w} I kept waiting for Amélie to answer my messages on Discord,{w} and I know she kept waiting for my own answers.{w} Furthermore, what little we exchanged over text wasn’t nearly enough to address all our feelings.

      We might very well have fared better had we exchanged by email.

      I felt torn between my love for Amélie and the frustration that had accumulated.{w} My feelings kept nabbing at me, whether I was tending to a corpse or resting at home -{w} the only time when I wasn’t thinking about our relationship must have been when I met the bereaved.{w} Focusing on their grief gave me enough of a reason to forget about my own woes.
    """

    nvl clear

    nvl_narrator """
      I desperately wanted to make things work, and I could not see any way forward.{w} Even the prospect of getting to work during the night shift,{w} to finally have more time together, did not feel like it would solve any problem;{w} only wreck havoc on my body, only make it impossible to make friends with anyone or attend any social event.

      Had nothing happened, I would probably have broken up with Amélie.
    """

    nvl clear
    nvl hide dissolve

    #Evening: Amélie comes home, stops working.
    # Living room. Leïla on a side of the screen, work clothes. Amélie appears, crying sprite, and goes through the screen before disappearing.
    show sub exhaustedtears sourcil blouse bigfrown at right
    "One evening, however, I was surprised to see Amélie come home at 8pm. She hadn’t sent me any message. Her eyes were red, and her face was marked with tears."
    "Without a word, she went to our room and rolled in a ball on top of our bed."
    # Bedroom : Dark. Amélie’s sprite, facing away from where she looks, still crying.
    "She hadn’t turned on the light, and so she was lying in the darkness."
    # Leïla enters and comes near her sprite.
    show dom worry littlefrown open at left
    "I approached her softly and held her hand in mine."
    show sub embarassed
    "She held me tight, unable to speak, but clearly not willing to let me go."
    dom "Did anything happen, sweetie?"
    "She nodded."
    dom "Do you want to talk about it?"
    "She shook her head."


    nvl show dissolve
    nvl_narrator """
      I caressed her hair, and her body seemed to relax;{w} she started breathing more evenly,{w} and I noticed that, until then, she had been mostly holding her breath.

      We stayed here for a while, lying in the dark.

      Even though she was obviously upset,{w} it felt good to be able to hold her against me like that.
    """
    nvl clear
    nvl hide dissolve


    # Some time passes. Amélie speaks in a low voice, smaller font than usual. Her name has a very dull colour.
    sub "…I… broke down at work."
    "I let her talk, brushing her hair in silence."
    sub "…there was a problem with a performance."
    sub " The gal I had talked with couldn’t come, and we had to improvise something last minute, and…{w} apparently it was a bad idea to do some fireplay, even on the stage…{w}"
    sub "And Mar wouldn’t get off my case, because she swears she knows the girl and that she’s an abuser…{w} and I couldn’t take it in the end."
    sub "Broke a glass in my hand.{w} Went home.{w} Don’t know if…{w} I’ll be able to come back…"
    sub "I’m just so tired…"

    scene bg introspection
    with fade

    play music "track 04 - introspection.ogg" if_changed

# Introspection
    nvl show dissolve

    nvl_narrator """
      Despite her fears, she still had a job to come back to, and I couldn’t tell whether she was relieved or not.
 
      We still had some days until our time off,{w} and I did not have much of an occasion to be with Amélie until then.

      However, the incident pushed me to investigate and look through the chatlogs of the Discords I knew she frequented.{w} It’s on the “Transfeminine Support Group” that I noticed that Amélie had been in a number of fights with people who I knew were her friends over the last weeks.
    """
    nvl clear 
    nvl_narrator """
      Her tone was consistently sarcastic.{w} She complained that people talked in the wrong channel,{w} never bothered to give sources for pictures,{w} couldn’t look for information that had already been pinned,{w} and she answered very defensively to any criticism.

      It felt so… strange to see how badly some of those situations grew.

      Incidents so banal and unimportant ended up needing the attention of moderators to put the channel in time-out.
    """
    nvl clear
    nvl_narrator """
      The last one was especially bizarre:{w} a discussion on the representation of trans women in drag,{w} harmful depictions in popular media,{w} reappropriation,{w} pride,{w} between a girl who came from Poland and someone I had seen at the bar,{w} with others occasionally chiming in.

      Hours after the conversation was over,{w} right before she had gone to work,{w} Amélie had written a long message which supported neither party and really looked like she was out for a fight.

      It was truly baffling.

      She had never even cared about drag.
    """

    nvl clear

    nvl_narrator """
      For the first time in what must have been weeks, I decided to go meet her at the bar.{w} Having looked through public chats to research Amélie’s messages,{w} I could not shake the impression that I was behaving like a stalker would,{w} and this made me feel quite uneasy.

      And so, I texted her.{w} I told her I was done with work and that I wanted to see her for a bit, go have dinner together. 

      Still, I didn’t have enough confidence to write{w} \“Hey, I saw that you kept getting into fights and got muted after ranting about drag (???) in #général,{w} is everything okay?\”.{w} It was all too obvious that she would make a mountain out of that,{w} and I dreaded the idea of another fight.
    """
    nvl clear

    scene bg bar
    with fade

    play music "track 02 - bar.ogg"


      # Bar. Amélie’s sprite is transparent because Leïla hasn’t yet interacted with her. Smile sprite variation with lines on the side of the mouth.
    show depressedsub beginning at right

    nvl_narrator """
      Amélie’s lips were too tight around her smile.{w} Anyone who knew her could see that it was forced.{w}

      She was talking to a customer when I entered and hadn’t yet noticed me.{w} The noise muffled the words she spoke, but her tone was clear enough:{w}
      it was cheerful to the point of being euphoric, and so full of cracks.
    """

    nvl_narrator "I stood in the entrance, unsure what to do.{w} I only really came further inside when someone came back from a smoke and needed me to move to enter."

    nvl_narrator "Amélie was {i}wrong{/i},{w} and seeing her like this made my heart ache and my stomach crawl."

    nvl hide dissolve
    nvl clear

    show dom littlefrown worry open outside at left
    "I sat on the barstool."
    dom "Hey sweetie."
    "Amélie turned sharply towards me.{w} For the moment that it took her to realise that I was me, she started going through a prepared speech…"
    sub "Hello and welcome to our Cabaret, how may -"
    # her smile fades. She looks tired.
    show depressedsub -beginning leilaarrive
    "…which she dropped all of a sudden when she noticed it was not necessary."
    sub "…Hi babe. Sorry. I’m tired."
    dom "Is there something I can do?"
    show depressedsub -leilaarrive grimace
    sub "I… I don’t know. Do you want a drink? It’s on me."
    dom "Give me a hot chocolate."
    sub "…Haha. I wish I could, but that’s not on the menu."
    dom "Just some lemonade, please."
    sub "Coming up."
    # Small pause
    dom "…when is your break? We can go get some ramen nearby."
    sub "…must be in an hour. Something like… eight and a half…"
    dom "…Amélie, that’s fifteen minutes away."
    sub "…Is it? Man…"
    # Amélie sighs
    sub "…yeah, please. Yeah. Let’s do that."
    "I took my lemonade and went to a table nearby to wait, until it was time for dinner."
    


# Outside in Paris
    scene bg rue
    with fade
        
    "The whole time we walked outside, Amélie was clinging to my arm."
    "She was so close that, in spite of all the traffic noise, in spite of how low she murmured, I still heard her:"

    show depressedsub tears at right
    sub "…I think I should quit this job."

    nvl show dissolve

    nvl_narrator """
      In the end, I managed to convince Amélie to go to the doctor,{w} so she would get prescribed time for sick leave.
      
      It took some coaxing, and the patient voice I normally used during aftercare:{w} maternal, slow, tender, reassuring. {w} “You are okay now, and everything will be fine. I love you.”
      
      The idea that she might have cut her ties with her friends and lost her source of income terrified me{w} to the point that I accompanied her back to the bar and stayed there the whole time, right up until 2 am. 
    """
    nvl clear

    nvl_narrator "Amélie walked very slowly on the road back to the bar,{w} but, apart from that, the night ended without any further incident."
    nvl_narrator "I was so exhausted by the time we got home that I slept through my alarm in the morning and was late for work."

    nvl clear
