from visit import *
def savePNG(filename,geometry=[4096,4096]):
    SaveWindowAtts = SaveWindowAttributes()
    SaveWindowAtts.outputToCurrentDirectory = 1
    SaveWindowAtts.fileName = filename
    SaveWindowAtts.family = 0
    SaveWindowAtts.format = SaveWindowAtts.PNG
    SaveWindowAtts.width = geometry[0]
    SaveWindowAtts.height = geometry[1]
    SaveWindowAtts.resConstraint = SaveWindowAtts.NoConstraint
    SaveWindowAtts.forceMerge = 1
    SetSaveWindowAttributes(SaveWindowAtts)
    return SaveWindow()

def SetAnnotations():
    import visit
    AnnotationAtts = AnnotationAttributes()
    AnnotationAtts.axes2D.visible = 1
    AnnotationAtts.axes2D.autoSetTicks = 1
    AnnotationAtts.axes2D.autoSetScaling = 1
    AnnotationAtts.axes2D.lineWidth = 0
    AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Outside  # Inside, Outside, Both
    AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
    AnnotationAtts.axes2D.xAxis.title.visible = 0
    AnnotationAtts.axes2D.xAxis.title.font.font = AnnotationAtts.axes2D.xAxis.title.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes2D.xAxis.title.font.scale = 1
    AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
    AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes2D.xAxis.title.font.bold = 0
    AnnotationAtts.axes2D.xAxis.title.font.italic = 1
    AnnotationAtts.axes2D.xAxis.title.userTitle = 0
    AnnotationAtts.axes2D.xAxis.title.userUnits = 0
    AnnotationAtts.axes2D.xAxis.title.title = "X-Axis"
    AnnotationAtts.axes2D.xAxis.title.units = ""
    AnnotationAtts.axes2D.xAxis.label.visible = 0
    AnnotationAtts.axes2D.xAxis.label.font.font = AnnotationAtts.axes2D.xAxis.label.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes2D.xAxis.label.font.scale = 1
    AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
    AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes2D.xAxis.label.font.bold = 0
    AnnotationAtts.axes2D.xAxis.label.font.italic = 1
    AnnotationAtts.axes2D.xAxis.label.scaling = 0
    AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1
    AnnotationAtts.axes2D.xAxis.tickMarks.majorMinimum = 0
    AnnotationAtts.axes2D.xAxis.tickMarks.majorMaximum = 1
    AnnotationAtts.axes2D.xAxis.tickMarks.minorSpacing = 0.02
    AnnotationAtts.axes2D.xAxis.tickMarks.majorSpacing = 0.2
    AnnotationAtts.axes2D.xAxis.grid = 0
    AnnotationAtts.axes2D.yAxis.title.visible = 0
    AnnotationAtts.axes2D.yAxis.title.font.font = AnnotationAtts.axes2D.yAxis.title.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes2D.yAxis.title.font.scale = 1
    AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
    AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes2D.yAxis.title.font.bold = 0
    AnnotationAtts.axes2D.yAxis.title.font.italic = 1
    AnnotationAtts.axes2D.yAxis.title.userTitle = 0
    AnnotationAtts.axes2D.yAxis.title.userUnits = 0
    AnnotationAtts.axes2D.yAxis.title.title = "Y-Axis"
    AnnotationAtts.axes2D.yAxis.title.units = ""
    AnnotationAtts.axes2D.yAxis.label.visible = 0
    AnnotationAtts.axes2D.yAxis.label.font.font = AnnotationAtts.axes2D.yAxis.label.font.Arial  # Arial, Courier, Times
    AnnotationAtts.axes2D.yAxis.label.font.scale = 1
    AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
    AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
    AnnotationAtts.axes2D.yAxis.label.font.bold = 0
    AnnotationAtts.axes2D.yAxis.label.font.italic = 1
    AnnotationAtts.axes2D.yAxis.label.scaling = 0
    AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
    AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
    AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
    AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
    AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
    AnnotationAtts.axes2D.yAxis.grid = 0
    AnnotationAtts.userInfoFlag = 0
    AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
    AnnotationAtts.userInfoFont.scale = 1
    AnnotationAtts.userInfoFont.useForegroundColor = 1
    AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
    AnnotationAtts.userInfoFont.bold = 0
    AnnotationAtts.userInfoFont.italic = 0
    AnnotationAtts.databaseInfoFlag = 0
    AnnotationAtts.timeInfoFlag = 1
    AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
    AnnotationAtts.databaseInfoFont.scale = 1
    AnnotationAtts.databaseInfoFont.useForegroundColor = 1
    AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
    AnnotationAtts.databaseInfoFont.bold = 0
    AnnotationAtts.databaseInfoFont.italic = 0
    AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
    AnnotationAtts.databaseInfoTimeScale = 1
    AnnotationAtts.databaseInfoTimeOffset = 0
    AnnotationAtts.legendInfoFlag = 0

    visit.SetAnnotationAttributes(AnnotationAtts)
    return 0

def getlaststep(fname):
  ### open file
  f=open(fname)
  ### Read last line in a string
  lastline = f.readlines()[-1]
  laststep = lastline.rsplit()[0] 
  return(int(laststep))

def drawCrack(options):
    ##
    ## Add pseudocolor plot of fracture field
    ##

    AddPlot("Pseudocolor", "Damage", 1, 1)

    AddPlot("Subset", "ElementBlock", 1, 1)
    SetActivePlots(1)
    SubsetAtts = SubsetAttributes()
    SubsetAtts.colorType = SubsetAtts.ColorByColorTable  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
    SubsetAtts.colorTableName = "Default"
    SubsetAtts.invertColorTable = 0
    SubsetAtts.legendFlag = 1
    SubsetAtts.lineWidth = 0
    SubsetAtts.singleColor = (0, 0, 0, 255)
    SubsetAtts.SetMultiColor(0, (255, 0, 0, 255))
    SubsetAtts.SetMultiColor(1, (0, 255, 0, 255))
    SubsetAtts.SetMultiColor(2, (0, 0, 255, 255))
    SubsetAtts.subsetNames = ("2", "1", "3")
    SubsetAtts.opacity = 1
    SubsetAtts.wireframe = 0
    SubsetAtts.drawInternal = 0
    SubsetAtts.smoothingLevel = 0
    SubsetAtts.pointSize = 0.05
    SubsetAtts.pointType = SubsetAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
    SubsetAtts.pointSizeVarEnabled = 0
    SubsetAtts.pointSizeVar = "default"
    SubsetAtts.pointSizePixels = 2
    SetPlotOptions(SubsetAtts)
    SubsetAtts = SubsetAttributes()
    SubsetAtts.colorType = SubsetAtts.ColorByColorTable  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
    SubsetAtts.colorTableName = "gray"
    SubsetAtts.invertColorTable = 0
    SubsetAtts.legendFlag = 1
    SubsetAtts.lineWidth = 0
    SubsetAtts.singleColor = (0, 0, 0, 255)
    SubsetAtts.SetMultiColor(0, (255, 0, 0, 255))
    SubsetAtts.SetMultiColor(1, (0, 255, 0, 255))
    SubsetAtts.SetMultiColor(2, (0, 0, 255, 255))
    SubsetAtts.subsetNames = ("2", "1", "3")
    SubsetAtts.opacity = 1
    SubsetAtts.wireframe = 0
    SubsetAtts.drawInternal = 0
    SubsetAtts.smoothingLevel = 0
    SubsetAtts.pointSize = 0.05
    SubsetAtts.pointType = SubsetAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
    SubsetAtts.pointSizeVarEnabled = 0
    SubsetAtts.pointSizeVar = "default"
    SubsetAtts.pointSizePixels = 2
    SetPlotOptions(SubsetAtts)
    SubsetAtts = SubsetAttributes()
    SubsetAtts.colorType = SubsetAtts.ColorByColorTable  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
    SubsetAtts.colorTableName = "gray"
    SubsetAtts.invertColorTable = 0
    SubsetAtts.legendFlag = 1
    SubsetAtts.lineWidth = 0
    SubsetAtts.singleColor = (0, 0, 0, 255)
    SubsetAtts.SetMultiColor(0, (255, 0, 0, 255))
    SubsetAtts.SetMultiColor(1, (0, 255, 0, 255))
    SubsetAtts.SetMultiColor(2, (0, 0, 255, 255))
    SubsetAtts.subsetNames = ("2", "1", "3")
    SubsetAtts.opacity = 0.243137
    SubsetAtts.wireframe = 0
    SubsetAtts.drawInternal = 0
    SubsetAtts.smoothingLevel = 0
    SubsetAtts.pointSize = 0.05
    SubsetAtts.pointType = SubsetAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
    SubsetAtts.pointSizeVarEnabled = 0
    SubsetAtts.pointSizeVar = "default"
    SubsetAtts.pointSizePixels = 2
    SetPlotOptions(SubsetAtts)
    SubsetAtts = SubsetAttributes()
    SubsetAtts.colorType = SubsetAtts.ColorByColorTable  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
    SubsetAtts.colorTableName = "gray"
    SubsetAtts.invertColorTable = 0
    SubsetAtts.legendFlag = 0
    SubsetAtts.lineWidth = 0
    SubsetAtts.singleColor = (0, 0, 0, 255)
    SubsetAtts.SetMultiColor(0, (255, 0, 0, 255))
    SubsetAtts.SetMultiColor(1, (0, 255, 0, 255))
    SubsetAtts.SetMultiColor(2, (0, 0, 255, 255))
    SubsetAtts.subsetNames = ("2", "1", "3")
    SubsetAtts.opacity = 0.243137
    SubsetAtts.wireframe = 0
    SubsetAtts.drawInternal = 0
    SubsetAtts.smoothingLevel = 0
    SubsetAtts.pointSize = 0.05
    SubsetAtts.pointType = SubsetAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
    SubsetAtts.pointSizeVarEnabled = 0
    SubsetAtts.pointSizeVar = "default"
    SubsetAtts.pointSizePixels = 2
    SetPlotOptions(SubsetAtts)
    SubsetAtts = SubsetAttributes()
    SubsetAtts.colorType = SubsetAtts.ColorByColorTable  # ColorBySingleColor, ColorByMultipleColors, ColorByColorTable
    SubsetAtts.colorTableName = "gray"
    SubsetAtts.invertColorTable = 0
    SubsetAtts.legendFlag = 0
    SubsetAtts.lineWidth = 0
    SubsetAtts.singleColor = (0, 0, 0, 255)
    SubsetAtts.SetMultiColor(0, (255, 0, 0, 255))
    SubsetAtts.SetMultiColor(1, (0, 255, 0, 255))
    SubsetAtts.SetMultiColor(2, (0, 0, 255, 255))
    SubsetAtts.subsetNames = ("2", "1", "3")
    SubsetAtts.opacity = 0.243137
    SubsetAtts.wireframe = 0
    SubsetAtts.drawInternal = 0
    SubsetAtts.smoothingLevel = 0
    SubsetAtts.pointSize = 0.05
    SubsetAtts.pointType = SubsetAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
    SubsetAtts.pointSizeVarEnabled = 0
    SubsetAtts.pointSizeVar = "default"
    SubsetAtts.pointSizePixels = 2
    SetPlotOptions(SubsetAtts)

    AddOperator("Displace", 1)
    DisplaceAtts = DisplaceAttributes()
    DisplaceAtts.factor = options.displacementScaling
    DisplaceAtts.variable = "Displacement"
    SetOperatorOptions(DisplaceAtts, 0, 1)

    AddOperator("Isovolume", 1)
    IsovolumeAtts = IsovolumeAttributes()
    IsovolumeAtts.lbound = -1e+37
    IsovolumeAtts.ubound = options.damageThreshold
    IsovolumeAtts.variable = "Damage"
    SetOperatorOptions(IsovolumeAtts, 0,1)
    DrawPlots()

    if options.BB == None:
        Query("SpatialExtents", use_actual_data=1)
        newBB = GetQueryOutputValue() 
    else:
        newBB = tuple(options.BB)    
    SetView(newBB)
    return newBB
    
def SetView(BB):
    View2DAtts = View2DAttributes()
    View2DAtts.viewportCoords = (0.05, 0.95, 0.05, 0.95)
    View2DAtts.windowCoords = BB
    View2DAtts.fullFrameActivationMode = View2DAtts.Auto  # On, Off, Auto
    View2DAtts.fullFrameAutoThreshold = 100
    View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
    View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
    View2DAtts.windowValid = 1
    SetView2D(View2DAtts)

def setBGBlack():
    AnnotationAtts = GetAnnotationAttributes()
    AnnotationAtts.backgroundColor = (0, 0, 0, 255)
    AnnotationAtts.foregroundColor = (255, 255, 255, 255)
    SetAnnotationAttributes(AnnotationAtts)
    return 0

def setBGWhite():
    AnnotationAtts = GetAnnotationAttributes()
    AnnotationAtts.backgroundColor = (255, 255, 255, 255)
    AnnotationAtts.foregroundColor = (0, 0, 0, 255)
    SetAnnotationAttributes(AnnotationAtts)
    return 0

def plot(options):
    import json
    import os
    import os.path
    import shutil
    import math
    

    prefix,ext = os.path.splitext(options.inputfile)
    FramesDir = f'{prefix}-Frames'
    if not os.path.exists(FramesDir):
        os.makedirs(FramesDir)

    laststep = 1000000
    if options.step_max == 0:
        enerfile = enerfile = prefix+'.ener'
        if os.path.exists(enerfile):
            laststep = getlaststep(enerfile)
        else:
            enerfile = prefix.split('_out')[0]+'.ener'
            if os.path.exists(enerfile):
                laststep = getlaststep(enerfile)
            else:
                print ("unable to find step to plot.")
                return -1
        stepmax = laststep
    else:
        stepmax = options.step_max
    stepmin = options.step_min
    
    ##  
    ## Open the database
    ##
    MyDatabase = os.path.join(options.inputfile)
      
    print ('Trying to load {0}'.format(MyDatabase))
    status = OpenDatabase(MyDatabase, stepmin-1)       
    if not status:
        print ("unable to open database %s"%MyDatabase)
        return -1

    BB = drawCrack(options)
    W = BB[1]-BB[0]
    H = BB[3]-BB[2]
    if W > H:
        geometry = (2048,int(2048.*H/W))
    else:
        geometry = (int(2048.*W/H),2048)

    SetAnnotations()
    #DrawPlots()
    for step in range(stepmin,stepmax):
        SetTimeSliderState(step)
        filename = '{basename}-{step:04d}'.format(basename = os.path.join(FramesDir,prefix),step=step)
        setBGWhite()
        status = savePNG(filename,geometry)

    status = savePNG(f'{prefix}.png',geometry)
    DeleteAllPlots()
    CloseDatabase(MyDatabase)

    print('Done processing Frames for {0}.'.format(filename))
    cmd_exists = lambda x: any(os.access(os.path.join(path, x), os.X_OK) for path in os.environ["PATH"].split(os.pathsep))    
    # cmd = f'ffmpeg -y -i {FramesDir}/{prefix}-%04d.png -vcodec mjpeg -qscale 1  {prefix}.avi'.format(prefix=prefix)
    cmd = f'ffmpeg -y -i {FramesDir}/{prefix}-%04d.png -f mp4 -vcodec h264 -pix_fmt yuv420p {prefix}.mp4'
    if cmd_exists('ffmpeg'):
        os.system(cmd)
    else:
        print('\t{0}'.format(cmd))

    return 0

def parse(args=None):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('inputfile',help='input file')
    parser.add_argument('--displacementScaling',type=float,default=0)
    parser.add_argument('--damageThreshold',type=float,default=1.0)
    parser.add_argument('--step_min',type=int,default=1)
    parser.add_argument('--step_max',type=int,default=0)
    parser.add_argument('--BB',type=float,nargs=4,default=None)
    return parser.parse_args()

if __name__ == "__main__":
    import sys  
    import os.path

    options = parse()
    if os.path.exists(options.inputfile):   
        print('processing {0}'.format(options.inputfile)) 
        plot(options)   
        sys.exit(0)
    else:
        print('Unable to find input file {0}'.format(options.inputfile))
        sys.exit(-1)

