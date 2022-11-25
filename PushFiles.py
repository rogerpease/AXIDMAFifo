#!/usr/bin/env python3 
import os 

MYPYNQBOARD="xilinx@10.0.0.151"


PROJECTDIRNAME="DMAFifo"

os.system("ssh "+MYPYNQBOARD+" mkdir /home/xilinx/"+PROJECTDIRNAME)

os.system("scp ./AXIFifo2.gen/sources_1/bd/design_2/hw_handoff/design_2.hwh "+MYPYNQBOARD+":/home/xilinx/"+PROJECTDIRNAME+"/"+PROJECTDIRNAME+".hwh")
os.system("scp ./AXIFifo2.runs/impl_1/design_2_wrapper.bit "+MYPYNQBOARD+":/home/xilinx/"+PROJECTDIRNAME+"/"+PROJECTDIRNAME+".bit")
os.system("scp AXIDMAFifo.py  "+MYPYNQBOARD+":/home/xilinx/"+PROJECTDIRNAME+"/")
