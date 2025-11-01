import bpy

def create_texture_node(context, image_name):
    obj = context.active_object
    if not obj or not obj.active_material:
        print("⚠️ Select an object with a material first.")
        return {'CANCELLED'}

    mat = obj.active_material
    mat.use_nodes = True
    nodes = mat.node_tree.nodes

    if image_name in bpy.data.images:
        print(f"⚠️ Image '{image_name}' already exists. Using existing image.")
        image = bpy.data.images[image_name]
    else:
        image = bpy.data.images.new(name=image_name, width=1024, height=1024)
    
    tex_node = nodes.new("ShaderNodeTexImage")
    tex_node.location = (0, 0)
    tex_node.image = image

    print(f"✅ Created/Set image '{image_name}' and assigned to texture node.")
    return {'FINISHED'}


class QTB_OT_CreateTextureNode(bpy.types.Operator):
    """Create a new image texture node and assign a user-defined image name"""
    bl_idname = "qtb.create_texture_node"
    bl_label = "Create Texture Node"
    bl_options = {'REGISTER', 'UNDO'}

    image_name: bpy.props.StringProperty(
        name="Texture Name",
        default="NewTexture"
    )

    def execute(self, context):
        return create_texture_node(context, self.image_name)


def register():
    bpy.utils.register_class(QTB_OT_CreateTextureNode)


def unregister():
    bpy.utils.unregister_class(QTB_OT_CreateTextureNode)
