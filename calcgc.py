from construct_wing_v0 import *

import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#================================================================
#===================Create Gcode===========================
#================================================================


def write_gc(hotwire,model_name,panel_list,side):  
 
    
    SX1 = hotwire.param[2]
    SY1 = hotwire.param[3]
    SX2 = hotwire.param[4]
    SY2 = hotwire.param[5]
    
    
    for i,p in enumerate(panel_list):
    
        if side == "L" :
            file = './GCODE/'+model_name.split('.')[0]+'_panel_'+str(i+1) +'_L'+'.gc'
        elif side == "R":
            file = './GCODE/'+model_name.split('.')[0]+'_panel_'+str(i+1) +'_R'+'.gc'
        
        
        
       
        x1 =[]
        y1 =[]
        x2 =[]
        y2 =[]

        for j,c in enumerate(p.root_Y_extc):
            x1.append(c)
        iend_extrados = len(x1)
        for j,c in enumerate(p.root_Y_intc[::-1]):
            x1.append(c)
        for j,c in enumerate(p.root_Z_extc):
            y1.append(c)
        for j,c in enumerate(p.root_Z_intc[::-1]):
            y1.append(c)
        
        for j,c in enumerate(p.tip_Y_extc):
            x2.append(c)
        for j,c in enumerate(p.tip_Y_intc[::-1]):
            x2.append(c)
        for j,c in enumerate(p.tip_Z_extc):
            y2.append(c)
        for j,c in enumerate(p.tip_Z_intc[::-1]):
            y2.append(c)

        if side == "R" :
            x10 = x1
            y10 = y1
            x20 = x2
            y20 = y2
            
            x1 = x20
            y1 = y20
            x2 = x10
            y2 = y10
    
        with open(file, 'wt') as fileobj:
            fileobj.write("( Panel " + str(i+1) +") \n")
            if side == "L" :
                fileobj.write("( Left panel ) \n")
            elif side == "R" :
                fileobj.write("( Right panel ) \n")
            fileobj.write("( Starting extrados from LE to TE) \n")
           
            fileobj.write("( Coordinate in mm )\n")
            gcstring="G21"+'\n'
            fileobj.write(gcstring)

            fileobj.write("( Absolute mode)\n")
            gcstring="G90"+'\n'
            fileobj.write(gcstring)


            fileobj.write("( Travel rate  in mm/min) \n")
            gcstring="G94"+'\n'
            fileobj.write(gcstring)
            gcstring="F" +hotwire.param[1].strip()+'\n'
            fileobj.write(gcstring)
            
            
            
            
            for i in range(iend_extrados):
                
                gcstring="G1 "
                gcstring += SX1+str( "{:.2f}".format(x1[i]))+" " 
                gcstring += SY1+str( "{:.2f}".format(y1[i]))+" " 
                gcstring += SX2+str( "{:.2f}".format(x2[i]))+" " 
                gcstring += SY2+str( "{:.2f}".format(y2[i]))+" " +'\n'
                fileobj.write(gcstring)
          
            fileobj.write("( Pause for 2 s) \n") 
            gcstring="G4 P2 \n"
            fileobj.write(gcstring)
            
            fileobj.write("( Sarting Intrados from TE to LE) \n") 

   

            for i in range(iend_extrados+1,len(x1)-1):
                gcstring="G1 "
                gcstring += SX1+str( "{:.2f}".format(x1[i]))+" " 
                gcstring += SY1+str( "{:.2f}".format(y1[i]))+" " 
                gcstring += SX2+str( "{:.2f}".format(x2[i]))+" " 
                gcstring += SY2+str( "{:.2f}".format(y2[i]))+" " +'\n'
                fileobj.write(gcstring)

            fileobj.write("( Going back to origine) \n") 
            gcstring="G1 "
            gcstring += SX1+str( "{:.2f}".format(0.0))+" " 
            gcstring += SY1+str( "{:.2f}".format(0.0))+" " 
            gcstring += SX2+str( "{:.2f}".format(0.0))+" " 
            gcstring += SY2+str( "{:.2f}".format(0.0))+" " +'\n'
            fileobj.write(gcstring)               
        fileobj.close()


    
    return

    
def export_gc(model_name,panel_list,foam,hotwire):

    print(' Construct Coordinate of airfoils')
    foam_list_coord=calc_coord(panel_list,foam,hotwire)

    #plt.figure() 
    
    for ip, p in enumerate(panel_list):
        plt.figure() 
       
        print("   ")
        print("  Panel n", ip)
        print("    Building gcode...")
        # for  ipoint, x in enumerate(p.root_X):
        #     print(x,p.root_Y_ext0[ipoint],p.root_Z_ext0[ipoint])
     
        
        fcrt = foam_list_coord[ip]
        fcr = fcrt[0]
        fct = fcrt[1]
        
        c=fcr[0]
        x = c[0]
        y = c[1]
        plt.plot(x,y,'black')


        c=fct[0]
        x = c[0]
        y = c[1]
        plt.plot(x,y,'green')      

        plt.plot(p.root_Y_ext0, p.root_Z_ext0, 'r',p.root_Y_int0,p.root_Z_int0,'r')
        plt.plot(p.root_Y_ext1, p.root_Z_ext1, 'm',p.root_Y_int1,p.root_Z_int1,'m')       
        plt.plot(p.tip_Y_ext0, p.tip_Z_ext0, 'b',p.tip_Y_int0,p.tip_Z_int0,'b')       
        plt.plot(p.tip_Y_ext1, p.tip_Z_ext1, 'c',p.tip_Y_int1,p.tip_Z_int1,'c')  


        
        plt.legend(['root foam','tip foam',
                    'root ext', 'root int', 
                    'root ext kerf', 'root int kerf', 
                    'tip ext', 'tip int',
                    'tip ext kerf', 'tip int kerf' 
                    ])
        plt.axis('equal')
        plt.grid(True)
        plt.show() 
    
        plt.figure() 
        plt.plot(p.root_Y_extc, p.root_Z_extc, 'r',p.root_Y_intc,p.root_Z_intc,'r')
        plt.plot(p.tip_Y_extc, p.tip_Z_extc, 'b',p.tip_Y_intc,p.tip_Z_intc,'b')  
        plt.axis('equal')
        plt.grid(True)
        plt.show() 

        fig = plt.figure() 
        ax = fig.gca(projection='3d')
        ax.plot(p.root_X, p.root_Y_ext1, p.root_Z_ext1, label='Root', c='r')
        ax.plot(p.root_X, p.root_Y_int1, p.root_Z_int1,  c='r')
        ax.plot(p.tip_X, p.tip_Y_ext1, p.tip_Z_ext1, label='tip', c='b')
        ax.plot(p.tip_X, p.tip_Y_int1, p.tip_Z_int1,  c='b')

        carriage_length = float(hotwire.param[0])
        for i , y in enumerate(p.root_Y_extc):
            xx = [ 0.0 , carriage_length]
            yy = [y, p.tip_Y_extc[i] ]
            zz = [p.root_Z_extc[i], p.tip_Z_extc[i] ]
            if (i % 1) == 0:
                ax.plot(xx,yy, zz,  c='black')
        for i , y in enumerate(p.root_Y_intc):
            xx = [ 0.0 , carriage_length]
            yy = [y, p.tip_Y_intc[i] ]
            zz = [p.root_Z_intc[i], p.tip_Z_intc[i] ]
            if (i % 1) == 0:
                ax.plot(xx,yy, zz,  c='grey')

        # ax.plot([-10],[-10], [-10],  c='white')
        # ax.plot([600],[-10], [-10],  c='white')
        # ax.plot([600],[100], [-10],  c='white')
        # ax.plot([-10],[100], [-10],  c='white')
   
        # ax.plot([-10],[-10], [50],  c='white')

    write_gc(hotwire,model_name,panel_list,"L",)
    write_gc(hotwire,model_name,panel_list,"R")

    return 



    return  

