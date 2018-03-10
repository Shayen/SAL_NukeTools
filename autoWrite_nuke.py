# AutoWrite

#Python
import os
import sys

#nuke
import nuke
import nukescripts

# salPipeline Module
from sal_pipeline.src import env

myenv  = env.getEnv()
info   = env.nuke_info()

_version_ = "2.1"
_WINDOWNAME_ = "Auto Write v.{version}".format(version = _version_)

# Version
# v1.0 : work fine
# v1.2 : Fix version bug
# v2.0 : add ui
# v2.1 : add file extension option
# v2.2 : add precomp

class layerPanel(nukescripts.PythonPanel):
	def __init__(self):

		nukescripts.PythonPanel.__init__( self, _WINDOWNAME_ )

		self.setMinimumSize(550, 100)

		self.knobs = []
		self.fileType = ['jpeg', 'exr', 'png', 'tiff']
		self.methodType = ['render', 'precomp']
		self.defaultFileType = 'exr'

		self.setupUi()

	def setupUi(self):
		''' setup UI elements '''
		renderPath = self._getRenderpath()

		# Render method
		self.method = nuke.Enumeration_Knob('renderMethod', 'Method :', self.methodType)
		
		# Renderpath  
		self.filepath = nuke.File_Knob('RenderPath', 'Render path :')
		self.filepath.setValue(renderPath)

		# Version
		self.version = nuke.String_Knob('version','version :')
		self.version.setValue(self._checkverison(renderPath))

		# File Type
		self.fileType = nuke.Enumeration_Knob('filetype', 'File type :', self.fileType)
		self.fileType.setValue(self.defaultFileType)

		# total file name
		self.fileName = nuke.Text_Knob('filename', 'filename :')
		self.fileName.setValue(self._getFileName())

		# --- add Knob ---
		self.setKnob(self.method)
		self.setKnob(self.filepath)
		self.setKnob(self.version)
		self.setKnob(self.fileType)
		self.setKnob(self.fileName)

	def setKnob(self, knob):
		self.knobs.append(knob)
		self.addKnob(knob)

	def knobChanged(self, knob):
		''' signal knob change '''

		# Set file path
		if knob.name()=='renderMethod' :
			if self.method.value() == 'precomp':
				self.filepath.setValue(self._getRenderpath()+"precomp")
			else :
				self.filepath.setValue(self._getRenderpath())

		# Set version
		if knob.name()=='RenderPath' or knob.name()=='renderMethod':
			self.version.setValue(self._checkverison(self.filepath.getValue()))

		# Set filename
		_knobNameList = ['version', 'filetype', 'RenderPath', 'renderMethod']
		if knob.name() in _knobNameList:
			self.fileName.setValue(self._getFileName())

	def _getRenderpath(self):
		'''
		return : "P:/smf_project/post_production/output/compout/q10_sh100"
		'''

		try :
			shotname	= "{seq}_{shot}".format(seq = info.get_sequence(), shot = info.get_shot())
			renderdir 	= '/'.join([info.renderPath, shotname])
			# P:/smf_project/post_production/output/compout/q10_sh100/v002/smf_s10_sh100_v002_compout.####.tiff

		except : 
			raise IOError("This file may not in pipeline.")

		return renderdir

	def _getFileName(self):
		''' 
		return : "smf_s10_sh100_v002_compout.####.tiff" 
		'''

		version = self.version.getValue()
		ext 	= self.fileType.value()

		if self.method.value() != 'precomp':
			method = "compOut"
		else :
			method = "precomp"

		filename 	= '{prjcode}_{seq}_{shot}_{version}_{method}.####.{ext}'.format( 	prjcode =info.get_projectCode(),
																						seq =info.get_sequence(),
																						shot=info.get_shot(),
																						version =version,
																						method = method,
																						ext= ext )

		return filename

	def _checkverison(self,renderdir):
		'''
		return : "0002"
		'''

		if not os.path.exists(renderdir):
			nuke.tprint("path not exists : " + renderdir)
			return ("0001")

		# Collect version
		dirs = [d for d in os.listdir(renderdir) if os.path.isdir(renderdir+'/'+d) and d.startswith("v")]
		dirs.sort()

		# if not have any version.
		if len(dirs) < 1 :
			nuke.tprint("dir count : " + str(len(dirs)))
			return ("0001")

		last_version = dirs[-1]
		next_version = "%04d"%(int(last_version.replace("v",'')) + 1)

		nuke.tprint("Render dir : " + renderdir)
		nuke.tprint("version :" + next_version)

		return next_version

	def setRender(self) :

		sel 	= nuke.selectedNode()
		crop 	= nuke.createNode("Crop")
		write 	= nuke.createNode("Write")

		crop.setInput(0, sel)
		write.setInput(0, crop)

		## Setup render path
		# Example : <ProjectPath>/post_production/output/compOut/sq0010_sh0010/v0001
		try :
			renderdir	= self.filepath.getValue()
			version 	= 'v'+self.version.getValue()
			filename 	= self._getFileName()

			renderPath  = '/'.join([renderdir, version, filename])

			nuke.tprint(renderPath)
			
			# nuke.tprint(os.path.dirname(renderPath))
			if not os.path.exists(os.path.dirname(renderPath)):
				os.makedirs(os.path.dirname(renderPath))
				nuke.tprint("make dirs : " + os.path.dirname(renderPath) )

			write['file'].setValue(renderPath)
		except Exception as e:
			nuke.tprint(str(e))

def run():
	app = layerPanel()
	result = app.showModalDialog()

	if result :
		app.setRender()
		pass