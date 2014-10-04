#FLM: CA Add extension to glyph name
App = "CA Add extension to glyph name v1.0"

""" 
		12/2013 Thomas Schostok
		www.cape-arcona.com

		USE AT YOUR OWN RISK!

		Description:
		Script adds an extension to all selected glyph names
		
		Example:
		Before: "Glyphname" or
				"Glyphname.extension" 
		After:  "Glyphname.your_extension"		
		
		If an extension is already set in the glyph name, it strips out the extension name first.
	
 		Requirements:
		- FontLab Studio 5

		NO WARRANTY.
		Always make copies of your .vfbs and run the script on the copies! Save .vfbs regularly.
		Script may damage .vfb files or crash FLS5. Script is provided as is. There is no warranty
		for performance or results obtained by using the script. The creator of the script will not
		be liable for any damages, claims or costs whatsoever or any direct, indirect, special,
		incidental or consequential damages, business interruption, nor for lost profits, savings or
		business information, arising out of any use of, or inability to use, the scripts.
"""
		
class MyDialog:
  def __init__(self):
    self.d = Dialog(self)
    self.d.size = Point(300, 140)
    self.d.Center()
    self.d.title = "Add Extension to Glyph Name"
    self.d.AddControl(STATICCONTROL, Rect(aIDENT, aIDENT, aIDENT, aIDENT), "frame", STYLE_FRAME) 
    self.d.AddControl(STATICCONTROL, Rect(aIDENT2, aIDENT2, aAUTO, aAUTO), "label1", STYLE_LABEL, "Glyphname.extension") 
    self.d.AddControl(EDITCONTROL, Rect(160, aNEXT, aIDENT2, aAUTO), "ext", STYLE_EDIT, "Enter extension:") 

    self.ext = ""

  def on_ext(self, code):
    self.d.GetValue("ext")
  def on_ok(self, code):
    return 1
  def Run(self):
    return self.d.Run()

def reName(f, g, i): # font, glyph, extension
		# Strips out everything after the . including the .
		head, sep, tail = g.name.partition('.')
		# Rename when ext is set
		if ext!="":
			# Add . and extension to Glyph name
			g.name = head + "." + ext
			print "Renamed to " + g.name
		else:
			print "Canceled, missing extension"
d = MyDialog()
if d.Run()== 1:
	ext = d.ext
	print ext
	print "\nProcessing...!\n"
	fl.ForSelected(reName)
	fl.UpdateFont()
	print "***********************************"
	print "Done."	
else:
	print "Canceled."