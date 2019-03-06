# -*- coding: utf-8 -*-
"""
Created on Thu Feb 05 19:43:15 2015

@author: Duncan Parkes


# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""

import seidel
import matplotlib.pyplot as plt
from descartes import PolygonPatch
from shapely.geometry import  Polygon


test = [(235.04275999999999, 739.07534999999996),
(218.13066000000001, 719.73902999999996),
(218.15215000000001, 709.96821),
(218.17362, 700.19740000000002),
(243.15215000000001, 685.27858000000003),
(268.13065, 670.35974999999996),
(268.13065, 660.81429000000003),
(268.13065, 651.26882999999998),
(314.55921999999998, 651.26882999999998),
(360.98779000000002, 651.26882999999998),
(360.98683999999997, 666.44740000000002),
(360.98046561000007, 669.27438118000009),
(360.96234088000011,672.68539864000013),
(360.93345946999995, 676.58895225999993),
(360.89481504000003, 680.89354191999996),
(360.84740125000002, 685.50766749999991),
(360.79221175999999, 690.33982888000003),
(360.73024022999999, 695.29852593999999),
(360.66248032000004, 700.29225856000005),
(360.58992569000003, 705.22952662000012),
(360.51357000000002, 710.01882999999998),
(360.04131999999998, 738.41168000000005),
(310.51454999999999, 738.41168000000005),
(260.98779999999999, 738.41168000000005),
(260.98779999999999, 748.41168000000005),
(260.98779999999999, 758.41168000000005),
(256.47133000000002, 758.41168000000005),
(251.95484999999999, 758.41168000000005)
]

seid = seidel.Triangulator(test)

triangles = seid.triangles()
trapezoids = seid.trapezoids
#trapezoids = seidel.trapezoidal_map.

trapezoid_verts_list = [(),]

plt.figure()

for t in trapezoids:
    verts = t.vertices()
    plt.gca().add_patch(PolygonPatch(Polygon(verts)))
    plt.gca().autoscale(tight=False)
    trapezoid_verts_list.append(verts)

plt.show()

# add new vertices to original polygon vertices list
new_poly_coords = list.copy(test)

#add non-duplicate vertices
for i in range(0, len(trapezoid_verts_list)):
        for j in range(0,len(trapezoid_verts_list[i])):
            x = (trapezoid_verts_list[i][j])
            if x in test:
                pass
            else:
                new_poly_coords.append(x)
    
new_poly_coords = list(set(new_poly_coords)) #remove duplicates by converting to set
    
#sort new poly coords in ccw 
#new_poly_coords = sorted(new_poly_coords, key=lambda k: [k[0], k[1]])
new_poly_coords = seidel.ccw_sort(new_poly_coords)

fig,ax = plt.subplots()    
xb = [i[0] for i in new_poly_coords[:]]
yb = [i[1] for i in new_poly_coords[:]]
ax.plot(xb,yb, color='r')
'''
plt.gca().add_patch(PolygonPatch(Polygon(new_poly_coords)))
plt.gca().autoscale(tight=False)
'''
plt.show()