screen extras():
    tag menu
    add "Graphics/ui/bg/infodesk_eve.png"
    grid 3 3:
        xfill True
        yfill True
        null
        null
        null
        textbutton "Image Gallery" action ShowMenu("galleryselect") xalign 0.5 yalign 0.5
        null
        textbutton "Music Room" action [ShowMenu("music_room"), Stop('music', fadeout=2.0), If(preferences.get_volume("music") == 0.0, true=SetVariable("ost.music_muted", True), false=SetMute('music', True)), Function(ost.refresh_list)] xalign 0.5 yalign 0.5
        null
        textbutton "Return" action Return() xalign 0.5 yalign 0.5
        null
