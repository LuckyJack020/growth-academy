init python:
    hoverExtra = ""

screen extras():
    tag menu
    add "Graphics/ui/bg/archiveBG/infodesk_eve.webp"
    grid 3 3:
        xfill True
        yfill True
        null
        null
        null
        imagebutton idle "Graphics/ui/icons/ArtGalleryIcon.webp" action ShowMenu("galleryselect") xalign 0.5 yalign 0.5 hovered SetVariable("hoverExtra", "Scene Gallery") unhovered SetVariable("hoverExtra", "")
        null
        imagebutton idle "Graphics/ui/icons/MusicRoomIcon.webp" hover "Graphics/ui/icons/MusicRoomIconHover.webp" action [ShowMenu("music_room"), Function(ost.get_music_channel_info), Stop('music', fadeout=2.0), Function(ost.refresh_list)] xalign 0.5 yalign 0.5 hovered SetVariable("hoverExtra", "Music Player") unhovered SetVariable("hoverExtra", "")
        null
        textbutton "Return" action Return() xalign 0.5 yalign 0.5 text_outlines [ (2, "#000000", 0, 0) ] text_size 30 text_color "#FFFFFF" text_hover_color "#b1b1b1"
        null
    if hoverExtra != "":
        frame:
            xalign 0.9
            yalign 0.9
            xanchor 1.0
            background Solid(Color((0, 0, 0, 100)))
            text(hoverExtra)
