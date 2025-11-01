bl_info = {
    "name": "Quick Texture Baker",
    "author": "Sudhanshu Ambastha",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),
    "location": "Shader Editor > Sidebar > Quick Texture Baker",
    "description": "Quickly create image texture nodes and bake textures from selected objects.",
    "category": "Material",
}

from . import ui
from . import ops_create_texture
from . import ops_bake_texture 

def register():
    ui.register()
    ops_create_texture.register()
    ops_bake_texture.register() 

def unregister():
    ui.unregister()
    ops_create_texture.unregister()
    ops_bake_texture.unregister() 

if __name__ == "__main__":
    register()
