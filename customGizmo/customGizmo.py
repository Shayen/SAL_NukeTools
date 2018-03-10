import os
import nuke

modulPath = os.path.dirname(__file__) + '/'
iconsPath = modulPath + 'icons'
GizmosPath= modulPath + 'gizmos'

nuke.pluginAddPath(modulPath+'gizmos')
nuke.pluginAddPath(modulPath+'icons')

t=nuke.menu("Nodes")
u=t.addMenu("customGizmos", icon = iconsPath +"/main.png")

'''
m.addCommand("Example 1", "nuke.createNode(\"Example 2\")", icon="ICON.png")

Example 1: This is the name that wil appear in your menu, this name does not need to match your Gizmo, name it whatever you want. (This will not show up in your DAG, See Example 2)
Example 2: This is the Gizmo you want Nuke to create. If you put it in your "gizmos" folder, you'll be fine. Be sure to replace "Example 2" with the exact name of your Gizmo. You can change the name of your gizmo and then change "Example 2" to match if you don't like the name of the Gizmo. (This will be the name that shows up in your DAG)
If you want more than one Menu within your Menu.py file,  this is what your menu.py file should look like:
Be sure you set an icon for each of them, you can use the same Icon for all of them also. 
'''

def getIcon(gizmoName):

	if os.path.exists(iconsPath + '/' + gizmoName + '.png'):
		return(iconsPath + '/' + gizmoName + '.png')
	else :
		return(iconsPath + '/missingIcon.png')


# add custom menu
gizmos = [os.path.splitext(g)[0] for g in os.listdir(GizmosPath) if g.endswith('.gizmo')]
for gizmo in gizmos :
	menuname = "customGizmos/{gizmoName}".format(gizmoName = gizmo)
	command  = "nuke.createNode('{gizmoName}')".format(gizmoName = gizmo)
	icon     = getIcon(gizmoName = gizmo)
	t.addCommand( menuname, command, icon= icon ) 

print ("customGizmo loaded")