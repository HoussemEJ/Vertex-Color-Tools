bl_info = {
    "name": "Vertex Color Tools",
    "author": "Houssemeddine Jebali",
    "version": (1, 0, 0),
    "blender": (4, 4, 0),
    "location": "3D View > N-Panel",
    "description": "Quick way to do vertex coloring for id maps",
    "category": "3D View",
}

import bpy
from . import operators
from . import interface

def register():
    operators.register()
    interface.register()
    bpy.types.Scene.vertex_color_picker = bpy.props.FloatVectorProperty(
        name="Vertex Color",
        subtype='COLOR',
        min=0.0, max=1.0,
        size=3,
        default=(1.0, 1.0, 1.0)
    )
    bpy.types.Scene.randomize_color = bpy.props.BoolProperty(
        name="Randomize",
        default=False
    )

def unregister():
    operators.unregister()
    interface.unregister()

    del bpy.types.Scene.vertex_color_picker
    del bpy.types.Scene.randomize_color

if __name__ == "__main__":
    register()