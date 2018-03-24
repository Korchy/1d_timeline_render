# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/1d_timeline_render
#
# Version history:
#   1.0. - Render frames from the first line of the text block by numbers and diapasones


import bpy


class TimeLineRenderPanel(bpy.types.Panel):
    bl_idname = 'timelinerender.panel'
    bl_label = 'TimeLineRender'
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'render'

    def draw(self, context):
        self.layout.operator('timelinerender.start', icon='TIME', text='Start TimeLine Render')


def register():
    bpy.utils.register_class(TimeLineRenderPanel)


def unregister():
    bpy.utils.unregister_class(TimeLineRenderPanel)
