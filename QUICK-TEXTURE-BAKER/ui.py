import bpy
from .ops_create_texture import QTB_OT_CreateTextureNode
from .ops_bake_texture import QTB_OT_BakeTexture


class QTB_PT_MainPanel(bpy.types.Panel):
    bl_label = "Quick Texture Baker"
    bl_idname = "QTB_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Quick Texture Baker"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.label(text="Create New Texture Image")
        row = layout.row()
        row.prop(scene, "qtb_texture_name", text="Texture Name")

        op = layout.operator(
            QTB_OT_CreateTextureNode.bl_idname,
            text="Create Texture Node",
            icon='TEXTURE_DATA'
        )
        if op:
            op.image_name = scene.qtb_texture_name

        layout.separator()
        
        bake_op = layout.operator(
            QTB_OT_BakeTexture.bl_idname,
            text="Bake to Texture (Diffuse)",
            icon='RENDER_STILL'
        )
        if bake_op:
            bake_op.image_name = scene.qtb_texture_name


def register():
    bpy.utils.register_class(QTB_PT_MainPanel)
    bpy.types.Scene.qtb_texture_name = bpy.props.StringProperty(
        name="Texture Name",
        description="Name for the new texture image",
        default="Body"
    )


def unregister():
    del bpy.types.Scene.qtb_texture_name
    bpy.utils.unregister_class(QTB_PT_MainPanel)
