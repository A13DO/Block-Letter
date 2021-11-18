# block letter ACII


a = """  AAA      
 AAAAA     
AA   AA    
AAAAAAA    
AA   AA"""
b = """BBBBB   
BB   B  
BBBBBB  
BB   BB 
BBBBBB""" 
c = """CCCCC  
CC    C 
CC      
CC    C 
 CCCCC """ 
d = """DDDDD   
DD  DD  
DD   DD 
DD   DD 
DDDDDD  """ 
e = """EEEEEEE 
EE      
EEEEE   
EE      
EEEEEEE  """ 
f = """FFFFFFF 
FF      
FFFF    
FF      
FF""" 
g = """  GGGG  
 GG  GG 
GG      
GG   GG 
 GGGGGG """ 
h = """HH   HH 
HH   HH 
HHHHHHH 
HH   HH 
HH   HH""" 
i = """IIIII   
 III    
 III    
 III    
IIIII""" 
j = """    JJJ 
    JJJ 
    JJJ 
JJ  JJJ 
 JJJJJ""" 
k = """KK  KK  
KK KK   
KKKK    
KK KK   
KK  KK""" 
l = """LL      
LL      
LL      
LL      
LLLLLLL""" 
m = """MM    MM  
MMM  MMM  
MM MM MM  
MM    MM  
MM    MM""" 
n = """NN   NN   
NNN  NN   
NN N NN   
NN  NNN   
NN   NN"""
o = """ OOOOO    
OO   OO   
OO   OO   
OO   OO   
 OOOO0 """ 
p = """PPPPPP    
PP   PP   
PPPPPP    
PP        
PP""" 
q = """ QQQQQ    
QQ   QQ   
QQ   QQ   
QQ  QQ    
 QQQQ Q""" 
r = """RRRRRR    
RR   RR   
RRRRRR    
RR  RR    
RR   RR""" 
s = """ SSSSS    
SS        
 SSSSS    
     SS   
 SSSSS""" 
t = """TTTTTTT   
  TTT     
  TTT     
  TTT     
  TTT  """ 
u = """UU   UU   
UU   UU   
UU   UU   
UU   UU   
 UUUUU """ 
v = """VV     VV 
VV     VV 
 VV   VV  
  VV VV   
   VVV  """ 
w = """WW      WW 
WW      WW 
WW   W  WW 
 WW WWW WW 
  WW   WW  """ 
x = """XX    XX  
 XX  XX   
  XXXX    
 XX  XX   
XX    XX""" 
y = """YY   YY 
YY   YY 
 YYYYY  
  YYY   
  YYY  """ 
z = """ZZZZZ   
   ZZ   
  ZZ    
 ZZ     
ZZZZZ""" 

ver_letters = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]

letter = str(input("Your letter: ")).strip()

# A chr = 97

letter_Num = ord(letter)
ver_Number = 97 - letter_Num
print(ver_letters[ver_Number])









