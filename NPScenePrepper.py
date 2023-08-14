import bpy
import os
from bpy_extras.io_utils import ExportHelper

def rename_cameras():
    cam_count = 1
    for obj in bpy.data.objects:
        if obj.type == 'CAMERA':
            focal_length = obj.data.lens
            new_name = f"Cam{cam_count}_{int(focal_length)}"
            obj.name = new_name
            cam_count += 1

def rgb_to_hex(rgb):
    return '{:02X}{:02X}{:02X}'.format(int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))

def rename_lights():
    light_count = 1
    for obj in bpy.data.objects:
        if obj.type == 'LIGHT':
            color = rgb_to_hex(obj.data.color)
            radius = obj.data.shadow_soft_size
            power = obj.data.energy
            light_type = obj.data.type  # This will return 'POINT', 'SPOT', etc.
            shadows_enabled = obj.data.use_shadow
            new_name = f"Light_{color}_{radius:.1f}_{int(power)}_{light_type}_{shadows_enabled}"
            obj.name = new_name
            light_count += 1

def user_choose_filepath():
    class ExportGLBOperator(bpy.types.Operator, ExportHelper):
        bl_idname = "scene.export_glb_operator"
        bl_label = "Export GLB"
        
        filename_ext = ".glb"

        def execute(self, context):
            if self.filepath:  # Only export if a valid filepath is provided
                bpy.ops.export_scene.gltf(filepath=self.filepath, export_format='GLB')
            return {'FINISHED'}

    # Unregister the operator if it's already registered
    if hasattr(bpy.types, "ExportGLBOperator"):
        bpy.utils.unregister_class(ExportGLBOperator)
    
    # Register the operator
    bpy.utils.register_class(ExportGLBOperator)
    
    # Invoke the file dialog
    bpy.ops.scene.export_glb_operator('INVOKE_DEFAULT')

rename_cameras()
rename_lights()
user_choose_filepath()