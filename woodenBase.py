import FreeCAD,Part,math

class WoodenBase:

  def __init__(self,obj, front=3000, rear=1000, rearOffset=1000, depth=3000, framingTimberX=50, framingTimberY=75, supportTimberX=100, supportTimberY=100):
		obj.addProperty("App::PropertyFloat","front","WoodenBase","Front Width.").front = front
		obj.addProperty("App::PropertyFloat","rear","WoodenBase","Rear Width.").rear = rear
		obj.addProperty("App::PropertyFloat","rearOffset","WoodenBase","Rear Offset.").rearOffset = rearOffset
		obj.addProperty("App::PropertyFloat","depth","WoodenBase","Depth.").depth = depth
		obj.addProperty("App::PropertyFloat","framingTimberX","WoodenBase","X of framing timber.").framingTimberX = framingTimberX
		obj.addProperty("App::PropertyFloat","framingTimberY","WoodenBase","Y of framing timber.").framingTimberY = framingTimberY
		obj.addProperty("App::PropertyFloat","supportTimberX","WoodenBase","X of support timber.").supportTimberX = supportTimberX
		obj.addProperty("App::PropertyFloat","supportTimberY","WoodenBase","Y of support timber.").supportTimberY = supportTimberY
		obj.Proxy = self

  def onChanged(self, fp, prop):
    "Do something when a property has changed"
    pass

  def execute(self, fp):
    FreeCAD.Console.PrintMessage("Execute..\n")
    fp.Shape=WoodenBase.buildshape(fp.front, fp.rear, fp.rearOffset, fp.depth, fp.framingTimberX, fp.framingTimberY, fp.supportTimberX, fp.supportTimberY)

  # see http://www.freecadweb.org/wiki/index.php?title=FreeCAD_Scripting_Basics		
  @staticmethod
  def buildshape(front, rear, rearOffset, depth, framingTimberX, framingTimberY, supportTimberX, supportTimberY):
    FreeCAD.Console.PrintMessage("buildshape..\n")
    # result = Part.shape()
    frontPiece = Part.makeBox(front,framingTimberX,framingTimberY)
    leftPiece = Part.makeBox(framingTimberX, depth, framingTimberY, App.Vector(-(framingTimberX),0,0))
    rightPiece = Part.makeBox(framingTimberX, depth, framingTimberY, App.Vector(front,0,0))
    backPiece = Part.makeBox(rear,framingTimberX,framingTimberY, App.Vector(rearOffset,depth-framingTimberX,0))
    # result.fuse(frontPiece)
    result = frontPiece.fuse(leftPiece)
    result = result.fuse(rightPiece)
    result = result.fuse(backPiece)
    FreeCAD.Console.PrintMessage("finished building.... return.\n")
    return result
		
def makeWoodenBase(front,rear,rearOffset, depth,framingTimberX,framingTimberY, supportTimberX, supportTimberY, doc=None):
  FreeCAD.Console.PrintMessage("makeWoodenBase..\n")
  doc = doc or FreeCAD.ActiveDocument
  obj=doc.addObject("Part::FeaturePython","WoodenBase")
  WoodenBase(obj)
  obj.ViewObject.Proxy=0 # just set it to something different from None (this assignment is needed to run an internal notification)
  return obj      

FreeCAD.Console.PrintMessage("running..\n")
makeWoodenBase(3000,3000,0,2000,75,50,100,100)
App.activeDocument().recompute()
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxometric()

