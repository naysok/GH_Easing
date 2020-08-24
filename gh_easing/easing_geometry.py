import rhinoscriptsyntax as rs

from . import easing_p


class Easing_Geometry():

    def remap_number(self, src, old_min, old_max, new_min, new_max):
        return ((src - old_min) / (old_max - old_min) * (new_max - new_min) + new_min)


    def easing_2pt(self, p0, p1, mode, res):

        x0, y0, z0 = p0
        x1, y1, z1 = p1

        pts = []
        
        for i in xrange(res + 1):
            
            if i != res:
                xx = (1.0 / res) * i
            else:
                # print("Last, {}".format(i))
                xx = 1.0

            if mode == "LINER":
                yy = easing_p.LinearInterpolation(xx)

            elif mode == "CUBIC":
                yy = easing_p.CubicEaseInOut(xx)
            
            elif mode == "QUADRATIC":
                yy = easing_p.QuadraticEaseInOut(xx)
            
            elif mode == "QUINTIC":
                yy = easing_p.QuinticEaseInOut(xx)
            
            elif mode == "SINE":
                yy = easing_p.SineEaseInOut(xx)
            
            elif mode == "CIRCULAR":
                yy = easing_p.CircularEaseInOut(xx)
            
            elif mode == "EXPONENTIAL":
                yy = easing_p.ExponentialEaseInOut(xx)

            elif mode == "ELASTIC":
                yy = easing_p.ElasticEaseInOut(xx)
            
            elif mode == "BACK":
                yy = easing_p.BackEaseInOut(xx)

            elif mode == "BOUNCE":
                yy = easing_p.BounceEaseInOut(xx)

            else:
                yy = easing_p.LinearInterpolation(xx)

            xxx = self.remap_number(xx, 0.0, 1.0, x0, x1)
            yyy = self.remap_number(yy, 0.0, 1.0, y0, y1)

            pt = rs.AddPoint(xxx, yyy, 0.0)
            pts.append(pt)

        return rs.AddInterpCurve(pts)


    def easing_pts(self, pts, mode, res):
        
        pts_geo = rs.coerce3dpointlist(pts)

        crvs = []
        for i in xrange(len(pts_geo) - 1):
            p0 = pts_geo[i]
            p1 = pts_geo[i+1]

            ### Easing 2points
            crv = self.easing_2pt(p0, p1, mode, res)
            crvs.append(crv)
        

        crv_joined = rs.JoinCurves(crvs)
        
        # return crvs
        return crv_joined

