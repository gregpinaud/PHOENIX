# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 22:03:18 2021

@author: Jacynthe
"""
import re
import numpy as np
from scipy import interpolate
import math


import tkinter as tk
from tkinter import messagebox

global d2r, r2d


d2r = math.pi /180.0
r2d = 1.0/d2r

def read_profile(filename_profil):
     """Reading Airfoil"""
     print("     Reading airfoil ")
     # Regex to identify data rows and throw away unused metadata
     yval = '(?P<yval>(\-|\d*)\.\d+(E\-?\d+)?)'
     zval = '(?P<zval>\-?\s*\d*\.\d+(E\-?\d+)?)'
     _regex = '^\s*' + yval + '\,?\s*' + zval + '\s*$'
     regex = re.compile(_regex)

     file = open(filename_profil, 'r')

     Y_Profile =[]
     Z_Profile =[]
     npts = 0
    


     for line in file:
         curdat = regex.match(line)

         if curdat is not None:
             y = float(curdat.group("yval"))
             z = float(curdat.group("zval"))
             # the normal processing
             Y_Profile.append(y)
             Z_Profile.append(z)
             npts +=1


     file.close()

     print("        Npoints Profile=",npts)



     # Separation Intrados Extrados
     Y_Ext_Profile =[]
     Y_Int_Profile =[]
     Z_Ext_Profile =[]
     Z_Int_Profile =[]

     # step = 1

     # for i in range(0,npts-1,step):
     #     y =  Y_Profile[i]
     #     z =  Z_Profile[i]

     #     if (z >= 0.0 ) :
     #         Y_Ext_Profile.append(y)
     #         Z_Ext_Profile.append(z)
     #     if (z <= 0.0 ) :
     #         Y_Int_Profile.append(y)
     #         Z_Int_Profile.append(z)

     # if (i != (npts)) :
     #     y =  Y_Profile[npts-1]
     #     z =  Z_Profile[npts-1]
     #     Y_Int_Profile.append(y)
     #     Z_Int_Profile.append(z)
     
     step = 1
     y0 =  10.0
     for i in range(0,npts-1,step):
          y =  Y_Profile[i]
          z =  Z_Profile[i]
          dy = y-y0
          y0 = y
          if(dy <=0) :
              Y_Ext_Profile.append(y)
              Z_Ext_Profile.append(z)
          else:
              Y_Int_Profile.append(y)
              Z_Int_Profile.append(z)
         
         
     
     return  npts,Y_Ext_Profile , Y_Int_Profile, Z_Ext_Profile, Z_Int_Profile


def resampling(Y_Ext_Profile0 , Y_Int_Profile0, Z_Ext_Profile0, Z_Int_Profile0,num_points):
    """ resemling de tous les profils nintrados et extrados sur 100 points """
    
    teta =np.asarray(np.linspace(0.0, math.pi, num_points))
    y0 = 0.5*(1.0-np.cos(teta))
    
    Y_Ext_Profile = y0
    Y_Int_Profile = y0  
 
    y = np.asarray(np.flip(Y_Ext_Profile0))
    z = np.asarray(np.flip(Z_Ext_Profile0)) 
    

    tck = interpolate.splrep(y,z,s=0)
    Z_Ext_Profile = interpolate.splev(y0,tck, der=0)
    
    y = np.asarray(Y_Int_Profile0)
    z = np.asarray(Z_Int_Profile0)  
    tck = interpolate.splrep(y,z,s=0)
    Z_Int_Profile = interpolate.splev(y0,tck, der=0)    
    
    return Y_Ext_Profile , Y_Int_Profile, Z_Ext_Profile, Z_Int_Profile


def rotate(p):
     """Rotation around the Hinge point  for the twist angle"""
     #print('Dans Rotate...')  
     y_hl = float(p.root_hingex)/100.0*float(p.rootchord)
     tck = interpolate.splrep(p.root_Y_ext0,p.root_Z_ext0,s=0)
     z_hl_ext = interpolate.splev(y_hl,tck, der=0)
     
     tck = interpolate.splrep(p.root_Y_int0,p.root_Z_int0,s=0)
     z_hl_int = interpolate.splev(y_hl,tck, der=0)
    
     z_hl= 0.5*(z_hl_ext + z_hl_int )
    
     #print('Root hinge line coord',y_hl, z_hl)
     yext = p.root_Y_ext0 - y_hl
     yint = p.root_Y_int0 - y_hl

     zext = p.root_Z_ext0 - z_hl
     zint = p.root_Z_int0 - z_hl
    
    
     cos_twist = np.cos(float(p.root_washout)*d2r)
     sin_twist = np.sin(float(p.root_washout)*d2r)
     M =[[cos_twist, -sin_twist],  [sin_twist, cos_twist]   ]
   
     p.root_Y_ext0 = y_hl + yext*M[0][0] + zext*M[0][1]
     p.root_Z_ext0 =        yext*M[1][0] + zext*M[1][1]
  
     p.root_Y_int0 = y_hl + yint*M[0][0] + zint*M[0][1]
     p.root_Z_int0 =        yint*M[1][0] + zint*M[1][1]

  


     y_hl = float(p.tip_hingex)/100.0*float(p.tipchord) 
     tck = interpolate.splrep(p.tip_Y_ext0,p.tip_Z_ext0,s=0)
     z_hl_ext= interpolate.splev(y_hl,tck, der=0)
     
     tck = interpolate.splrep(p.tip_Y_int0,p.tip_Z_int0,s=0)
     z_hl_int= interpolate.splev(y_hl,tck, der=0)
      
     z_hl=  0.5*(z_hl_ext + z_hl_int )
     
     #print('tip hinge line coord: ',y_hl, z_hl)    
     
     yext = p.tip_Y_ext0 - y_hl
     yint = p.tip_Y_int0 - y_hl

     zext = p.tip_Z_ext0 - z_hl
     zint = p.tip_Z_int0 - z_hl

     cos_twist = np.cos(float(p.tip_washout)*d2r)
     sin_twist = np.sin(float(p.tip_washout)*d2r)
     M =[[cos_twist, -sin_twist],  [sin_twist, cos_twist]   ]
   
     p.tip_Y_ext0 = y_hl + yext*M[0][0] + zext*M[0][1]
     p.tip_Z_ext0 =        yext*M[1][0] + zext*M[1][1]
  
     p.tip_Y_int0 = y_hl + yint*M[0][0] + zint*M[0][1]
     p.tip_Z_int0 =        yint*M[1][0] + zint*M[1][1]

  
     return


    
def add_kerf(p,hotwire):
    """Adding Kerf"""
    print("Adding Kerf to panel")
    # length ratio between root and tip
    srext = 0.0
    for i in range(len(p.root_Y_ext0)-1):
        yi = p.root_Y_ext0[i] 
        zi = p.root_Z_ext0[i]
        y  = p.root_Y_ext0[i+1]
        z  = p.root_Z_ext0[i+1]        
        srext +=  math.sqrt(  math.pow(y-yi,2)  +  math.pow(z-zi,2) ) 

    srint = 0.0
    for i in range(len(p.root_Y_int0)-1):
        yi = p.root_Y_int0[i] 
        zi = p.root_Z_int0[i]
        y  = p.root_Y_int0[i+1]
        z  = p.root_Z_int0[i+1]        
        srint +=  math.sqrt(  math.pow(y-yi,2)  +  math.pow(z-zi,2) ) 


    stext = 0.0
    for i in range(len(p.tip_Y_ext0)-1):
        yi = p.tip_Y_ext0[i]
        zi = p.tip_Z_ext0[i]
        y  = p.tip_Y_ext0[i+1]
        z  = p.tip_Z_ext0[i+1]        
        stext +=  math.sqrt(  math.pow(y-yi,2)  +  math.pow(z-zi,2) ) 

    stint = 0.0
    for i in range(len(p.tip_Y_int0)-1):
        yi = p.tip_Y_int0[i]
        zi = p.tip_Z_int0[i]
        y  = p.tip_Y_int0[i+1]
        z  = p.tip_Z_int0[i+1]        
        stint +=  math.sqrt(  math.pow(y-yi,2)  +  math.pow(z-zi,2) ) 

    speed_ratio_ext = stext/srext
    speed_ratio_int = stint/srint

    

# Estimation of the speed at the root and tip and associated kerf
    carriage_max_feed_rate = float(hotwire.param[1])
    xr = p.root_X[0]
    xt = p.tip_X[0]
    carriage_length = float(hotwire.param[0])
    panel_length = float(p.panel_span)

    root_feed_rate_ext = carriage_max_feed_rate*panel_length/(xt-xr*speed_ratio_ext)
    root_feed_rate_int = carriage_max_feed_rate*panel_length/(xt-xr*speed_ratio_int)
    
    tip_feed_rate_ext = carriage_max_feed_rate*panel_length/(xt/speed_ratio_ext -xr)
    tip_feed_rate_int = carriage_max_feed_rate*panel_length/(xt/speed_ratio_int -xr)

    kerf0 =0
    kerf0 = float(hotwire.param[8]) -kerf_law(carriage_max_feed_rate,kerf0)
    
    kerf_root_ext = kerf_law(root_feed_rate_ext,kerf0)
    kerf_root_int = kerf_law(root_feed_rate_int,kerf0)
    kerf_tip_ext = kerf_law(tip_feed_rate_ext,kerf0)
    kerf_tip_int = kerf_law(tip_feed_rate_int,kerf0)    

    # print(root_feed_rate_ext,root_feed_rate_int,tip_feed_rate_ext,tip_feed_rate_int)
    # print(kerf_root_ext,kerf_root_int,kerf_tip_ext,kerf_tip_int)
    p.root_Y_ext1=[]
    p.root_Z_ext1=[]
    for i in range(len(p.root_Y_ext0)-1):
            yi = p.root_Y_ext0[i] 
            zi = p.root_Z_ext0[i]
            y  = p.root_Y_ext0[i+1]
            z  = p.root_Z_ext0[i+1]        
            vect_tg = [ y -yi  ,  z-zi ]
            vect_n = np.asarray( [  -vect_tg[1],  vect_tg[0] ] )
            mod_n = norm(vect_n)
            vect_n= vect_n/mod_n
            p.root_Y_ext1.append(p.root_Y_ext0[i] +vect_n[0]*kerf_root_ext)
            p.root_Z_ext1.append(p.root_Z_ext0[i] +vect_n[1]*kerf_root_ext)
    
    p.root_Y_ext1.append( p.root_Y_ext0[len(p.root_Y_ext0)-1] +vect_n[0]*kerf_root_ext )
    p.root_Z_ext1.append( p.root_Z_ext0[len(p.root_Y_ext0)-1] +vect_n[1]*kerf_root_ext )

    p.root_Y_int1=[]
    p.root_Z_int1=[]
    for i in range(len(p.root_Y_int0)-1):
            yi = p.root_Y_int0[i] 
            zi = p.root_Z_int0[i]
            y  = p.root_Y_int0[i+1]
            z  = p.root_Z_int0[i+1]        
            vect_tg = [ y -yi  ,  z-zi ]
            vect_n = np.asarray( [   vect_tg[1],  -vect_tg[0] ] )
            mod_n = norm(vect_n)
            vect_n= vect_n/mod_n
            p.root_Y_int1.append(p.root_Y_int0[i] +vect_n[0]*kerf_root_ext)
            p.root_Z_int1.append(p.root_Z_int0[i] +vect_n[1]*kerf_root_ext)
    
    p.root_Y_int1.append(p.root_Y_int0[len(p.root_Y_int0)-1] +vect_n[0]*kerf_root_ext)
    p.root_Z_int1.append(p.root_Z_int0[len(p.root_Y_int0)-1] +vect_n[1]*kerf_root_ext)



    p.tip_Y_ext1=[]
    p.tip_Z_ext1=[]
    for i in range(len(p.tip_Y_ext0)-1):
            yi = p.tip_Y_ext0[i] 
            zi = p.tip_Z_ext0[i]
            y  = p.tip_Y_ext0[i+1]
            z  = p.tip_Z_ext0[i+1]        
            vect_tg = [ y -yi  ,  z-zi ]
            vect_n = np.asarray( [  -vect_tg[1],  vect_tg[0] ] )
            mod_n = norm(vect_n)
            vect_n= vect_n/mod_n
            p.tip_Y_ext1.append(p.tip_Y_ext0[i] +vect_n[0]*kerf_tip_ext)
            p.tip_Z_ext1.append(p.tip_Z_ext0[i] +vect_n[1]*kerf_tip_ext)
    
    p.tip_Y_ext1.append( p.tip_Y_ext0[len(p.tip_Y_ext0)-1] +vect_n[0]*kerf_tip_ext )
    p.tip_Z_ext1.append( p.tip_Z_ext0[len(p.tip_Y_ext0)-1] +vect_n[1]*kerf_tip_ext )

    p.tip_Y_int1=[]
    p.tip_Z_int1=[]
    for i in range(len(p.tip_Y_int0)-1):
            yi = p.tip_Y_int0[i] 
            zi = p.tip_Z_int0[i]
            y  = p.tip_Y_int0[i+1]
            z  = p.tip_Z_int0[i+1]        
            vect_tg = [ y -yi  ,  z-zi ]
            vect_n = np.asarray( [   vect_tg[1],  -vect_tg[0] ] )
            mod_n = norm(vect_n)
            vect_n= vect_n/mod_n
            p.tip_Y_int1.append(p.tip_Y_int0[i] +vect_n[0]*kerf_tip_ext)
            p.tip_Z_int1.append(p.tip_Z_int0[i] +vect_n[1]*kerf_tip_ext)
    
    p.tip_Y_int1.append(p.tip_Y_int0[len(p.tip_Y_int0)-1] +vect_n[0]*kerf_tip_ext)
    p.tip_Z_int1.append(p.tip_Z_int0[len(p.tip_Y_int0)-1] +vect_n[1]*kerf_tip_ext)





    return


def kerf_law(v,k0):
    """ estimated feed rate correction of the kerf , v in  mm/min , kerf in mm"""
    kerf = k0 + 11.054*math.pow(v,-0.485)
    return kerf

def norm(vect):
    """ norme of the vector"""
    mod2= 0
    for vc in vect:
        mod2 += math.pow(vc,2)
    mod = math.sqrt(mod2)
    return mod 

def carriage_projection(p,hotwire,foam):
     """Projection of the airfoil trace on the carriage axis """
     print("Trace on carriage axis for panel")
     eps = 1.0e-6
     
     
     # check minimum length
     carriage_length = float(hotwire.param[0])
     panel_length = float(p.panel_span)
     dxr = float(foam.param[0])
     foam_block_xmax = panel_length + dxr
     
     if foam_block_xmax > carriage_length :
         messagebox.showwarning("In carriage_projection,  carriage length too short -> reduce x offset or panel span")
     
     #===========================================================================   
     #  adding Mid height (int-ext)) in front, tail of the foam  (root and tip)
     extralength_le = float(foam.param[3])
     extralength_te = float(foam.param[4])



     #      Root      EXT  ==============================
     xr = p.root_X[0]
     avg_y_r_le =  (p.root_Y_ext1[0] + p.root_Y_int1[0])*0.5
     avg_y_r_te =  (p.root_Y_ext1[-1] + p.root_Y_int1[-1])*0.5
     avg_z_r_le =  (p.root_Z_ext1[0] + p.root_Z_int1[0])*0.5
     avg_z_r_te =  (p.root_Z_ext1[-1] + p.root_Z_int1[-1])*0.5     
 
     yfront_foam_r = avg_y_r_le -extralength_le
     yback_foam_r  = avg_y_r_te + extralength_te*1.5 #   1.5 :to be sure to exit
     
     p.root_X.insert(0,xr)
     p.root_Y_ext1.insert(0,avg_y_r_le)    # avg height  LE
     p.root_Z_ext1.insert(0,avg_z_r_le)

     p.root_X.insert(0,xr)
     p.root_Y_ext1.insert(0,yfront_foam_r)   # avg height in front of foam LE
     p.root_Z_ext1.insert(0,avg_z_r_le)

     p.root_X.append(xr)
     p.root_Y_ext1.append(avg_y_r_te)    # avg height at TE
     p.root_Z_ext1.append(avg_z_r_te)

     p.root_X.append(xr)
     p.root_Y_ext1.append(yback_foam_r)    # avg height at the back of foam TE
     p.root_Z_ext1.append(avg_z_r_te)
     
     
     
     #      tip        EXT    ==============================
     xt = p.tip_X[0]
     avg_y_t_le =  (p.tip_Y_ext1[0]   + p.tip_Y_int1[0])*0.5
     avg_y_t_te =  (p.tip_Y_ext1[-1]  + p.tip_Y_int1[-1])*0.5
     avg_z_t_le =  (p.tip_Z_ext1[0]   + p.tip_Z_int1[0])*0.5
     avg_z_t_te =  (p.tip_Z_ext1[-1]  + p.tip_Z_int1[-1])*0.5     
        
     yfront_foam_t = avg_y_t_le -extralength_le
     yback_foam_t  = avg_y_t_te + extralength_te*1.5  #   1.5 :to be sure to exit
     
     p.tip_X.insert(0,xt)
     p.tip_Y_ext1.insert(0,avg_y_t_le)    # avg height  LE
     p.tip_Z_ext1.insert(0,avg_z_t_le)

     p.tip_X.insert(0,xt)
     p.tip_Y_ext1.insert(0,yfront_foam_t)   # avg height in front of foam LE
     p.tip_Z_ext1.insert(0,avg_z_t_le)

     p.tip_X.append(xt)
     p.tip_Y_ext1.append(avg_y_t_te)    # avg height at TE
     p.tip_Z_ext1.append(avg_z_t_te)    

     p.tip_X.append(xt)
     p.tip_Y_ext1.append(yback_foam_t)    # avg height at the back of foam TE
     p.tip_Z_ext1.append(avg_z_t_te)    

     # ==============================================

     #      Root      INT  ==============================
 
 
     p.root_Y_int1.insert(0,avg_y_r_le)    # avg height  LE
     p.root_Z_int1.insert(0,avg_z_r_le)

 
     p.root_Y_int1.insert(0,yfront_foam_r)   # avg height in front of foam LE
     p.root_Z_int1.insert(0,avg_z_r_le)


     p.root_Y_int1.append(avg_y_r_te)    # avg height at TE
     p.root_Z_int1.append(avg_z_r_te)

 
     p.root_Y_int1.append(yback_foam_r)    # avg height at the back of foam TE
     p.root_Z_int1.append(avg_z_r_te)
     
     #      tip        INT    ==============================

 
     
     p.tip_Y_int1.insert(0,avg_y_t_le)    # avg height  LE
     p.tip_Z_int1.insert(0,avg_z_t_le)

 
     p.tip_Y_int1.insert(0,yfront_foam_t)   # avg height in front of foam LE
     p.tip_Z_int1.insert(0,avg_z_t_le)
 
     p.tip_Y_int1.append(avg_y_t_te)
     p.tip_Z_int1.append(avg_z_t_te)     # avg height at TE
 
     p.tip_Y_int1.append(yback_foam_t)
     p.tip_Z_int1.append(avg_z_t_te)     # avg height at the back of foam TE




     
    #=========================================================================
    # Prepararing array for the projection on the Carriage
     p.root_Y_extc =  []
     p.root_Y_intc =  []
     p.root_Z_extc =  []
     p.root_Z_intc =  []
    

     p.tip_Y_extc =  []
     p.tip_Y_intc =  []
     p.tip_Z_extc =  []
     p.tip_Z_intc =  []
     
     # Extrados
     
     for i in range(len(p.root_Y_ext1)):
         xr = p.root_X[0]
         yr = p.root_Y_ext1[i]
         zr = p.root_Z_ext1[i]
         
         xt = p.tip_X[0]
         yt = p.tip_Y_ext1[i]
         zt = p.tip_Z_ext1[i]
         
         ay = (yt-yr)/(xt-xr)
         az = (zt-zr)/(xt-xr)
         
         p.root_Y_extc.append(yr-ay*xr)
         p.root_Z_extc.append(zr-az*xr)
         p.tip_Y_extc.append(yr+ay*(carriage_length-xr))
         p.tip_Z_extc.append(zr+az*(carriage_length-xr)) 
         
      # Intrados
     
     for i in range(len(p.root_Y_int1)):
         xr = p.root_X[0]
         yr = p.root_Y_int1[i]
         zr = p.root_Z_int1[i]
         
         xt = p.tip_X[0]
         yt = p.tip_Y_int1[i]
         zt = p.tip_Z_int1[i]
         
         ay = (yt-yr)/(xt-xr)
         az = (zt-zr)/(xt-xr)
         
         
         p.root_Y_intc.append(yr-ay*xr)
         p.root_Z_intc.append(zr-az*xr)
         p.tip_Y_intc.append(yr+ay*(carriage_length-xr))
         p.tip_Z_intc.append(zr+az*(carriage_length-xr)) 


#    Motion up to foam entry (starting with extrados)
     zr = p.root_Z_extc[0]
     p.root_Y_extc.insert(0,0.0)
     p.root_Z_extc.insert(0,zr)
 
     zt = p.tip_Z_extc[0]
     p.tip_Y_extc.insert(0,0.0)
     p.tip_Z_extc.insert(0,zt)
 
     p.root_Y_intc.insert(0,0.0)
     p.root_Z_intc.insert(0,zr)

     p.root_Y_intc.insert(0,0.0)
     p.root_Z_intc.insert(0,0.0)     
     
     
     p.tip_Y_intc.insert(0,0.0)
     p.tip_Z_intc.insert(0,zt)

     p.tip_Y_intc.insert(0,0.0)
     p.tip_Z_intc.insert(0,0.0)
     
 

#      Checking the minimum/maximum Y,Z of the wire
     zmin = 99999.9
     zmax = -99999.9
     
     ymin = 99999.9
     ymax = -99999.9
 
     ylimit = float(hotwire.param[6])    
     zlimit = float(hotwire.param[7])

     for i in range(len(p.root_Z_extc)):
         yc_int =p.root_Y_intc[i]
         zc_int =p.root_Z_intc[i]
         yc_ext =p.root_Y_extc[i]
         zc_ext =p.root_Z_extc[i]
         
         if zc_int < zmin :
             zmin = zc_int
         if zc_ext < zmin :
             zmin = zc_ext

         if zc_int > zmax :
             zmax = zc_int
         if zc_ext > zmax :
             zmax = zc_ext            
             
         if yc_int < ymin :
             ymin = yc_int
         if yc_ext < ymin :
             ymin = yc_ext

         if yc_int > ymax :
             ymax = yc_int
         if yc_ext > ymax :
             ymax = yc_ext            
    
     if zmin < 0. :
         messagebox.showwarning("In carriage_projection, Check the lowest altitude of the hotwire -> increase Zoffset of the foam")
     if zmax > zlimit :
         messagebox.showwarning("In carriage_projection, Upper vertical limit reach")

     if ymin < 0. :
         messagebox.showwarning("In carriage_projection, Check the minimum horizontal of the hotwire -> increase Yoffset of the foam")
     if ymax > ylimit :
         messagebox.showwarning("In carriage_projection, Maximum horizontal limit reach  ")



     return




def calc_coord(panel_list,foam,hotwire):

    foam_list_coord =[]
    z_ext_max = -9999.0
    z_int_min = 9999.0
    
    for ip, p in enumerate(panel_list):

        # Root
         npts, Y_Ext_Profile0 , Y_Int_Profile0, Z_Ext_Profile0, Z_Int_Profile0 = read_profile(p.root_airfoil_filename)
         p.rootnpts = npts
         
         num_points= 50
         
         Y_Ext_Profile , Y_Int_Profile, Z_Ext_Profile, Z_Int_Profile = resampling(Y_Ext_Profile0 , Y_Int_Profile0, Z_Ext_Profile0, Z_Int_Profile0,num_points)

         p.root_Y_ext0 = (Y_Ext_Profile)*float(p.rootchord) 
         p.root_Z_ext0 = (Z_Ext_Profile)*float(p.rootchord) 
         p.root_Y_int0 = (Y_Int_Profile)*float(p.rootchord)
         p.root_Z_int0 = (Z_Int_Profile)*float(p.rootchord)
         


        # tip
         npts, Y_Ext_Profile0 , Y_Int_Profile0, Z_Ext_Profile0, Z_Int_Profile0 = read_profile(p.tip_airfoil_filename)
         p.tipnpts = npts
         
         Y_Ext_Profile , Y_Int_Profile, Z_Ext_Profile, Z_Int_Profile = resampling(Y_Ext_Profile0 , Y_Int_Profile0, Z_Ext_Profile0, Z_Int_Profile0,num_points)
         
         p.tip_Y_ext0 = (Y_Ext_Profile)*float(p.tipchord)  
         p.tip_Z_ext0 = (Z_Ext_Profile)*float(p.tipchord)         
         p.tip_Y_int0 = (Y_Int_Profile)*float(p.tipchord)
         p.tip_Z_int0 = (Z_Int_Profile)*float(p.tipchord)

        
         #print(p.tip_Y_ext0)
         # print(p.tip_Z_ext0) 
         # print(p.tip_Z_int0)
         
         rotate(p)
         
         for z in p.root_Z_ext0 :
             if(z >z_ext_max ) :
                 z_ext_max = z
         for z in p.root_Z_int0 :
             if(z < z_int_min ) :
                 z_int_min = z
         for z in p.tip_Z_ext0 :
             if(z >z_ext_max ) :
                 z_ext_max = z
         for z in p.tip_Z_int0 :
             if(z < z_int_min ) :
                 z_int_min = z
                 
    amplitude_airfoil =  abs(z_ext_max) +  abs(z_int_min)         
    thicknessfoam = float(foam.param[5])
    zoffsetfoam = float(foam.param[2])
 

#   Z offset to center the core ( diedral not taken into account -> only at assemblying phase)
    dh = 0.5*( thicknessfoam - amplitude_airfoil )
    #print('Amplitude=',amplitude_airfoil)   
    #print('dh=',dh)
    if( dh <=0 ):
        print('!!!!!  Warning, thickness of foam is too small relative to the thicknesses of the airfoils')
        messagebox.showwarning("In calc_coord", "Thickness of foam is too small relative to the thicknesses of the airfoils -> increase Foam block thickness")
    zoffset_profil = zoffsetfoam + dh +  abs(z_int_min)   
    
    
    for ip, p in enumerate(panel_list):
        p.root_Z_ext0 +=    zoffset_profil
        p.root_Z_int0 +=    zoffset_profil
        p.tip_Z_ext0  +=    zoffset_profil
        p.tip_Z_int0  +=    zoffset_profil
        
  

#   y offset to center the core  
    yroot_offset = float(foam.param[1]) + float(foam.param[3])

    for ip, p in enumerate(panel_list):
        
        dy  = float(p.panel_span)*np.tan(float(p.sweepangle)*d2r)
        ytip_offset =  yroot_offset + dy
        
 
        p.root_Y_ext0  =  p.root_Y_ext0  +  yroot_offset
        p.root_Y_int0  =  p.root_Y_int0 +  yroot_offset
        p.tip_Y_ext0   =  p.tip_Y_ext0  +  ytip_offset
        p.tip_Y_int0   =  p.tip_Y_int0  +  ytip_offset
        

#   X offset  
        
    for ip, p in enumerate(panel_list):
        dxr = float(foam.param[0])
        dxt = dxr + float(p.panel_span)
        p.root_X = []
        p.tip_X = []
        for ic in p.root_Y_ext0:
            p.root_X.append(dxr)
            p.tip_X.append(dxt)


# Adding Kerf
            
    for ip, p in enumerate(panel_list):
        add_kerf(p,hotwire)

#   Airfoil Projection on carriage axis
        
    for ip, p in enumerate(panel_list):
        carriage_projection(p,hotwire, foam)
   



# Construct foam geometry for verification
    for ip, p in enumerate(panel_list):
        foam.root_coord=[]
        foam.tip_coord=[] 

        # Foam at root
        y1 = float(foam.param[1]) 
        y2 = y1 + float(p.rootchord)  + float(foam.param[3])  + float(foam.param[4]) 
        y3 = y2
        y4 = y1
        y5 = y1
        
        z1 = float(foam.param[2]) 
        z2 = z1
        z3 = z2 + float(foam.param[5]) 
        z4 = z1 + float(foam.param[5]) 
        z5 = z1
        foam.root_coord.append( [  [y1,y2,y3,y4,y5],[z1,z2,z3,z4,z5]   ] )
    
    
        # Foam at tip
        y1 = float(foam.param[1]) +  float(p.panel_span)*np.tan(float(p.sweepangle)*d2r)
        y2 = y1 + float(p.tipchord)  + float(foam.param[3])  + float(foam.param[4]) 
        y3 = y2
        y4 = y1
        y5 = y1
        
        z1 = float(foam.param[2]) 
        z2 = z1
        z3 = z2 + float(foam.param[5]) 
        z4 = z1 + float(foam.param[5])
        z5 = z1                      
        foam.tip_coord.append( [   [y1,y2,y3,y4,y5],[z1,z2,z3,z4,z5]     ] )      
                               
    
        foam_list_coord.append([foam.root_coord,foam.tip_coord ] )


    # print("#    Foam ")
    # for p in foam.param:
    #     print(p)
 
    # print("#    Machine ")
    # for p in hotwire.param:
    #     print(p)

    return foam_list_coord