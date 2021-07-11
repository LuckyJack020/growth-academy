init python:
    hoverExtra = ""

screen extras():
    tag menu
    add "Graphics/ui/bg/infodesk_eve.png"
    grid 3 3:
        xfill True
        yfill True
        null
        null
        null
        imagebutton idle "Graphics/ui/icons/ArtGalleryIcon.png" action ShowMenu("galleryselect") xalign 0.5 yalign 0.5 hovered SetVariable("hoverExtra", "Scene Gallery") unhovered SetVariable("hoverExtra", "")
        null
        imagebutton idle "Graphics/ui/icons/MusicRoomIcon.png" action [ShowMenu("music_room"), Stop('music', fadeout=2.0), If(preferences.get_volume("music") == 0.0, true=SetVariable("ost.music_muted", True), false=SetMute('music', True)), Function(ost.refresh_list)] xalign 0.5 yalign 0.5 hovered SetVariable("hoverExtra", "Music Player") unhovered SetVariable("hoverExtra", "")
        null
        textbutton "Return" action Return() xalign 0.5 yalign 0.5
        null
    if hoverExtra != "":
        frame:
            xalign 0.9
            yalign 0.9
            xanchor 1.0
            background Solid(Color((0, 0, 0, 100)))
            text(hoverExtra)
