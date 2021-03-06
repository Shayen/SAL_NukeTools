# earlier in your NUKE_PATH, for instance $HOME/.nuke/menu.py.

# Add python path
import sys, os, traceback
import nuke

sys.path.append('P:/_studioTool')
#sys.path.append('D:/WORK/Programming/project')
modulepath = os.path.dirname(__file__) + '/'

# Load pixelfudger Plugins
try:
	nuke.pluginAddPath(modulepath + 'pixelfudger')
	import pixelfudger
except ImportError as e:
	print ("Load plugin : pixelfudger Error")
	print e

# Load custom Plugins
try:
	nuke.pluginAddPath(modulepath + 'customGizmo')
	import customGizmo
except ImportError as e:
	print ("Load plugin : customGizmo Error")
	print e

# Add extra menu : SAL_tools

def loadRenderThread():
	try:
		from renderthreads import renderthreads
		reload(renderthreads)
		renderthreads.run()

	except ImportError:
		sys.path.append(modulepath + 'renderthreads')
		print("add path : " + modulepath + 'renderthreads' )

		try:
			from renderthreads import renderthreads
			reload(renderthreads)
			renderthreads.run()
		except Exception as e:
			print ("Import error : renderthreads")
			traceback.print_exc()

def layerSplitter():
	import layerSplitter
	reload (layerSplitter)
	layerSplitter.run()

def autoWrite():

	import autoWrite_nuke
	reload(autoWrite_nuke)
	autoWrite_nuke.run()


fileManager = "from sal_pipeline.app import projectExplorer_nuke \nreload(projectExplorer_nuke)\napp = projectExplorer_nuke.nuke_projectExplorer( )\napp.ui.show()"
# channelSplitter = 

nuke.menu('Nuke').addCommand('SAL Tools/File manager', fileManager)
nuke.menu('Nuke').addCommand('SAL Tools/Layers splitter', "layerSplitter()")
nuke.menu('Nuke').addCommand('SAL Tools/Renderthread',"loadRenderThread()")
nuke.menu('Nuke').addCommand('SAL Tools/AutoWrite',"autoWrite()")
print ("Add 'SAL tools' menu")
