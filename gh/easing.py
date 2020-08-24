##########################
###      ghPython      ###
##########################


import sys
sys.path.append("C:\\Users\\ysoky\\Documents\\GH_Easing")
#print(sys.path)


import rhinoscriptsyntax as rs


from gh_easing import easing_geometry
reload(easing_geometry)


eg = easing_geometry.Easing_Geometry()

rr = 100

LINER = eg.easing_pts(POINTS, "LINER", rr)
CUBIC = eg.easing_pts(POINTS, "CUBIC", rr)
QUADRATIC = eg.easing_pts(POINTS, "QUADRATIC", rr)
QUINTIC = eg.easing_pts(POINTS, "QUINTIC", rr)
SINE = eg.easing_pts(POINTS, "SINE", rr)
CIRCULAR = eg.easing_pts(POINTS, "CIRCULAR", rr)
EXPONENTIAL = eg.easing_pts(POINTS, "EXPONENTIAL", rr)
ELASTIC = eg.easing_pts(POINTS, "ELASTIC", rr)
BACK = eg.easing_pts(POINTS, "BACK", rr)
BOUNCE = eg.easing_pts(POINTS, "BOUNCE", rr)
