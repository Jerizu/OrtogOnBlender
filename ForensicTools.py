import bpy
import re
import platform
import subprocess

from datetime import datetime

from .PontosAnatomicos import *
from .FerrImgTomo import *

def AdicionaMarcadorDef(nome, distancia):

    bpy.ops.object.empty_add(type='SINGLE_ARROW', view_align=False)
    bpy.context.object.empty_display_size = distancia

    bpy.context.object.name = nome


    context = bpy.context
    obj = context.object
    scn = context.scene

    Marcador_EMP = obj
#    Marcador_EMP.select_set(True)
#    bpy.context.view_layer.objects.active = Marcador_EMP

    Marcador_EMP.location = bpy.context.scene.cursor.location
    Marcador_EMP.rotation_euler = bpy.context.scene.cursor.rotation_euler

#    bpy.context.scene.tool_settings.snap_elements = {'FACE'}
#    bpy.context.scene.tool_settings.use_snap_align_rotation = True

#    bpy.ops.wm.tool_set_by_id(name="builtin.rotate")

#    bpy.context.scene.transform_orientation_slots[0].type = 'NORMAL'

#    bpy.ops.view3d.view_selected(use_all_regions=False)

#    bpy.ops.view3d.view_center_cursor()

class AdicionaMarcador(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.adiciona_marcador"
    bl_label = "Add Soft Tissue Marker"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        NomePonto = bpy.context.scene.nome_marcador
        DistPonto = float(bpy.context.scene.dimensao_marcador)
        AdicionaMarcadorDef(NomePonto, DistPonto)
        return {'FINISHED'}

bpy.utils.register_class(AdicionaMarcador)


#-----------------------------------
# Cria Botões Marcadores Tecido mole

'''
with open('/home/linux3dcs/prj/Arc-Team_Santo/planilha.csv', 'r') as f:
    fileLines = f.readlines()

for i in range(len(fileLines)):
    limpaFinalLinha = fileLines[i].strip()
    separa = limpaFinalLinha.split(',')
    print(separa)
'''


def CriaBotoesDef():

    context = bpy.context
    #obj = context.object
    scn = context.scene

    bpy.context.scene.tool_settings.transform_pivot_point = 'MEDIAN_POINT' # Tem que estar assim senão o alinhamento dá errado!


#        with open('/home/linux3dcs/prj/Arc-Team_Santo/planilha.csv', 'r') as f:
    with open(scn.my_tool.filepathcsv, 'r') as f:
        fileLines = f.readlines()

    posicaoZ = 0

    for i in range(len(fileLines))[::-1]:
        limpaFinalLinha = fileLines[i].strip()
        separa = limpaFinalLinha.split(',')
        #print(separa)

        # Cria def do botão
        Nome = "Mk "+separa[0]
        NomeClass = Nome.replace(" ", "")
        NomeMin = "object."+Nome.lower().replace(" ", "_")

        bpy.ops.object.empty_add(type='SINGLE_ARROW', view_align=False, location=(-150, 0, posicaoZ))
        bpy.context.object.name = Nome
        bpy.context.object.empty_display_size = float(separa[1])
        bpy.context.object.show_name = True
        bpy.ops.transform.rotate(value=1.5708, orient_axis='Y')
        posicaoZ += 10

    # ENVIA COLLECTION

        obj2 = bpy.context.view_layer.objects.active

        ListaColl = []

        for i in bpy.data.collections:
            ListaColl.append(i.name)

        if "Soft Tissue Markers" not in ListaColl:

            myCol = bpy.data.collections.new("Soft Tissue Markers")
            bpy.context.scene.collection.children.link(myCol)
            bpy.ops.object.collection_link(collection='Soft Tissue Markers')
    #        mainCol = bpy.data.collections['Collection']
    #        bpy.context.scene.collection.children.unlink(mainCol)
            bpy.data.collections['Collection'].objects.unlink(obj2)

        else:
            bpy.ops.object.collection_link(collection='Soft Tissue Markers')
    #        mainCol = bpy.data.collections['Collection']
    #        bpy.context.scene.collection.children.unlink(mainCol)
            bpy.data.collections['Collection'].objects.unlink(obj2)

    bpy.context.scene.tool_settings.snap_elements = {'FACE'}
    bpy.context.scene.tool_settings.use_snap_align_rotation = True




class CriaBotoes(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_cria_botoes"
    bl_label = "Cria Botões"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        CriaBotoesDef()
        return {'FINISHED'}

bpy.utils.register_class(CriaBotoes)

def OcultaNomesDef():
    context = bpy.context
    #obj = context.object
    scn = context.scene

    for i in bpy.context.selected_objects:
        i.show_name = False

class OcultaNomes(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.oculta_nomes"
    bl_label = "Hide Names"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        OcultaNomesDef()
        return {'FINISHED'}

bpy.utils.register_class(OcultaNomes)

def EngrossaLinhaDef():
    context = bpy.context
    #obj = context.object
    scn = context.scene

    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.convert(target='CURVE')
    bpy.context.object.data.bevel_depth = 0.84

class EngrossaLinha(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.engrossa_linha"
    bl_label = "Make Tube Line"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        EngrossaLinhaDef()
        return {'FINISHED'}

bpy.utils.register_class( EngrossaLinha)


def ForensicImportaMuscleDef(nome, colecao):

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    try:
        bpy.ops.object.mode_set(mode='OBJECT')
    except:
        print("Erro com o Object Mode!")


    if platform.system() == "Linux":

        dirScript = bpy.utils.user_resource('SCRIPTS')

        blendfile = dirScript+"addons/OrtogOnBlender-master/ForensicObj.blend"
#        section   = "\\Collection\\"
#        object    = "SPLINT"
        section   = "\\Object\\"
        object    = nome

    if platform.system() == "Darwin":

        dirScript = bpy.utils.user_resource('SCRIPTS')

        blendfile = dirScript+"addons/OrtogOnBlender-master/ForensicObj.blend"
        section   = "\\Object\\"
        object    = nome

    if platform.system() == "Windows":

        dirScript = 'C:/OrtogOnBlender/Blender280/2.80/scripts/'

        blendfile = dirScript+"addons/OrtogOnBlender-master/ForensicObj.blend"
        section   = "\\Object\\"
        object    = nome


    filepath  = blendfile + section + object
    directory = blendfile + section
    filename  = object

    bpy.ops.wm.append(
        filepath=filepath,
        filename=filename,
        directory=directory)

    ObjImportado = bpy.data.objects[nome]


    bpy.ops.object.select_all(action='DESELECT')
    ObjImportado.select_set(True)
    context.view_layer.objects.active = ObjImportado

    # Coloca na camada
    obj2 = bpy.context.view_layer.objects.active

    ListaColl = []

    for i in bpy.data.collections:
        ListaColl.append(i.name)

    if colecao not in ListaColl:

        myCol = bpy.data.collections.new(colecao)
        bpy.context.scene.collection.children.link(myCol)
        bpy.ops.object.collection_link(collection=colecao)
#        mainCol = bpy.data.collections['Collection']
#        bpy.context.scene.collection.children.unlink(mainCol)
        bpy.data.collections['Collection'].objects.unlink(obj2)

    else:
        bpy.ops.object.collection_link(collection=colecao)
#        mainCol = bpy.data.collections['Collection']
#        bpy.context.scene.collection.children.unlink(mainCol)
        bpy.data.collections['Collection'].objects.unlink(obj2)

class ForensicImportaTemporalis(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_importa_temporalis"
    bl_label = "Import Temporalis"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Temporalis' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        ForensicImportaMuscleDef("Temporalis", "Muscle")
        return {'FINISHED'}

bpy.utils.register_class(ForensicImportaTemporalis)


class ForensicImportaMasseter(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_importa_masseter"
    bl_label = "Import Masseter"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Masseter' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        ForensicImportaMuscleDef("Masseter", "Muscle")
        return {'FINISHED'}

bpy.utils.register_class(ForensicImportaMasseter)


class ForensicImportaOrbicularisOculi(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_importa_orbicularis_oculi"
    bl_label = "Import Orbicularis Oculi"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Orbicularis Oculi' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        ForensicImportaMuscleDef("Orbicularis Oculi", "Muscle")
        return {'FINISHED'}

bpy.utils.register_class(ForensicImportaOrbicularisOculi)


class ForensicImportaElevatorLabiiSuperioris(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_importa_elevator_labii_superioris"
    bl_label = "Import Elevator Labii Superioris"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Elevator Labii Superioris' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        ForensicImportaMuscleDef("Elevator Labii Superioris", "Muscle")
        return {'FINISHED'}

bpy.utils.register_class(ForensicImportaElevatorLabiiSuperioris)


class ForensicImportaNasalis(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_importa_nasalis"
    bl_label = "Import Nasalis"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Nasalis' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        ForensicImportaMuscleDef("Nasalis", "Muscle")
        return {'FINISHED'}

bpy.utils.register_class(ForensicImportaNasalis)

class ForensicImportaZygomaticus(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_importa_zygomaticus"
    bl_label = "Import Zygomaticus"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Zygomaticus' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        ForensicImportaMuscleDef("Zygomaticus", "Muscle")
        return {'FINISHED'}

bpy.utils.register_class(ForensicImportaZygomaticus)


class ForensicImportaOrbicularisOris(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_importa_orbicularis_oris"
    bl_label = "Import Orbicularis Oris"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Orbicularis Oris' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        ForensicImportaMuscleDef("Orbicularis Oris", "Muscle")
        return {'FINISHED'}

bpy.utils.register_class(ForensicImportaOrbicularisOris)


class ForensicImportaBuccinator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_importa_buccinator"
    bl_label = "Import Buccinator"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Buccinator' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        ForensicImportaMuscleDef("Buccinator", "Muscle")
        return {'FINISHED'}

bpy.utils.register_class(ForensicImportaBuccinator)


class ForensicImportaMentalis(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_importa_mentalis"
    bl_label = "Import Mentalis"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Mentalis+' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        ForensicImportaMuscleDef("Mentalis+", "Muscle")
        return {'FINISHED'}

bpy.utils.register_class(ForensicImportaMentalis)


class ForensicImportaSternocleidomastoid(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_importa_sternocleidomastoid"
    bl_label = "Import Sternocleidomastoid"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Sternocleidomastoid+' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        ForensicImportaMuscleDef("Sternocleidomastoid+", "Muscle")
        return {'FINISHED'}

bpy.utils.register_class(ForensicImportaSternocleidomastoid)


class ForensicImportaOlho(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_importa_olho"
    bl_label = "Import Eye"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Eye' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        ForensicImportaMuscleDef("Eye", "Eyes")
        return {'FINISHED'}


bpy.utils.register_class(ForensicImportaOlho)

def CopiaEspelhaDef():

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)

    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.context.scene.tool_settings.transform_pivot_point = 'MEDIAN_POINT'
    bpy.ops.object.duplicate_move()
    bpy.ops.transform.mirror(orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

class CopiaEspelha(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_copia_espelha"
    bl_label = "Copy and Mirror"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        CopiaEspelhaDef()
        return {'FINISHED'}

bpy.utils.register_class(CopiaEspelha)

def ForensicEsculturaGrabDef():

    context = bpy.context
    scn = context.scene

#    bpy.context.space_data.shading.type = 'MATERIAL'
    bpy.ops.object.mode_set(mode = 'SCULPT')
    bpy.ops.wm.tool_set_by_id(name="builtin_brush.Grab")
    bpy.context.scene.tool_settings.sculpt.use_symmetry_x = False

class ForensicEsculturaGrab(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_escultura_grab"
    bl_label = "Change to Grab"

    @classmethod
    def poll(cls, context):
        o = context.object
        if o is None:
            return False
        else:
            if o.type == "MESH":
                if bpy.context.mode == 'OBJECT' or bpy.context.mode == 'SCULPT':
                    return True
                else:
                    return False
            else:
                return False

    def execute(self, context):
        ForensicEsculturaGrabDef()
        return {'FINISHED'}

bpy.utils.register_class(ForensicEsculturaGrab)


def ForensicEsculturaClayStripsDef():

    context = bpy.context
    scn = context.scene

#    bpy.context.space_data.shading.type = 'MATERIAL'
    bpy.ops.object.mode_set(mode = 'SCULPT')
    bpy.ops.wm.tool_set_by_id(name="builtin_brush.Clay Strips")
    bpy.context.scene.tool_settings.sculpt.use_symmetry_x = False

class ForensicEsculturaClayStrips(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_escultura_clay_strips"
    bl_label = "Change to Grab"

    @classmethod
    def poll(cls, context):
        o = context.object
        if o is None:
            return False
        else:
            if o.type == "MESH":
                if bpy.context.mode == 'OBJECT' or bpy.context.mode == 'SCULPT':
                    return True
                else:
                    return False
            else:
                return False

    def execute(self, context):
        ForensicEsculturaClayStripsDef()
        return {'FINISHED'}

bpy.utils.register_class(ForensicEsculturaClayStrips)


def ForensicEsculturaSmoothDef():

    context = bpy.context
    scn = context.scene

#    bpy.context.space_data.shading.type = 'MATERIAL'
    bpy.ops.object.mode_set(mode = 'SCULPT')
    bpy.ops.wm.tool_set_by_id(name="builtin_brush.Smooth")
    bpy.context.scene.tool_settings.sculpt.use_symmetry_x = False

class ForensicEsculturaSmooth(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_escultura_smooth"
    bl_label = "Change to Smooth"

    @classmethod
    def poll(cls, context):
        o = context.object
        if o is None:
            return False
        else:
            if o.type == "MESH":
                if bpy.context.mode == 'OBJECT' or bpy.context.mode == 'SCULPT':
                    return True
                else:
                    return False
            else:
                return False

    def execute(self, context):
        ForensicEsculturaSmoothDef()
        return {'FINISHED'}

bpy.utils.register_class(ForensicEsculturaSmooth)



def GeraBaseSculptDef():

    # Usuário seleciona tudo

    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((0, 0, 0), (0, 0, 0), (0, 0, 0)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})

    bpy.ops.object.join()

    bpy.context.object.name = "Muscles"

    # Adiciona esfera

    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0))

    bpy.ops.transform.resize(value=(180, 180, 180), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=34.004)

    # Joga na colação Face Scupting

    obj2 = bpy.context.view_layer.objects.active

    ListaColl = []

    for i in bpy.data.collections:
        ListaColl.append(i.name)

    if "Face Sculpting" not in ListaColl:

        myCol = bpy.data.collections.new("Face Sculpting")
        bpy.context.scene.collection.children.link(myCol)
        bpy.ops.object.collection_link(collection='Face Sculpting')
        ColecaoAtual = bpy.context.collection
        ColecaoAtual.objects.unlink(obj2)

    else:
        bpy.ops.object.collection_link(collection='Face Sculpting')
        ColecaoAtual = bpy.context.collection
        ColecaoAtual.objects.unlink(obj2)


    bpy.ops.object.modifier_add(type='SHRINKWRAP')
    bpy.context.object.modifiers["Shrinkwrap"].target = bpy.data.objects["Muscles"]
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Shrinkwrap")

    # Sistema de Escultura

    #bpy.ops.object.mode_set(mode='SCULPT')
    bpy.ops.object.forensic_escultura_clay_strips()
    bpy.ops.sculpt.dynamic_topology_toggle()
    bpy.context.scene.tool_settings.sculpt.detail_size = 3



class GeraBaseSculpt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_cria_face_basica"
    bl_label = "Create Basic Face Sculpting"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        GeraBaseSculptDef()
        return {'FINISHED'}

bpy.utils.register_class(GeraBaseSculpt)


class RenomeiaCranio(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.renomeia_cranio"
    bl_label = "Rename Skull"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Bones' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        bpy.context.object.name = "Bones"
        return {'FINISHED'}

bpy.utils.register_class(RenomeiaCranio)



class ForensicImportaLuzes(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_importa_luzes"
    bl_label = "Import Forensic Lights"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'ForensicLight' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        ForensicImportaMuscleDef("ForensicLight", "Lights")
        ForensicImportaMuscleDef("ForensicLight.001", "Lights")
        ForensicImportaMuscleDef("ForensicLight.002", "Lights")
        ForensicImportaMuscleDef("ForensicLight.003", "Lights")
        ForensicImportaMuscleDef("ForensicLight.004", "Lights")

        bpy.context.scene.eevee.use_gtao = True
        bpy.context.scene.eevee.gtao_distance = 8
        bpy.context.scene.eevee.use_gtao_bent_normals = False
        # bpy.context.scene.eevee.use_bloom = True # NÃO FICA BOM!
        bpy.context.scene.eevee.use_sss = True
        bpy.context.scene.eevee.use_ssr = True
        bpy.context.scene.eevee.use_ssr_refraction = True
        bpy.context.scene.eevee.ssr_thickness = 3
        bpy.context.scene.render.hair_type = 'STRIP'
        bpy.context.scene.eevee.shadow_method = 'ESM'
        bpy.context.scene.eevee.shadow_cube_size = '512'
        bpy.context.scene.eevee.shadow_cascade_size = '512'
        bpy.context.scene.eevee.use_soft_shadows = True
        bpy.context.scene.eevee.light_threshold = 0.013
        bpy.context.scene.view_settings.exposure = 0.2

        bpy.context.space_data.shading.type = 'RENDERED'
        return {'FINISHED'}

bpy.utils.register_class(ForensicImportaLuzes)


def CriaMaterialOssosDef():

    m = Material()
#    m.set_cycles()
    # from chapter 1 of [DRM protected book, could not copy author/title]
    m.make_material("Final_Bones")

#    image_path = TmpDirPNG+"/"+Arquivo

    ImageTexture = m.makeNode('ShaderNodeTexImage', 'Image Texture')
    ImageTexture.image = bpy.data.images["scene_dense_mesh_texture_material_0_map_Kd.jpg"]


    diffuseBSDF = m.nodes['Principled BSDF']
    diffuseBSDF.inputs["Base Color"].default_value = [0.2, 0.2, 0.2, 1]
    materialOutput = m.nodes['Material Output']

    mixShader = m.makeNode('ShaderNodeMixShader', 'Mix Shader')
    m.dump_node(mixShader)
    mixShader.inputs['Fac'].default_value = 0.3

    mixShader2 = m.makeNode('ShaderNodeMixShader', 'Mix Shader 2')
    mixShader2.inputs['Fac'].default_value = 0.015

    sssShader = m.makeNode('ShaderNodeSubsurfaceScattering', 'Subsurface Scattering')
    sssShader.inputs[1].default_value = 20

    glossyShader = m.makeNode('ShaderNodeBsdfGlossy', 'Glossy BSDF')
    glossyShader.inputs[1].default_value = .15

    m.link(diffuseBSDF, 'BSDF', mixShader, 2)
    m.link(sssShader, 'BSSRDF', mixShader, 1)
    m.link(glossyShader, 'BSDF', mixShader2, 2)
    m.link(mixShader, 'Shader', mixShader2, 1)
    m.link(mixShader2, 'Shader', materialOutput, 'Surface')
    m.link(ImageTexture, 'Color', diffuseBSDF, 'Base Color')
    m.link(ImageTexture, 'Color', sssShader, 'Color')

    bpy.ops.object.material_slot_remove()
    bpy.ops.object.material_slot_add()

    bpy.data.objects["Bones"].active_material = bpy.data.materials["Final_Bones"]

#    bpy.data.objects[bpy.context.view_layer.objects.active.name].active_material = bpy.data.materials["Final_Bones"]


class CriaMaterialOssos(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.ajusta_material_cranio"
    bl_label = "Skull Material Adjustament"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = bpy.data.objects["Bones"].active_material.name

        if found == "Final_Bones":
            return False
        else:
            if found != "Final_Bones":
                return True

    def execute(self, context):
        CriaMaterialOssosDef()
        return {'FINISHED'}

bpy.utils.register_class(CriaMaterialOssos)


def ForensicGeraImagemDef():


    context = bpy.context
    scn = context.scene

    homeDir = expanduser("~")

    NomeArquivoImagem = "IMG_"+str(datetime.now()).replace(",","").replace(":","").replace(".","-").replace(" ","-")+".png"

    NomePaciente = bpy.context.scene.nome_paciente
    SobrenomePaciente = bpy.context.scene.sobrenome_paciente

    NomePacienteDir = homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Render"

#        if found == False:
    if not os.path.exists(NomePacienteDir):
        print("Patience Dir does not exist!")
        try:
            os.mkdir(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Render")
            bpy.ops.render.opengl()

            bpy.data.images['Render Result'].save_render(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Render/"+NomeArquivoImagem)

            CaminhoCompletoImagem = homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Render/"+NomeArquivoImagem

            if platform.system() == 'Darwin':
                subprocess.call(('open', CaminhoCompletoImagem))
            elif platform.system() == 'Windows':
                os.startfile(CaminhoCompletoImagem)
            else:
                subprocess.call(('xdg-open', CaminhoCompletoImagem))

        except:
            print("Não rolou a renderização!")
    else:
        if os.path.exists(NomePacienteDir):
            #shutil.copytree(Origem, NomePacienteDir+"/Render")

            bpy.ops.render.opengl()

            bpy.data.images['Render Result'].save_render(homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Render/"+NomeArquivoImagem)

            CaminhoCompletoImagem = homeDir+"/OrtogOnBlenderDir/"+NomePaciente+"_"+SobrenomePaciente+"/Render/"+NomeArquivoImagem

            if platform.system() == 'Darwin':
                subprocess.call(('open', CaminhoCompletoImagem))
            elif platform.system() == 'Windows':
                os.startfile(CaminhoCompletoImagem)
            else:
                subprocess.call(('xdg-open', CaminhoCompletoImagem))

class ForensicGeraImagem(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.forensic_gera_imagem"
    bl_label = "Forensic Render Image"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        ForensicGeraImagemDef()
        return {'FINISHED'}

bpy.utils.register_class(ForensicGeraImagem)
