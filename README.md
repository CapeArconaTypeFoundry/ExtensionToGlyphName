ExtensionToGlyphName
====================

A FontLab Studio 5 Script

Description:
Simple script that adds an extension/suffix to all selected glyph names. Probably not needful for experts, but we found the internal function of renaming/adding suffixes inside FontLab not handy enough for our needs, so we wrote our own script. Use it or leave it.

Example:
Before:	"Glyphname" or
	"Glyphname.extension" 
After:	"Glyphname.your_extension"		

If an extension is already set in the glyph name, it strips out the extension name first.

![Add Extension to glyphs in Fontlab](https://github.com/CapeArconaTypeFoundry/ExtensionToGlyphName/blob/master/add_extension.png)
