import bpy

class VCT_PT_main_panel(bpy.types.Panel):
    """Vertex Color Tools"""
    bl_label = "Vertex Color Tools"
    bl_idname = "VCT_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "5Th-Dimension"

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene, "vertex_color_picker", text="Color")
        layout.prop(context.scene, "randomize_color", text="Randomize")
        layout.operator("vct.assign_vertex_color", text="Assign Color")

classes = (
    VCT_PT_main_panel,
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister():
    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)