import bpy

class QTB_OT_BakeTexture(bpy.types.Operator):
    """Bake the active object’s material to the selected texture"""
    bl_idname = "qtb.bake_texture"
    bl_label = "Bake Texture"
    bl_options = {'REGISTER', 'UNDO'}

    image_name: bpy.props.StringProperty()

    def execute(self, context):
        obj = context.active_object
        
        if not obj or not obj.active_material:
            self.report({'WARNING'}, "No active object or material found.")
            return {'CANCELLED'}
            
        if obj.type != 'MESH':
            self.report({'ERROR'}, f"Active object '{obj.name}' is not a mesh. Baking requires the active object to be a selected mesh object.")
            return {'CANCELLED'}

        mat = obj.active_material
        nodes = mat.node_tree.nodes

        tex_node = next((n for n in nodes if n.type == 'TEX_IMAGE' and n.image and n.image.name == self.image_name), None)
        if not tex_node:
            self.report({'WARNING'}, f"No image texture node found with the name '{self.image_name}'. Did you create it first?")
            return {'CANCELLED'}

        if bpy.context.scene.render.engine != 'CYCLES':
            bpy.context.scene.render.engine = 'CYCLES'

        nodes.active = tex_node
        tex_node.select = True
        
        for node in nodes:
            if node != tex_node:
                node.select = False

        bpy.context.scene.cycles.bake_type = 'DIFFUSE'
        bpy.context.scene.render.bake.use_pass_direct = False
        bpy.context.scene.render.bake.use_pass_indirect = False
        bpy.context.scene.render.bake.use_selected_to_active = False 

        try:
            bpy.ops.object.bake(type='DIFFUSE')
        except RuntimeError as e:
            self.report({'ERROR'}, f"Baking failed: {e}. Ensure a Mesh object is actively selected and has a material.")
            return {'CANCELLED'}


        self.report({'INFO'}, f"Baked Diffuse to image '{self.image_name}'.")
        return {'FINISHED'}


def register():
    bpy.utils.register_class(QTB_OT_BakeTexture)


def unregister():
    bpy.utils.unregister_class(QTB_OT_BakeTexture)
v