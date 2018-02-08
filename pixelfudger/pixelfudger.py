import os
import nuke

modulPath = os.path.dirname(__file__) + '/'

t=nuke.menu("Nodes")
u=t.addMenu("Pixelfudger", icon=modulPath +"PxF_Menu.png")
 
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