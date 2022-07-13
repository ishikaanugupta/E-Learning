from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponse
import os
from .models import myuploadfile
from pathlib import Path
from django.conf import settings
from django.contrib.auth.models import User

#!/usr/bin/env python
import vtk
# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    VTK_VERSION_NUMBER,
    vtkLookupTable,
    vtkVersion
)
from vtkmodules.vtkFiltersCore import (
    vtkFlyingEdges3D,
    vtkMarchingCubes,
    vtkStripper
)
from vtkmodules.vtkFiltersModeling import vtkOutlineFilter
from vtkmodules.vtkIOImage import vtkMetaImageReader
from vtkmodules.vtkImagingCore import vtkImageMapToColors
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkCamera,
    vtkImageActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

# Create your views here.

def index(request):
    
    return render(request,'casestudys/casestudy.html')

def send_files(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        f_name = request.POST.get("filename")
        myfile = request.FILES.getlist("file_field")


        name_path = "dicom/guest/"

        path = os.path.join(settings.MEDIA_ROOT,name_path)


        for f in os.listdir(path):
            os.remove(os.path.join(path, f))
        
        for f in myfile:
            
            myuploadfile(myfiles=f,user_id=user_id).save()


        colors = vtkNamedColors()

        colors.SetColor('SkinColor', [240, 184, 160, 255])
        colors.SetColor('BkgColor', [51, 77, 102, 255])

        # Create the renderer, the render window, and the interactor. The
        # renderer draws into the render window, the interactor enables
        # mouse- and keyboard-based interaction with the data within the
        # render window.
        #
        a_renderer = vtkRenderer()
        ren_win = vtkRenderWindow()
        ren_win.AddRenderer(a_renderer)
        iren = vtkRenderWindowInteractor()
        iren.SetRenderWindow(ren_win)

        # Set a background color for the renderer and set the size of the
        # render window (expressed in pixels).
        a_renderer.SetBackground(colors.GetColor3d('BkgColor'))
        ren_win.SetSize(640, 480)

        # The following reader is used to read a series of 2D slices (images)
        # that compose the volume. The slice dimensions are set, and the
        # pixel spacing. The data Endianness must also be specified. The
        # reader uses the FilePrefix in combination with the slice number to
        # construct filenames using the format FilePrefix.%d. (In this case
        # the FilePrefix is the root name of the file: quarter.)
        # CT_dir = "D:\FCRIT\BE Project 2022\Datasets\Head Neck Cancer\manifest-1600133301170\QIN-HEADNECK\QIN-HEADNECK-01-0031\\03-02-1987-NA-Thorax1HEADNECKPETCT-15228\CT WB 5.0 B40sCHEST-46695"
        CT_dir = path
        reader = vtk.vtkDICOMImageReader()
        reader.SetDirectoryName(CT_dir)
        reader.Update()
        
        # An isosurface, or contour value of -300 (originally 600) is known to correspond to
        # the skin of the patient.
        # The triangle stripper is used to create triangle
        # strips from the isosurface these render much faster on may
        # systems.
        skin_extractor = vtkFlyingEdges3D()
        skin_extractor.SetInputConnection(reader.GetOutputPort())
        skin_extractor.SetValue(0, -350)

        skin_extractor.Update()

        skin_writer = vtk.vtkSTLWriter()
        skin_writer.SetInputConnection(skin_extractor.GetOutputPort())
        skin_writer.SetFileTypeToBinary()
        path_skin = os.path.join(settings.MEDIA_ROOT,name_path)
        skin_writer.SetFileName(path_skin + "skin.stl")
        skin_writer.Write()

        # An isosurface, or contour value of 100 (originally 1150) is known to correspond to
        # the bone of the patient.
        # The triangle stripper is used to create triangle
        # strips from the isosurface these render much faster on may
        # systems.
        bone_extractor = vtkFlyingEdges3D()
        bone_extractor.SetInputConnection(reader.GetOutputPort())
        bone_extractor.SetValue(0, 250)

        bone_writer = vtk.vtkSTLWriter()
        bone_writer.SetInputConnection(bone_extractor.GetOutputPort())
        bone_writer.SetFileTypeToBinary()
        path_bone = os.path.join(settings.MEDIA_ROOT,name_path)
        bone_writer.SetFileName(path_bone + "bone.stl")
        bone_writer.Write()
        print(myfile)
        #return HttpResponse("Ok")

        '''context = {
           'path_skin':path_skin,
           'path_bone' :path_bone
        }'''

        return render(request,'casestudys/casestudys_model.html' )
