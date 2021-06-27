from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import os
import math
from  datetime import datetime


from calcgc import *

global model_name
global npanel,npanel0
global main_frame
global panel_list

global wing_canvas, wing_canvas_width, wing_canvas_height

global d2r, r2d



#================================================================
class FoamBlock():
    """ Define Foam parameter :
        - x shift
        - z shift ...   """

    def __init__(self):
        """Init FoamBlock"""
 
    def callbackefbxo(self):
#       """get the foam xoffset"""
        self.var = self.ehfbxo.get().strip()
        self.param[0] = self.var
        print(self.param)
        return True

    def callbackefbyo(self):
#       """get the foam xoffset"""
        self.var = self.ehfbyo.get().strip()
        self.param[1] = self.var
        print(self.param)
        return True
    def callbackefbzo(self):
#       """get the foam xoffset"""
        self.var = self.ehfbzo.get().strip()
        self.param[2] = self.var
        print(self.param)
        return True
  
    def callbackefbovle(self):
#       """get the foam xoffset"""
        self.var = self.ehfbovle.get().strip()
        self.param[3] = self.var
        print(self.param)
        return True
    def callbackefbovte(self):
#       """get the foam xoffset"""
        self.var = self.ehfbovte.get().strip()
        self.param[4] = self.var
        print(self.param)
        return True
    
    def callbackefbh(self):
#       """get the foam xoffset"""
        self.var = self.ehfbh.get().strip()
        self.param[5] = self.var
        print(self.param)
        return True

    def construct(self,foam_param):
        
        self.param=foam_param
        
        irow = 0
        lbl0 = Label(tab3, text= 'Foam block position')
        lbl0.grid(column=0, row=irow)
        irow = irow +1
        lbl0 = Label(tab3, text= 'X1 corner offset (mm)')
        lbl0.grid(column=0, row=irow)       
        self.var = StringVar() 
        self.ehfbxo = Entry(tab3,width=8,textvariable=self.var, validate="focusout", validatecommand=self.callbackefbxo)
        self.ehfbxo.grid(column=1, row=irow)
        self.ehfbxo.insert(0,self.param[0])  


        irow = irow +1
        lbl0 = Label(tab3, text= 'Y1 corner offset (mm)')
        lbl0.grid(column=0, row=irow)       
        self.var = StringVar() 
        self.ehfbyo = Entry(tab3,width=8,textvariable=self.var, validate="focusout", validatecommand=self.callbackefbyo)
        self.ehfbyo.grid(column=1, row=irow)
        self.ehfbyo.insert(0,self.param[1])  


        irow = irow +1
        lbl0 = Label(tab3, text= 'Z1 corner offset (mm)')
        lbl0.grid(column=0, row=irow)       
        self.var = StringVar() 
        self.ehfbzo = Entry(tab3,width=8,textvariable=self.var, validate="focusout", validatecommand=self.callbackefbzo)
        self.ehfbzo.grid(column=1, row=irow)
        self.ehfbzo.insert(0,self.param[2])  


        irow = irow +3
        lbl0 = Label(tab3, text= 'Foam block extra length and size')
        lbl0.grid(column=0, row=irow)   
        irow = irow +1
        lbl0 = Label(tab3, text= 'At leading edge (mm)')
        lbl0.grid(column=0, row=irow)  
        self.var = StringVar() 
        self.ehfbovle = Entry(tab3,width=8,textvariable=self.var, validate="focusout", validatecommand=self.callbackefbovle)
        self.ehfbovle.grid(column=1, row=irow)
        self.ehfbovle.insert(0,self.param[3])          
       
        irow = irow +1
        lbl0 = Label(tab3, text= 'At trailing edge (mm)')
        lbl0.grid(column=0, row=irow)  
        self.var = StringVar() 
        self.ehfbovte = Entry(tab3,width=8,textvariable=self.var, validate="focusout", validatecommand=self.callbackefbovte)
        self.ehfbovte.grid(column=1, row=irow)
        self.ehfbovte.insert(0,self.param[4])          

        irow = irow +1
        lbl0 = Label(tab3, text= 'Thickness (mm)')
        lbl0.grid(column=0, row=irow)  
        self.var = StringVar() 
        self.ehfbh = Entry(tab3,width=8,textvariable=self.var, validate="focusout", validatecommand=self.callbackefbh)
        self.ehfbh.grid(column=1, row=irow)
        self.ehfbh.insert(0,self.param[5])   



def FoamBlock_default_set_up():
    """ default machine  set up:
        - hotwire length
        - speed ...   """
    foam_param=[]
    foam_param.append("10.0")  # x offset (mm)   [0]
    foam_param.append("0.0")   # y offset (mm)   [1] 
    foam_param.append("50.0")  # z offset (mm)   [2] 
    foam_param.append("10.0")  # overlength leading edge (mm)    [3]     
    foam_param.append("10.0")  # overlength trailing edge (mm)   [4]        
    foam_param.append("80.0")  # foam block thickness (mm)       [5]       
    return foam_param










#================================================================

class Machine():
    """ Define hotwire machine :
        - hotwire length
        - speed ...   """

    def __init__(self):
        """Init hotwire"""

    def callbackehwl(self):
#       """get the hotwire length"""
        self.var = self.ehwl.get().strip()
        self.param[0] = self.var
        print(self.param)
        return True
        # if self.var.isdigit():
        #     self.param[0] = self.var
        #     print(self.param)
        #     return True
        # else:
        #      messagebox.showerror("Error"," Not a valid entry")
        #      return False

    def callbackehwcs(self):
#       """get the hotwire length"""
        self.var = self.ehwcs.get().strip()
        self.param[1] = self.var
        print(self.param)
        return True


    def callbackehwx1(self):
#       """get the hotwire length"""
        self.var = self.ehwx1.get().strip()
        self.param[2] = self.var
        print(self.param)
        return True

    def callbackehwy1(self):
#       """get the hotwire length"""
        self.var = self.ehwy1.get().strip()
        self.param[3] = self.var
        print(self.param)
        return True


    def callbackehwx2(self):
#       """get the hotwire length"""
        self.var = self.ehwx2.get().strip()
        self.param[4] = self.var
        print(self.param)
        return True
    
    def callbackehwy2(self):
#       """get the hotwire length"""
        self.var = self.ehwy2.get().strip()
        self.param[5] = self.var
        print(self.param)
        return True


    def callbackehwxl(self):
#       """get the hotwire length"""
        self.var = self.ehwxl.get().strip()
        self.param[6] = self.var
        print(self.param)
        return True

    def callbackehwyl(self):
#       """get the hotwire length"""
        self.var = self.ehwyl.get().strip()
        self.param[7] = self.var
        print(self.param)
        return True

    def callbackehwk0(self):
#       """get the kerf """
        self.var = self.ehwk0.get().strip()
        self.param[8] = self.var
        print(self.param)
        return True

    def construct(self,hotwire_param):
        
        self.param=hotwire_param
        

        irow = 0
        lbl0 = Label(tab2, text= 'Hotwire length (mm):')
        lbl0.grid(column=0, row=irow)
        self.var = StringVar() 
        #self.ehwl = Entry(tab2,width=8)     
        self.ehwl = Entry(tab2,width=8,textvariable=self.var, validate="focusout", validatecommand=self.callbackehwl)
        self.ehwl.grid(column=1, row=irow)
        self.ehwl.insert(0,self.param[0])  

        irow = irow+1
        lbl1 = Label(tab2, text= 'Cut speed (mm/min):')
        lbl1.grid(column=0, row=irow)
        self.var = StringVar() 
        #self.ehwl = Entry(tab2,width=8)     
        self.ehwcs = Entry(tab2,width=8,textvariable=self.var, validate="focusout", validatecommand=self.callbackehwcs)
        self.ehwcs.grid(column=1, row=irow)
        self.ehwcs.insert(0,self.param[1])  
  
        irow = irow+1
        lbl1 = Label(tab2, text= 'Axis names')
        lbl1.grid(column=0, row=irow)
        irow = irow+1
        lbl1 = Label(tab2, text= 'X1', justify='right')
        lbl1.grid(column=0, row=irow)
        self.var = StringVar() 
        self.ehwx1 = Entry(tab2,width=4,textvariable=self.var, validate="focusout", validatecommand=self.callbackehwx1)
        self.ehwx1.grid(column=1, row=irow)
        self.ehwx1.insert(0,self.param[2])  
   
        lbl1 = Label(tab2, text= 'Y1', justify='right')
        lbl1.grid(column=2, row=irow)
        self.var = StringVar() 
        self.ehwy1 = Entry(tab2,width=4,textvariable=self.var, validate="focusout", validatecommand=self.callbackehwy1)
        self.ehwy1.grid(column=3, row=irow)
        self.ehwy1.insert(0,self.param[3])  
        
        
        irow = irow+1
        lbl1 = Label(tab2, text= 'X2', justify='right')
        lbl1.grid(column=0, row=irow)
        self.var = StringVar() 
        self.ehwx2 = Entry(tab2,width=4,textvariable=self.var, validate="focusout", validatecommand=self.callbackehwx2)
        self.ehwx2.grid(column=1, row=irow)
        self.ehwx2.insert(0,self.param[4])  
   
        lbl1 = Label(tab2, text= 'Y2', justify='right')
        lbl1.grid(column=2, row=irow)
        self.var = StringVar() 
        self.ehwy2 = Entry(tab2,width=4,textvariable=self.var, validate="focusout", validatecommand=self.callbackehwy2)
        self.ehwy2.grid(column=3, row=irow)
        self.ehwy2.insert(0,self.param[5])  
        
        irow = irow+3
        lbl1 = Label(tab2, text= 'Axis limit', justify='right')
        lbl1.grid(column=0, row=irow)
        irow = irow+1
        lbl1 = Label(tab2, text= 'X (mm)', justify='right')
        lbl1.grid(column=1, row=irow)
        self.var = StringVar() 
        self.ehwxl = Entry(tab2,width=6,textvariable=self.var, validate="focusout", validatecommand=self.callbackehwxl)
        self.ehwxl.grid(column=2, row=irow)
        self.ehwxl.insert(0,self.param[6])  
        irow = irow+1
        lbl1 = Label(tab2, text= 'Y(mm)', justify='right')
        lbl1.grid(column=1, row=irow)
        self.var = StringVar() 
        self.ehwyl = Entry(tab2,width=6,textvariable=self.var, validate="focusout", validatecommand=self.callbackehwyl)
        self.ehwyl.grid(column=2, row=irow)
        self.ehwyl.insert(0,self.param[7])  


        irow = irow+1
        lbl0 = Label(tab2, text= 'Kerf(Travel speed) (mm):')
        lbl0.grid(column=0, row=irow)
        self.var = StringVar() 
        #self.ehwl = Entry(tab2,width=8)     
        self.ehwk0 = Entry(tab2,width=8,textvariable=self.var, validate="focusout", validatecommand=self.callbackehwk0)
        self.ehwk0.grid(column=1, row=irow)
        self.ehwk0.insert(0,self.param[8])  




def hotwire_default_set_up():
    """ default machine  set up:
        - hotwire length
        - speed ...   """
    hotwire_param=[]
    hotwire_param.append("500.0")  # hw length (mm)   [0]
    hotwire_param.append("300.0")  # hw travel speed (mm)   [1] 
    hotwire_param.append("X")      #  X1              [2] 
    hotwire_param.append("Y")      #  Y1              [3]     
    hotwire_param.append("U")      #  X2              [4] 
    hotwire_param.append("Z")      #  Y2              [5]         
    hotwire_param.append("500.0")  #  Xlimit          [6] 
    hotwire_param.append("250.0")  #  Ylimit          [7]             
    hotwire_param.append("0.7")    #  Kerf            [8]           
    
    return hotwire_param




#================================================================
    #                Wing Panel class 
#================================================================
class Panel :
    
    """ Panel will be define by :
        - panel number
        - root Profile_Name   """
    
    global main_frame
        
    def __init__(self,n):
        """Init panel"""

        self.Panel_Number = n
        #print("--------------------------------------")
        #print('Panel Nb', self.Panel_Number+1)

        self.rootchord = ''
        self.tipchord =  ''
    


    def callbackws(self,event):
#       """get the panel span"""
        self.panel_span = self.ews.get()

        
    def callbackr(self,event):
#       """get the root chord length"""
        self.rootchord=self.erc.get()


    def callbackt(self,event):
#         """get the tip chord length,  set the root chord length for the nex panel"""
        self.tipchord=self.etc.get()       
        print(' Panel :',self.Panel_Number,'/',npanel,', Root',  self.rootchord,', Tip:',self.etc.get() )       
  
        if npanel > 1 :
            if ((self.Panel_Number+1) < npanel ) :
                p = panel_list[self.Panel_Number +1]
                p.rootchord =self.tipchord
                p.erc.delete(0,END)
                p.erc.insert(0, p.rootchord)

    def select_file_afr(self):
         self.root_airfoil_filename = filedialog.askopenfilename(initialdir=".", title="Select an aifoil file", filetypes=( ("dat files", "*.dat") , ("txt files", "*.txt")  ))     
         f = self.root_airfoil_filename
         dirl= f.split("/")
         self.lblafr = Label(self.frame, text= dirl[-1], bg="white")
         self.lblafr.grid(column=1, row=2)
         
    def select_file_aft(self):
         self.tip_airfoil_filename = filedialog.askopenfilename(initialdir=".", title="Select an aifoil file", filetypes=( ("dat files", "*.dat") , ("txt files", "*.txt")  ))     
         f = self.tip_airfoil_filename
         dirl= f.split("/")
         self.lblaft = Label(self.frame, text= dirl[-1], bg="white")
         self.lblaft.grid(column=1, row=4)
         if npanel > 1 :
              if ((self.Panel_Number+1) < npanel ) :
                  
                  p = panel_list[self.Panel_Number +1]
                  p.root_airfoil_filename =self.tip_airfoil_filename
                  f = p.root_airfoil_filename
                  dirl= f.split("/")
                  p.lblafr= Label(p.frame, text= dirl[-1], bg="white")
                  p.lblafr.grid(column=1, row=2)



    def callbacks(self,event):
#         """get the sweep angle for the leading edge (>0 , backward )"""
        self.sweepangle=self.esr.get()
        print(' Panel :',self.Panel_Number,'/',npanel, 
              ', Root',  self.rootchord,
              ', Tip:',self.etc.get(),
              'Sweep',self.sweepangle  ) 
        s = float(self.sweepangle)

    def callbackwr(self,event):
#         """get the washout angle for the root (>0 , trailing edge up )"""
        self.root_washout=self.ewr.get()
        print(' Panel :',self.Panel_Number,'/',npanel, 
              'Wash r',self.root_washout              ) 


    def callbackwt(self,event):
#         """get the washout angle for the tip (>0 , trailing edge up )"""
        self.tip_washout=self.ewt.get()
        print(' Panel :',self.Panel_Number,'/',npanel, 
              'Wash t ',self.tip_washout )
        if npanel > 1 :
            if ((self.Panel_Number+1) < npanel ) :
                p = panel_list[self.Panel_Number +1]
                p.root_washout =self.tip_washout
                p.ewr.delete(0,END)
                p.ewr.insert(0,p.root_washout)

    def callbackwd(self,event):
#         """get the diedre angle for the panel (>0 , up )"""
        self.diedre=self.ed.get()
        print(' Panel :',self.Panel_Number,'/',npanel, 
              ', diedre:', self.diedre )
        if(self.Panel_Number == 0) :
            for ipanel, p in enumerate(panel_list):
                if ipanel >0 :
                    p.diedre = self.diedre
                    p.ed.delete(0,END)
                    p.ed.insert(0,p.diedre)

    def callbackhxr(self,event):
#         """get the position of the root hinge line x/c  /LE (%)"""
        self.root_hingex=self.ehxr.get()
        print(' Panel :',self.Panel_Number,'/',npanel, 
              'Root Hinge x',self.root_hingex              )
        
    def callbackhxt(self,event):
#         """get the position of the tip hinge line x/c  /LE (%)"""
        self.tip_hingex=self.ehxt.get()
        print(' Panel :',self.Panel_Number,'/',npanel, 
              'Tip Hinge x',self.tip_hingex              ) 


    def construct(self):
        global panel_list
        panel_name = 'Panel '+str(self.Panel_Number+1)
        self.frame = LabelFrame(main_frame, text=panel_name, width=300, height=300) 
        self.frame.grid(row=0,column=2*self.Panel_Number+1)  
        
        
        

      #  Panel span
        irow = 0
        #self.var = StringVar()
        lbl0 = Label(self.frame, text= 'Panel span (mm):')
        lbl0.grid(column=0, row=irow)
        self.ews = Entry(self.frame,width=8)
        #self.ews = Entry(self.frame,width=8,textvariable=self.var, validate="focusout", validatecommand=self.callbackws)
        self.ews.grid(column=1, row=irow)
        self.ews.bind('<Return>',self.callbackws) 

       #  Root chord
        irow +=1
        lbl1 = Label(self.frame, text= 'Root chord (mm):')
        lbl1.grid(column=0, row=irow)
  
        #self.varrc = StringVar()
        #self.erc = Entry(self.frame,width=8,textvariable=self.varrc, validate="focusout", validatecommand=self.callbackr)
        self.erc = Entry(self.frame,width=8)
        self.erc.grid(column=1, row=irow)
        if (self.Panel_Number == 0 ) :
            self.erc.delete(0,END)
            self.erc.insert(0,self.rootchord)
        #self.erc.bind('<KeyPress>',self.callback)
        self.erc.bind('<Return>',self.callbackr) 

       #  Root airfoil
        irow=irow+1
        self.sfbr = Button(self.frame,text='Select Root Airfoil',command=self.select_file_afr)
        self.sfbr.grid(row=irow,column=0)
        self.root_airfoil_filename = ""
 



       #  Tip  chord
        irow=irow+1
        lbl3 = Label(self.frame, text= 'Tip chord (mm):')
        lbl3.grid(column=0, row=irow)
        self.etc = Entry(self.frame,width=8)
        self.etc.grid(column=1, row=irow)
        self.etc.bind('<Return>',self.callbackt) 
        

       #  Tip airfoil
        irow=irow+1
        self.sfbt = Button(self.frame,text='Select Tip Airfoil',command=self.select_file_aft)
        self.sfbt.grid(row=irow,column=0)
        self.tip_airfoil_filename = ""

        # Sweep angle
        irow=irow+1
        lbl4 = Label(self.frame, text= 'Leading edge sweep angle (deg):')           
        lbl4.grid(column=0, row=irow)           
        self.esr = Entry(self.frame,width=8)
        self.esr.grid(column=1, row=irow)
        self.esr.bind('<Return>',self.callbacks)

       # Diedre angle
        irow=irow+1
        lbl7 = Label(self.frame, text= 'Diedre angle (deg):', pady = 5)           
        lbl7.grid(column=0, row=irow)           
        self.ed = Entry(self.frame,width=8)
        self.ed.grid(column=1, row=irow)
        self.ed.insert(0,"")
        self.ed.bind('<Return>',self.callbackwd)
         
       # Wash out angle
        irow=irow+1
        lbl5 = Label(self.frame, text= 'Root washout angle (deg):')           
        lbl5.grid(column=0, row=irow)           
        self.ewr = Entry(self.frame,width=8)
        self.ewr.grid(column=1, row=irow)
        self.ewr.insert(0,"")
        self.ewr.bind('<Return>',self.callbackwr)
        irow=irow+1
        lbl6 = Label(self.frame, text= 'Tip washout angle (deg):')           
        lbl6.grid(column=0, row=irow)        
        self.ewt = Entry(self.frame,width=8)
        self.ewt.grid(column=1, row=irow)
        self.ewt.insert(0,"")
        self.ewt.bind('<Return>',self.callbackwt)

      #  Root Hingeline x
        irow=irow+1
        lbl8 = Label(self.frame, text= 'Root Hinge X/c/LE (%):')           
        lbl8.grid(column=0, row=irow)           
        self.ehxr = Entry(self.frame,width=8)
        self.ehxr.grid(column=1, row=irow)
        self.ehxr.insert(0,"")
        self.ehxr.bind('<Return>',self.callbackhxr)

      #  Tip Hingeline x
        irow=irow+1
        lbl9 = Label(self.frame, text= 'Tip Hinge X/c/LE (%):')           
        lbl9.grid(column=0, row=irow)           
        self.ehxt = Entry(self.frame,width=8)
        self.ehxt.grid(column=1, row=irow)
        self.ehxt.insert(0,"")
        self.ehxt.bind('<Return>',self.callbackhxt)

#================================================================


def test_e1(inStr,acttyp):
    if acttyp == '1': #insert
        if not inStr.isdigit():
            return False
    return True

#================================================================
#            Fonction to set all wing default data
#================================================================
def load_default_wing():
    global model_name
    we0.delete(0,END)
    we0.insert(0,model_name)
    
    for ip, p in enumerate(panel_list):
        p.ews.delete(0,END)
        p.panel_span= "200.0"
        p.ews.insert(0, p.panel_span)

        p.erc.delete(0,END)
        p.rootchord = "150.0"
        p.erc.insert(0, p.rootchord)

        p.etc.delete(0,END)
        p.tipchord= "150.0"
        p.etc.insert(0, p.tipchord)
        
        
        p.root_airfoil_filename = "./dat/CLARKY.dat"
        f = p.root_airfoil_filename
        dirl= f.split("/")
        
        p.lblafr = Label(p.frame, text= dirl[-1], bg="white")
        p.lblafr.grid(column=1, row=2)
        
                
        p.tip_airfoil_filename = "./dat/CLARKY.dat"
        f = p.tip_airfoil_filename
        dirl= f.split("/")
        p.lblaft = Label(p.frame, text= dirl[-1], bg="white")
        p.lblaft.grid(column=1, row=4)


        p.esr.delete(0,END)
        p.sweepangle= "0.0"
        p.esr.insert(0, p.sweepangle) 

        p.ed.delete(0,END)
        p.diedre= "2.0"
        p.ed.insert(0, p.diedre) 


        p.ewr.delete(0,END)
        p.root_washout= "0.0"
        p.ewr.insert(0, p.root_washout) 
 
        p.ewt.delete(0,END)
        p.tip_washout= "0.0"
        p.ewt.insert(0, p.tip_washout)  
        

        p.ehxr.delete(0,END)
        p.root_hingex= "75"
        p.ehxr.insert(0, p.root_hingex)
        
        p.ehxt.delete(0,END)
        p.tip_hingex= "75"
        p.ehxt.insert(0, p.tip_hingex)        
 

#================================================================
#            Fonction to set all wing open data from model
#================================================================
def load_open_model_wing():
    global panel_list
    global model_name
    

    we0.delete(0,END)
    we0.insert(0,model_name)
    
    for ip, p in enumerate(panel_list):
        p.ews.delete(0,END)
        p.ews.insert(0, p.panel_span)

        p.erc.delete(0,END)
        p.erc.insert(0, p.rootchord)

        p.etc.delete(0,END)
        p.etc.insert(0, p.tipchord)
        
        f = p.root_airfoil_filename
        dirl= f.split("/")
        p.lblafr = Label(p.frame, text= dirl[-1], bg="white")
        p.lblafr.grid(column=1, row=2)
        
        f = p.tip_airfoil_filename
        dirl= f.split("/")
        p.lblaft = Label(p.frame, text= dirl[-1], bg="white")
        p.lblaft.grid(column=1, row=4)
        
        
        
        p.esr.delete(0,END)
        p.esr.insert(0, p.sweepangle) 

        p.ed.delete(0,END)
        p.ed.insert(0, p.diedre) 


        p.ewr.delete(0,END)
        p.ewr.insert(0, p.root_washout) 
 
        p.ewt.delete(0,END)
        p.ewt.insert(0, p.tip_washout)  
        

        p.ehxr.delete(0,END)
        p.ehxr.insert(0, p.root_hingex)
        
        p.ehxt.delete(0,END)
        p.ehxt.insert(0, p.tip_hingex)        





#================================================================

def fct_wing_validate():
    global npanel
    global npanel0
    global panel_list
    global main_frame
    global model_name
    
    model_name = we0.get()
    
    npanel0  = npanel
    npanel = int(we1.get())
 
    main_frame.destroy()
    main_frame = LabelFrame(tab1, text='Wing platform Description ', width=500, height=200)
    main_frame.grid(row=3,column=3)  


    frame_list = []
    panel_list =[]
    for ipanel in range(npanel):
        p = Panel(ipanel)
        panel_list.append(p)
        p.construct()

    load_default_wing()

#================================================================
#            Fonction to read all wing data
#================================================================
def fct_read_wing():
    global model_name
    status = True
    fault_list = []
    model_name = we0.get()
    if(model_name == ""):
        status = False
        model_name = "default_model_name"
        fault_list.append(model_name)
 
    
    npanel = int(we1.get())
    if(npanel == 0):
        status = False
        fault_list.append("npanel")


    for ip, p in enumerate(panel_list):
        
        fault_list.append("-----PANEL "+str(ip+1)+"-----")
        
        p.panel_span = p.ews.get()
        if p.panel_span == "" :
            status = False
            fault_list.append("panel_span")
            
        p.rootchord = p.erc.get()
        if p.rootchord == "" :
            status = False
            fault_list.append("rootchord")
            
        p.tipchord = p.etc.get()
        if p.tipchord == "" :
            status = False 
            fault_list.append("tipchord")

        if p.root_airfoil_filename  == "" :
            status = False 
            fault_list.append("root_airfoil_filename")

        if p.tip_airfoil_filename  == "" :
            status = False 
            fault_list.append("tip_airfoil_filename")

        p.sweepangle = p.esr.get()
        if p.sweepangle == "" :
            status = False
            fault_list.append("sweepangle")

        p.root_washout = p.ewr.get()
        if p.root_washout == "" :
            status = False
            fault_list.append("root_washout")

        p.tip_washout = p.ewt.get()
        if p.tip_washout == "" :
            status = False
            fault_list.append("tip_washout")

        p.diedre = p.ed.get()
        if p.diedre == "" :
            status = False
            fault_list.append("diedre")
        
        p.root_hingex=p.ehxr.get()
        if p.root_hingex == "" :
            status = False
            fault_list.append("root_hingex")

        p.tip_hingex=p.ehxt.get()
        if p.tip_hingex == "" :
            status = False
            fault_list.append("tip_hingex")


    return status, fault_list








#=====================================================
#   Fonction Wing drawing
#=====================================================


def fct_draw_wing():
    print('drawing...')
    # set the scale:
    list_color = [ "black", "blue", "green", "red","purple","yellow"]
    fct_clear()
    status, fault_list = fct_read_wing()
    
    if status == False :
        line = ""
        for fault in fault_list:
            line+=str(fault)+'\n'
        messagebox.showerror("Error", "Missing data: \n"+line)
    else:
       
        xmargin = 10
        ymargin = 10
        
        xdeb = xmargin
        ydeb =  ymargin
        
        wing_span = 0.0
        ymin = 10000.0
        ymax = -10000.0
        for p in panel_list:
            sinalfa = math.sin( float(p.sweepangle)*d2r)
            wing_span += float(p.panel_span)
          
            p1y = ydeb
            p4y = p1y +  float(p.rootchord)
            if p1y < ymin :
                ymin = p1y
            if p4y > ymax :
                ymax = p4y
                
            p2y = p1y + float(p.panel_span)*sinalfa 
            p3y = p2y + float(p.tipchord)
            if p2y < ymin :
                ymin = p2y
            if p3y > ymax :
                ymax = p3y
    
        scaley = wing_canvas_height / (ymax-ymin +2*ymargin ) 
        scalex = wing_canvas_width / (wing_span +2*xmargin )  

        scale =min(scalex, scaley)
        
   


        xdeb = xmargin
        ydeb =  ymargin

        for ip, p in enumerate(panel_list): 
            p1x = xdeb
            p1y = ydeb
            
            sinalfa = math.sin( float(p.sweepangle)*d2r)
            p2x = p1x + float(p.panel_span)*scale
            p2y = p1y + float(p.panel_span)*sinalfa*scale
            
            p3x = p2x
            p3y = p2y + float(p.tipchord)*scale
            
            p4x = p1x 
            p4y = p1y +  float(p.rootchord)*scale
            
            p5x = p1x
            p5y = p1y
            
            # Panel
            wing_canvas.create_line(  (p1x, p1y), (p2x, p2y) , (p3x, p3y), (p4x, p4y), (p5x, p5y),
                              fill=list_color[ip], width=1, smooth=False)    
        
            wing_canvas.create_text (0.5*(p1x+p2x), 0.5*(p1y+p4y), text= "Panel nb "+str(ip+1),
                              fill= list_color[ip], font= ("courier", 8, "bold italic"),
                              anchor="center", justify= "center")            

#           Hinge line
            p6x = p1x
            p6y = p1y + float(p.rootchord)*scale*float(p.root_hingex)/100.0

            p7x = p2x
            p7y = p2y + float(p.tipchord)*scale*float(p.tip_hingex)/100.0
            
            wing_canvas.create_line(  (p6x, p6y), (p7x, p7y) , dash=(1,1),
                              fill=list_color[ip], width=1, smooth=False)    



            xdeb = p2x
            ydeb = p2y
        





        # wing_canvas.create_rectangle ((100, 100), (600, 600),  
        #                          fill="cyan", outline="blue", width=5)
    
        # wing_canvas.create_oval ((100, 100), (600, 600), 
        #                     fill="pink", outline="red", width=3)
    
        # wing_canvas.create_line ((100, 100), (500, 200),(600, 600), 
        #                     fill="gray", width=3, dash=(8,4))
    
        # wing_canvas.create_line ((100, 100), (500, 200), (600, 600), 
        #                     fill="black", width=5, smooth=True,
        #                     arrow="last", arrowshape=(30,45,15))
     
        # wing_canvas.create_text (600, 100, text= "Hello\nEverybody",
        #                     fill= "black", font= ("courier", 30, "bold italic"),
        #                     anchor="center", justify= "center")

def fct_clear():
    wing_canvas.delete("all")


#=====================================================
#   Fonction For menu Bar
#=====================================================
def new_model():
    #print('new_model')
    fct_wing_validate()
    
def open_model():
    #print('open_model')
    global panel_list
    global main_frame
    global model_name
    
    open_model_filename = filedialog.askopenfilename(initialdir=".", title="Select a model file", filetypes=( ("mod files", "*.mod") , ("txt files", "*.txt")  )  ) 

    main_frame.destroy()
    main_frame = LabelFrame(tab1, text='Wing platform Description ', width=500, height=200)
    main_frame.grid(row=3,column=3)  

    with  open(open_model_filename) as file:
        line=file.readline()
        model_name = file.readline().strip('\n')
        line=file.readline()
        npanel= int(file.readline())
        
        frame_list = []
        panel_list =[]
        for ipanel in range(npanel):
            
            line=file.readline()
            print(line)
            p = Panel(ipanel)
            panel_list.append(p)
            p.construct()
            
            p.panel_span = file.readline()
            p.rootchord  = file.readline()
            p.tipchord   = file.readline()
            p.root_airfoil_filename= file.readline().strip('\n')
            p.tip_airfoil_filename= file.readline().strip('\n')
            p.sweepangle= file.readline()
            p.diedre= file.readline()
            p.root_washout= file.readline()
            p.tip_washout = file.readline()
            p.root_hingex= file.readline()
            p.tip_hingex = file.readline()
        
        # read hotwire description
        l = file.readline()
        for ip, p in enumerate(hotwire.param):
            l = file.readline()
            hotwire.param[ip] =l.strip('\n')
       
        hotwire.construct(hotwire.param)
        
        
        # read foam description
        l = file.readline()
        for ip, p in enumerate(foam.param):
            l = file.readline()
            foam.param[ip] =l.strip('\n')
            
        foam.construct(foam.param)
        
    file.close()
    load_open_model_wing()



def save_model():
    global model_name
    #print('save_model')
    save_model_file = asksaveasfile(initialfile = 'Untitled.mod',
                              defaultextension=".mod",filetypes=[("All Files","*.*")])

    if save_model_file is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    save_model_file.write("# Created the ")
    save_model_file.write(dt_string)
    save_model_file.write('\n')
    save_model_file.write(model_name + '\n')
    save_model_file.write("#    Wing Description   \n")
    
    save_model_file.write(str(npanel)+'\n')
    
    for ip, p in enumerate(panel_list):
        save_model_file.write("#    Panel nb "+str(ip+1)+'\n')
        save_model_file.write(p.panel_span.strip('\n')+'\n')
        save_model_file.write(p.rootchord.strip('\n')+'\n')
        save_model_file.write(p.tipchord.strip('\n')+'\n')
        save_model_file.write(p.root_airfoil_filename.strip('\n')+'\n')
        save_model_file.write(p.tip_airfoil_filename.strip('\n')+'\n')
        save_model_file.write(p.sweepangle.strip('\n')+'\n')
        save_model_file.write(p.diedre.strip('\n')+'\n') 
        save_model_file.write( p.root_washout.strip('\n') +'\n')
        save_model_file.write(p.tip_washout.strip('\n') +'\n')
        save_model_file.write(p.root_hingex.strip('\n')+'\n') 
        save_model_file.write(p.tip_hingex.strip('\n') +'\n')

   
    save_model_file.write("#    Hotwire Description   \n")
    for ip, p in enumerate(hotwire.param):
        save_model_file.write(p +'\n')
        
    
        
    save_model_file.write("#    Foam block Description   \n")
    for ip, p in enumerate(foam.param):
        save_model_file.write(p +'\n')
        
    
        
      
    
    
    
    save_model_file.close()







#=====================================================
#=====================================================
#=====================================================

if __name__ == '__main__':
    
    d2r = math.pi /180.0
    r2d = 1.0/d2r
    
    root = Tk()
    root.title("The  Phoenix   App")
    root.iconbitmap('./phoenix.ico')
    root.geometry("1256x800")
    
    # for the wing platform drawing
    wing_canvas_width = 800
    wing_canvas_height = 300

    
    
    
    menuBar = Menu(root)
    
    menuFile = Menu(menuBar, tearoff=0)
    menuFile.add_command(label="New", command=new_model)
    menuFile.add_command(label="Open", command=open_model)
    menuFile.add_command(label="Save",command=save_model)
    menuFile.add_separator()
    menuFile.add_command(label="Exit", command=root.quit)
    
    
    menuBar.add_cascade( label="File", menu=menuFile)
    root.config(menu = menuBar)  
    
    
    
    tab_control = ttk.Notebook(root)
    
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab3 = ttk.Frame(tab_control)
    tab4 = ttk.Frame(tab_control)
    
    tab_control.add(tab1, text='Wing Definition')
    tab_control.add(tab2, text='Machine set up')
    tab_control.add(tab3, text='Foam Definition')
    tab_control.add(tab4, text='Gcode export')    
    
    
    

    
    #================================================================
    #       Tab wing
    #================================================================
    #
    irow = 0    
    lbl0 = Label(tab1, text= 'Model name:', anchor='e',width = 20)
    lbl0.grid(column=0, row=irow)
    we0 = Entry(tab1, width=20,justify="right")
    we0.grid(column=1, row=irow)
    we0.insert(0, 'default_model.mod')  
    
   
    npanel = 1
    npanel0 = npanel
    irow +=1
    lbl1 = Label(tab1, text= 'Number of panel for half wing:',anchor='e' )
    lbl1.grid(column=0, row=irow )
    
  
    we1 = Entry(tab1, width=20,validate="key",justify="right")
    we1.grid(column=1, row=irow)
    we1.insert(0, str(npanel))
    we1['validatecommand'] = (we1.register(test_e1),'%P','%d')
    
    irow += 1
    wbutton_validate = Button(tab1, text='Validate', command= fct_wing_validate, fg="black", bg="white", padx = 35)
    wbutton_validate.grid(row=irow, column=1)
    
    irow += 1
    main_frame = LabelFrame(tab1, text='Wing platform Description ', width=500, height=200)
    main_frame.grid(row=irow,column=3)  
 
    
    
    
    irow += 1
    wbutton_draw = Button(tab1, text='Check wing Platform', command= fct_draw_wing, fg="black", bg="white")
    wbutton_draw.grid(row=irow, column=0,pady=5)
   
    #wbutton_clear = Button(tab1, text='Clear drawing', command= fct_clear, fg="black", bg="white")
    #wbutton_clear.grid(row=irow, column=1,pady=5)
    
    irow += 1
    wing_canvas= Canvas(tab1, width=wing_canvas_width, height= wing_canvas_height, bg="white")
    wing_canvas.grid(row=irow,column=3, pady = 10) 
    
    
     
    #================================================================
    #       Tab Machine set up 
    #================================================================
    #
    hotwire = Machine()
    
    hotwire_param = hotwire_default_set_up()
    
    hotwire.construct(hotwire_param)
    
    
    
    
    
    
    
    
    
    #================================================================
    #       Tab Foam
    #================================================================
    #
    foam = FoamBlock()
    foam_parameter = FoamBlock_default_set_up()
    foam.construct(foam_parameter)
    
    
    #================================================================
    #      Tab   Export gcode
    #================================================================
    #    
    
    irow  = 0
    wbutton_validate = Button(tab4, text='Export left Panels', command= lambda:export_gcl(model_name,panel_list,foam,hotwire), fg="black", bg="white", padx = 35)
    wbutton_validate.grid(row=irow, column=1)

    irow +=1
    wbutton_validate = Button(tab4, text='Export Symetric Panels', command= lambda:export_gcs(model_name,panel_list,foam,hotwire), fg="black", bg="white", padx = 35)
    wbutton_validate.grid(row=irow, column=1)

    irow +=1
    wbutton_validate = Button(tab4, text='Export left and Symetric Panels', command= lambda:export_gcls(model_name,panel_list,foam,hotwire), fg="black", bg="white", padx = 35)
    wbutton_validate.grid(row=irow, column=1)
    
    #================================================================
    #
    tab_control.pack(expand=1, fill='both')
    
    
    
    
    root.mainloop()