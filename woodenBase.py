import FreeCAD,Part,math

class WoodenBase:

  def __init__(self,obj, longueurX=4000, largeurY=3000):
		obj.addProperty("App::PropertyFloat","front","WoodenBase","Front Width.").front = front
		obj.addProperty("App::PropertyFloat","depth","WoodenBase","Depth.").depth = depth
		obj.Proxy = self

  def onChanged(self, fp, prop):
 		"Do something when a property has changed"
		pass

  def execute(self, fp):
		fp.Shape=WoodenBase.buildshape(fp.front, fp.depth)
		
  @staticmethod
	def buildshape(front, depth):
		poutrePorteeMax = 5500
		
		shape = Part.Shape()
		return shape
		
def makeWoodenBase(x,y,doc=None):
  doc = doc or FreeCAD.ActiveDocument
  obj=doc.addObject("Part::FeaturePython","WoodenBase")
  WoodenBase(obj)
	obj.ViewObject.Proxy=0 # just set it to something different from None (this assignment is needed to run an internal notification)
  return obj      
            
if __name__ == '__main__':
	makeWoodenBase(4000,2000)

