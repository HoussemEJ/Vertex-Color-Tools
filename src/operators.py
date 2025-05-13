import bpy
import random

class VCT_OT_assign_vertex_color(bpy.types.Operator):
    """Assign random vertex colors to multiple selected objects, if specific faces are selected color will be only assigned for those faces."""
    bl_idname = "vct.assign_vertex_color"
    bl_label = "Assign Vertex Color"
    bl_options = {'REGISTER', 'UNDO'}

    def generate_random_color(self):
        return (random.random(), random.random(), random.random())
    
    def execute(self, context):
        selected_objects = [obj for obj in context.selected_objects if obj.type == 'MESH']

        if not selected_objects:
            self.report({'WARNING'}, "No mesh objects selected.")
            return {'CANCELLED'}
            
        for obj in selected_objects:
            context.view_layer.objects.active = obj
            bpy.ops.object.mode_set(mode='VERTEX_PAINT')
            obj.data.use_paint_mask = True

            if context.scene.randomize_color:
                color = self.generate_random_color()
            else:
                color_picker = context.scene.vertex_color_picker
                color = (color_picker[0], color_picker[1], color_picker[2])

            bpy.context.tool_settings.vertex_paint.brush.color = color
            bpy.ops.paint.vertex_color_set()

        bpy.ops.object.mode_set(mode='OBJECT')

        return {'FINISHED'}

classes = (
    VCT_OT_assign_vertex_color,
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister():
    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)