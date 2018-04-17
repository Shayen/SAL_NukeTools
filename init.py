# Add python path
import sys, os
import nuke

sys.path.append('P:/_studioTool')
#sys.path.append('D:/WORK/Programming/project')
modulepath = 'P:/_studioTool/nuke' + '/'

# Load pixelfudger Plugins
try:
	nuke.pluginAddPath(modulepath + 'pixelfudger')
	import pixelfudger
except ImportError as e:
	print ("Load plugin : pixelfudger Error")
	print e

# Load custom Plugins
try:
	nuke.pluginAddPath(modulepath + 'customGizmo\gizmos')
	import customGizmo
except ImportError as e:
	print ("Load plugin : customGizmo Error")
	print e