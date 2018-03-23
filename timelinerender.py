# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/1d_timeline_render
#
# Version history:
#   1.0. - Dev start


import os
import bpy


class TimeLineRender:

    @staticmethod
    def checktextblock(context):
        textblock = None
        if TimeLineRenderOptions.textblockname in bpy.data.texts:
            textblock = bpy.data.texts[TimeLineRenderOptions.textblockname]
        else:
            textblock = bpy.data.texts.new(name=TimeLineRenderOptions.textblockname)
            textblock.from_string(TimeLineRenderOptions.emptyshablon)
            textblock.name = TimeLineRenderOptions.textblockname
        if textblock:
            areatoshow = None
            for area in context.screen.areas:
                if area.type == 'TEXT_EDITOR':
                    areatoshow = area
            if not areatoshow:
                for area in context.screen.areas:
                    if area.type not in ['PROPERTIES', 'INFO', 'OUTLINER']:
                        areatoshow = area
                        break
            if areatoshow:
                areatoshow.type = 'TEXT_EDITOR'
                areatoshow.spaces.active.text = textblock
                textblock.current_line_index = 0


class TimeLineRenderOptions:

    textblockname = 'TimeLineRender.txt'
    emptyshablon = '1,2,7-9,4\n# В первой строке указываются номера и диапазоны кадров для рендера'
