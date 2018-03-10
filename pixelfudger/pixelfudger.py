import os
import nuke

modulPath = os.path.dirname(__file__) + '/'

print ("Pixelfudger Loaded")

t=nuke.menu("Nodes")
u=t.addMenu("Pixelfudger", icon=modulPath +"PxF_Menu.png")

'''
m.addCommand("Example 1", "nuke.createNode(\"Example 2\")", icon="ICON.png")

Example 1: This is the name that wil appear in your menu, this name does not need to match your Gizmo, name it whatever you want. (This will not show up in your DAG, See Example 2)
Example 2: This is the Gizmo you want Nuke to create. If you put it in your "gizmos" folder, you'll be fine. Be sure to replace "Example 2" with the exact name of your Gizmo. You can change the name of your gizmo and then change "Example 2" to match if you don't like the name of the Gizmo. (This will be the name that shows up in your DAG)
If you want more than one Menu within your Menu.py file,  this is what your menu.py file should look like:
Be sure you set an icon for each of them, you can use the same Icon for all of them also. 
'''
t.addCommand( "Pixelfudger/PxF_Bandpass", "nuke.createNode('PxF_Bandpass')", icon=modulPath + "PxF_Bandpass.png" ) 
t.addCommand( "Pixelfudger/PxF_ChromaBlur", "nuke.createNode('PxF_ChromaBlur')", icon=modulPath + "PxF_ChromaBlur.png") 
t.addCommand( "Pixelfudger/PxF_Distort", "nuke.createNode('PxF_Distort')", icon=modulPath + "PxF_Distort.png") 
t.addCommand( "Pixelfudger/PxF_Erode", "nuke.createNode('PxF_Erode')", icon=modulPath + "PxF_Erode.png")
t.addCommand( "Pixelfudger/PxF_Filler", "nuke.createNode('PxF_Filler')", icon=modulPath + "PxF_Filler.png") 
t.addCommand( "Pixelfudger/PxF_Grain", "nuke.createNode('PxF_Grain')", icon=modulPath + "PxF_Grain.png") 
t.addCommand( "Pixelfudger/PxF_HueSat", "nuke.createNode('PxF_HueSat')", icon=modulPath + "PxF_HueSat.png")  
t.addCommand( "Pixelfudger/PxF_IDefocus", "nuke.createNode('PxF_IDefocus')", icon=modulPath + "PxF_IDefocus.png")
t.addCommand( "Pixelfudger/PxF_KillSpill", "nuke.createNode('PxF_KillSpill')", icon=modulPath + "PxF_KillSpill.png") 
t.addCommand( "Pixelfudger/PxF_Line", "nuke.createNode('PxF_Line')", icon=modulPath + "PxF_Line.png" ) 
t.addCommand( "Pixelfudger/PxF_MergeWrap", "nuke.createNode('PxF_MergeWrap')", icon=modulPath + "PxF_MergeWrap.png" ) 
t.addCommand( "Pixelfudger/PxF_ScreenClean", "nuke.createNode('PxF_ScreenClean')", icon=modulPath + "PxF_ScreenClean.png")