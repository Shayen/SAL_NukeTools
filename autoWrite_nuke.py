# AutoWrite

#Python
import os
import sys

#nuke
import nuke

# salPipeline Module
from salPipeline.src import env

env  = env.getEnv()
info = env.nuke_info()

def setRender():

	sel 	= nuke.selectedNode()
	write 	= nuke.createNode("Write")

	write.setInput(0, sel)

	## Setup render path
	# Example : <ProjectPath>/post_production/output/final

	shotname	= "{seq}_{shot}".format(seq = info.get_sequence(),shot = info.get_shot())
	version 	= ''
	filename 	= ''
	renderPath  = os.path.join(info.renderPath, 'compOut', shotname, version, filename)


def run():
	nuke.tprint ("Run autowrite")
	setRender()