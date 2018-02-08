# Nuke layer splitter
'''
- pro process
+ Select Read node > Run script
+ List all chanel in Readnode : Show in checkbox

- Run splitter
+ Create shuffle node with name
+ create Merge node, point
'''
import nuke
import nukescripts

_WINDOWNAME_ = "SAL layers splitter"

class core():
	''' core class of cannel splitter '''

	def listlayerFromNode(self, node):
		'''
		List layer and layer from node

		input : @node : [node object]

		return: List of layers
		'''

		layerList 	= []
		channelList = node.channels()

		for channel in channelList :
			layer_name = channel.split('.')[0]
			if not layer_name in layerList :
				layerList.append(layer_name)

		return layerList

core = core()

class layerPanel():
	def __init__(self):
		# nuke.Panel.__init__(self, _WINDOWNAME_)
		self.ui 		= nuke.Panel(_WINDOWNAME_)
		self.node 		= nuke.selectedNode()
		self.nodePos 	= (self.node.xpos(), self.node.ypos())

		self.setupUi()

	def setupUi(self):
		''' setup UI elements '''
		self.ui.addEnumerationPulldown("Enable postage_stamp :", "Enable Disable")
		self.ui.addEnumerationPulldown("Create merge :", "Enable Disable")

		self._setupLayerList()

	def _setupLayerList(self):
		layerList = core.listlayerFromNode(self.node)

		for layerName in layerList :
			self.ui.addBooleanCheckBox(layerName, False)

	def createTemplate(self):
		''' Generate template from given layer '''

		is_enablePostStamp 	= True if self.ui.value("Enable postage_stamp :") == "Enable" else False
		is_createMerge		= True if self.ui.value("Create merge :") == "Enable" else False

		# Get value
		values = []  
		for name in core.listlayerFromNode(self.node):
			values.append( (name, self.ui.value(name)) )

		# Create Dot
		dot = nuke.createNode("Dot")
		dot.setXYpos(dot.xpos() , self.nodePos[1] + 150)

		# Generate
		for name, value in values :
			nuke.tprint([name, value])
			if value != 1 :
				continue

			node = nuke.createNode('Shuffle')
			# node.setXYpos(node.xpos() - 150 , dot.ypos()-35)
			node.setXYpos(dot.xpos() - 35 , node.ypos()+50)
			node['label'].setValue("[knob in]")
			node['postage_stamp'].setValue(is_enablePostStamp)
			node['in'].setValue(name)
		
def run():
	app = layerPanel()
	result = app.ui.show()

	if result :
		app.createTemplate()