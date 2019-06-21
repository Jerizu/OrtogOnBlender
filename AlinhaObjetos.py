import bpy
import math

# MENSAGENS

class MessageSelecioneObjAlinhar(bpy.types.Operator):
    bl_idname = "object.dialog_operator_selecione_alinhar"
    bl_label = "Please, select the object to be aligned!"
  
    def execute(self, context):
        message = ("Please, select an object before!")
        self.report({'INFO'}, message)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

bpy.utils.register_class(MessageSelecioneObjAlinhar)

# Origin

def EMP1aDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP1a"
    #bpy.context.object.empty_draw_size = 3
    bpy.context.object.empty_display_size = 3


class EMP1a(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp1a"
    bl_label = "EMP1a"

    @classmethod
    def poll(cls, context):

        found = 'EMP1a' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    
    def execute(self, context):
        context = bpy.context
        obj = context.object

        if bpy.context.selected_objects == []:
            bpy.ops.object.dialog_operator_selecione_alinhar('INVOKE_DEFAULT')
            return {'FINISHED'}
        else:
            EMP1aDef(self, context)
            bpy.ops.object.select_all(action='DESELECT')
            obj.select_set(True)
            context.view_layer.objects.active = obj
        return {'FINISHED'}

def EMP2aDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP2a"
    #bpy.context.object.empty_draw_size = 3
    bpy.context.object.empty_display_size = 3


class EMP2a(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp2a"
    bl_label = "EMP2a"

    @classmethod
    def poll(cls, context):

        found = 'EMP2a' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    
    def execute(self, context):
        context = bpy.context
        obj = context.object

        if bpy.context.selected_objects == []:
            bpy.ops.object.dialog_operator_selecione_alinhar('INVOKE_DEFAULT')
            return {'FINISHED'}
        else:
            EMP2aDef(self, context)
            bpy.ops.object.select_all(action='DESELECT')
            obj.select_set(True)
            context.view_layer.objects.active = obj
        return {'FINISHED'}

def EMP3aDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP3a"
    #bpy.context.object.empty_draw_size = 3
    bpy.context.object.empty_display_size = 3


class EMP3a(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp3a"
    bl_label = "EMP3a"

    @classmethod
    def poll(cls, context):

        found = 'EMP3a' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    
    def execute(self, context):
        context = bpy.context
        obj = context.object

        if bpy.context.selected_objects == []:
            bpy.ops.object.dialog_operator_selecione_alinhar('INVOKE_DEFAULT')
            return {'FINISHED'}
        else:
            EMP3aDef(self, context)
            bpy.ops.object.select_all(action='DESELECT')
            obj.select_set(True)
            context.view_layer.objects.active = obj
        return {'FINISHED'}

 # Align

def EMP1bDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP1b"
    #bpy.context.object.empty_draw_size = 3
    bpy.context.object.empty_display_size = 3


class EMP1b(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp1b"
    bl_label = "EMP1b"

    @classmethod
    def poll(cls, context):

        found = 'EMP1b' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    
    def execute(self, context):
        context = bpy.context
        obj = context.object

        if bpy.context.selected_objects == []:
            bpy.ops.object.dialog_operator_selecione_alinhar('INVOKE_DEFAULT')
            return {'FINISHED'}
        else:
            EMP1bDef(self, context)
            bpy.ops.object.select_all(action='DESELECT')
            obj.select_set(True)
            context.view_layer.objects.active = obj
        return {'FINISHED'}

def EMP2bDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP2b"
    #bpy.context.object.empty_draw_size = 3
    bpy.context.object.empty_display_size = 3


class EMP2b(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp2b"
    bl_label = "EMP2b"

    @classmethod
    def poll(cls, context):

        found = 'EMP2b' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    
    def execute(self, context):
        context = bpy.context
        obj = context.object

        if bpy.context.selected_objects == []:
            bpy.ops.object.dialog_operator_selecione_alinhar('INVOKE_DEFAULT')
            return {'FINISHED'}
        else:
            EMP2bDef(self, context)
            bpy.ops.object.select_all(action='DESELECT')
            obj.select_set(True)
            context.view_layer.objects.active = obj
        return {'FINISHED'}


def EMP3bDef(self, context):
    
    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.empty_add(type='PLAIN_AXES')
    bpy.context.object.name = "EMP3b"
    #bpy.context.object.empty_draw_size = 3
    bpy.context.object.empty_display_size = 3


class EMP3b(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.emp3b"
    bl_label = "EMP3b"

    @classmethod
    def poll(cls, context):

        found = 'EMP3b' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    
    def execute(self, context):
        context = bpy.context
        obj = context.object

        if bpy.context.selected_objects == []:
            bpy.ops.object.dialog_operator_selecione_alinhar('INVOKE_DEFAULT')
            return {'FINISHED'}
        else:
            EMP3bDef(self, context)
            bpy.ops.object.select_all(action='DESELECT')
            obj.select_set(True)
            context.view_layer.objects.active = obj
        return {'FINISHED'}

def AlinhaTresPontosDef(self, context):

    context = bpy.context
    objAlinhar = context.active_object

    if bpy.context.selected_objects == []:
        bpy.ops.object.dialog_operator_selecione_alinhar('INVOKE_DEFAULT')
        return {'FINISHED'}

    else:
        # Adiciona plano Origem
        bpy.ops.mesh.add_mesh_alinha_origi()
        bpy.context.object.name = "MeshAlignOrigi" # Força nome para não dar erro

        # Seleciona pontos
        bpy.ops.object.mode_set(mode = 'OBJECT')
        obj = bpy.context.active_object
        bpy.ops.object.mode_set(mode = 'EDIT') 
        bpy.ops.mesh.select_mode(type="VERT")
        bpy.ops.mesh.select_all(action = 'DESELECT')
        bpy.ops.object.mode_set(mode = 'OBJECT')
        obj.data.vertices[0].select = True
        obj.data.vertices[1].select = True
        obj.data.vertices[2].select = True
        bpy.ops.object.mode_set(mode = 'EDIT')

        # Seleciona os pontos de rotação
        bpy.ops.maplus.quickalignplanesgrabdest()

        # Sai do modo de edição
        bpy.ops.object.mode_set(mode='OBJECT')

        # Adiciona plano a Alinhar
        bpy.ops.mesh.add_mesh_alinha_alinha()
        bpy.context.object.name = "MeshAlignAlign" # Força nome para não dar erro

        objMalhaAlinha = context.active_object

        # Seleciona os pontos
        bpy.ops.object.mode_set(mode = 'OBJECT')
        obj = bpy.context.active_object
        bpy.ops.object.mode_set(mode = 'EDIT') 
        bpy.ops.mesh.select_mode(type="VERT")
        bpy.ops.mesh.select_all(action = 'DESELECT')
        bpy.ops.object.mode_set(mode = 'OBJECT')
        obj.data.vertices[0].select = True
        obj.data.vertices[1].select = True
        obj.data.vertices[2].select = True
        bpy.ops.object.mode_set(mode = 'EDIT')

        bpy.ops.object.mode_set(mode='OBJECT')

        # Sai do modo de edição
        bpy.ops.object.select_all(action='DESELECT')
        objAlinhar.select_set(True)
        objMalhaAlinha.select_set(True)
        bpy.context.view_layer.objects.active = objMalhaAlinha

        # Agrupa malha e objeto

        bpy.ops.object.parent_set()

        bpy.ops.object.select_all(action='DESELECT')
        objMalhaAlinha.select_set(True)
        bpy.context.view_layer.objects.active = objMalhaAlinha

        # Alinha planos
        bpy.ops.maplus.quickalignplanesobject()

        # Desparenteia rotacionado
        bpy.ops.object.select_all(action='DESELECT')
        objAlinhar.select_set(True)
        bpy.context.view_layer.objects.active = objAlinhar

        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')


        # Apaga objetos
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects['EMP1a'].select_set(True)
        bpy.data.objects['EMP2a'].select_set(True)
        bpy.data.objects['EMP3a'].select_set(True)
        bpy.data.objects['EMP1b'].select_set(True)
        bpy.data.objects['EMP2b'].select_set(True)
        bpy.data.objects['EMP3b'].select_set(True)
        bpy.data.objects['MeshAlignOrigi'].select_set(True)
        bpy.data.objects['MeshAlignAlign'].select_set(True)
        bpy.context.view_layer.objects.active = objMalhaAlinha

        bpy.ops.object.delete(use_global=False)

        # Seleciona objeto alinhado
        bpy.ops.object.select_all(action='DESELECT')
        objAlinhar.select_set(True)
        bpy.context.view_layer.objects.active = objAlinhar

    '''
	context = bpy.context
	ObjAlinha = context.object

	EMP1a = bpy.data.objects['EMP1a']
	EMP2a = bpy.data.objects['EMP2a']
	EMP3a = bpy.data.objects['EMP3a']

	# EMP4a
	bpy.ops.object.empty_add(type='SPHERE', location=((EMP2a.location[0]+EMP3a.location[0])/2, (EMP2a.location[1]+EMP3a.location[1])/2, (EMP2a.location[2]+EMP3a.location[2])/2))

	bpy.context.object.name = "EMP4a"
	EMP4a = bpy.data.objects['EMP4a']

	EMP1b = bpy.data.objects['EMP1b']
	EMP2b = bpy.data.objects['EMP2b']
	EMP3b = bpy.data.objects['EMP3b']

	bpy.ops.object.empty_add(type='SPHERE', location=((EMP2b.location[0]+EMP3b.location[0])/2, (EMP2b.location[1]+EMP3b.location[1])/2, (EMP2b.location[2]+EMP3b.location[2])/2))

	bpy.context.object.name = "EMP4b"
	EMP4b = bpy.data.objects['EMP4b']

	# Alinha no molde

	EMP1b.select_set(True)
	EMP2b.select_set(True)
	EMP3b.select_set(True)
	ObjAlinha.select_set(True)

	bpy.ops.object.parent_set()

	# Alinha com o EMP4b ao EMP4a

	bpy.ops.object.select_all(action='DESELECT')

	EMP4b.select_set(True)
	context.view_layer.objects.active = EMP4b

	bpy.context.object.location = EMP4a.location

	bpy.ops.object.select_all(action='DESELECT')
	EMP1b.select_set(True)
	EMP2b.select_set(True)
	EMP3b.select_set(True)
	ObjAlinha.select_set(True)
	bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')

	# Calcula grau

	A = math.sqrt((EMP2b.location[0] - EMP4a.location[0])**2 + (EMP2b.location[2] - EMP4a.location[2])**2)

	B = math.sqrt((EMP2b.location[0] - EMP2a.location[0])**2 + (EMP2b.location[2] - EMP2a.location[2])**2)

	C = math.sqrt((EMP2a.location[0] - EMP4a.location[0])**2 + (EMP2a.location[2] - EMP4a.location[2])**2)

	AngEMP4ab = (C**2 + A**2 - B**2) / (2 * C * A) # Parênteses importantes!!!

	# Radianos
	RotacaoY = math.acos(AngEMP4ab)

	# Ângulo
	math.acos(AngEMP4ab)* 180/math.pi

	bpy.ops.object.select_all(action='DESELECT')
	EMP1b.select_set(True)
	EMP2b.select_set(True)
	EMP3b.select_set(True)
	ObjAlinha.select_set(True)
	EMP4b.select_set(True)
	context.view_layer.objects.active = EMP4b
	bpy.ops.object.parent_set()

	bpy.ops.object.select_all(action='DESELECT')
	EMP4b.select_set(True)
	context.view_layer.objects.active = EMP4b

	# Rotação Y

	if EMP2a.location[2] < EMP2b.location[2]:
	    bpy.ops.transform.rotate(value=RotacaoY, orient_axis='Y', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
	    
	if EMP2a.location[2] > EMP2b.location[2]:
	    bpy.ops.transform.rotate(value=-abs(RotacaoY), orient_axis='Y', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
	    
	# Desagrupa para cálculo

	bpy.ops.object.select_all(action='DESELECT')
	EMP1b.select_set(True)
	EMP2b.select_set(True)
	EMP3b.select_set(True)
	ObjAlinha.select_set(True)
	bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')

	A = math.sqrt((EMP1b.location[1] - EMP4a.location[1])**2 + (EMP1b.location[2] - EMP4a.location[2])**2)

	B = math.sqrt((EMP1b.location[1] - EMP1a.location[1])**2 + (EMP1b.location[2] - EMP1a.location[2])**2)

	C = math.sqrt((EMP1a.location[1] - EMP4a.location[1])**2 + (EMP1a.location[2] - EMP4a.location[2])**2)

	AngEMP4ab = (C**2 + A**2 - B**2) / (2 * C * A)

	# Radianos
	RotacaoX = math.acos(AngEMP4ab)

	# Ângulo
	math.acos(AngEMP4ab)* 180/math.pi

	bpy.ops.object.select_all(action='DESELECT')
	EMP1b.select_set(True)
	EMP2b.select_set(True)
	EMP3b.select_set(True)
	ObjAlinha.select_set(True)
	EMP4b.select_set(True)
	context.view_layer.objects.active = EMP4b
	bpy.ops.object.parent_set()

	bpy.ops.object.select_all(action='DESELECT')
	EMP4b.select_set(True)
	context.view_layer.objects.active = EMP4b

	if EMP1a.location[2] < EMP1b.location[2]:
	    bpy.ops.transform.rotate(value=RotacaoX, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
	if EMP1a.location[2] > EMP1b.location[2]:
	    bpy.ops.transform.rotate(value=-abs(RotacaoX), orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
	    
	# Desagrupa para cálculo

	bpy.ops.object.select_all(action='DESELECT')
	EMP1b.select_set(True)
	EMP2b.select_set(True)
	EMP3b.select_set(True)
	ObjAlinha.select_set(True)
	bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')

	A = math.sqrt((EMP1b.location[0] - EMP4a.location[0])**2 + (EMP1b.location[1] - EMP4a.location[1])**2)

	B = math.sqrt((EMP1b.location[0] - EMP1a.location[0])**2 + (EMP1b.location[1] - EMP1a.location[1])**2)

	C = math.sqrt((EMP1a.location[0] - EMP4a.location[0])**2 + (EMP1a.location[1] - EMP4a.location[1])**2)

	AngEMP4ab = (C**2 + A**2 - B**2) / (2 * C * A)
	print("Angulo grosso", AngEMP4ab)

	# Radianos
	RotacaoZ = math.acos(AngEMP4ab)

	# Ângulo
	AnguloZ = math.acos(AngEMP4ab)* 180/math.pi

	bpy.ops.object.select_all(action='DESELECT')
	EMP1b.select_set(True)
	EMP2b.select_set(True)
	EMP3b.select_set(True)
	ObjAlinha.select_set(True)
	EMP4b.select_set(True)
	context.view_layer.objects.active = EMP4b
	bpy.ops.object.parent_set()

	bpy.ops.object.select_all(action='DESELECT')
	EMP4b.select_set(True)
	context.view_layer.objects.active = EMP4b

	if EMP1a.location[0] > EMP1b.location[0]:
	    bpy.ops.transform.rotate(value=RotacaoZ, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
	if EMP1a.location[0] < EMP1b.location[0]:
	    bpy.ops.transform.rotate(value=-abs(RotacaoZ), orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

	# Apaga referências
	bpy.ops.object.select_all(action='DESELECT')
	EMP1a.select_set(True)
	EMP2a.select_set(True)
	EMP3a.select_set(True)
	EMP4a.select_set(True)  
	EMP1b.select_set(True)
	EMP2b.select_set(True)
	EMP3b.select_set(True)
	EMP4b.select_set(True)    
	bpy.ops.object.delete()
    '''

class AlinhaTresPontos(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.alinha_tres_pontos"
    bl_label = "Align 3 Points"
    
    def execute(self, context):
        AlinhaTresPontosDef(self, context)
        return {'FINISHED'}