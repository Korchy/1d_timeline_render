# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/1d_timeline_render
#
# Version history:
#   1.0. - Dev start


import bpy
from .timelinerender import TimeLineRender
import os

class TimeLineRenderStart(bpy.types.Operator):
    bl_idname = 'timelinerender.start'
    bl_label = 'Start TimeLineRender'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}


def register():
    bpy.utils.register_class(TimeLineRenderStart)


def unregister():
    bpy.utils.unregister_class(TimeLineRenderStart)
