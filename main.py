import os,sys,time
from cfonts import render
from curl_to_code.core import Aashu33 as Aashu2
from curl_to_code.generators import Aashu33 as Aashu3,Aashu34 as Aashu4

banner=render(' Aashu',font='block',colors=['red','white'],align='center',background='black')
Aashu13="Curl to Souce by Aashu"
Aashu14={1:'py',2:'py',3:'py',4:'go',5:'rb',6:'php',7:'php',8:'cs',9:'java',10:'js',11:'js',12:'js',13:'ts',14:'py',15:'exs',16:'js',17:'java',18:'cs',19:'cpp',20:'c',21:'rs',22:'kt',23:'swift',24:'dart',25:'R',26:'lua',27:'pl',28:'ps1',29:'sh',30:'sh',31:'txt',32:'json'}
Aashu15=os.path.join(os.path.dirname(os.path.abspath(__file__)),'output')

def Aashu16(Aashu1):
 os.makedirs(Aashu15,exist_ok=True)
 Aashu5=[]
 for Aashu2,(Aashu3,Aashu4) in Aashu1.items():
  Aashu6=Aashu3.replace(" ","_").replace(".","_").replace("::","_")
  Aashu7=os.path.join(Aashu15,f'{Aashu2:02d}_{Aashu6}.{Aashu14[Aashu2]}')
  with open(Aashu7,'w',encoding='utf-8') as Aashu8:Aashu8.write(Aashu4)
  Aashu5.append(Aashu7)
 return Aashu5

def Aashu8():
 print('\x1b[1;39m━'*63)
 print(banner)
 print('\x1b[1;39m━'*63)
 for Aashu5 in range(len(Aashu13)+1):
  print("\033[1;32m\033[1;97m"+Aashu13[:Aashu5].center(63)+"\033[0m",end="\r")
  sys.stdout.flush()
  time.sleep(0.05)
 print()
 print('\x1b[1;39m━'*63)

def Aashu9():
 Aashu8()
 print("\nPaste your cURL command.")
 print("Press Enter on an empty line when finished.\n")
 Aashu5=[]
 while True:
  Aashu6=sys.stdin.readline()
  if not Aashu6:
   break
  if not Aashu6.strip() and Aashu5:
   break
  Aashu5.append(Aashu6.rstrip("\n"))
 Aashu7="\n".join(Aashu5).strip()
 if not Aashu7:
  print("\nNo cURL command provided.")
  return
 try:
  Aashu10=Aashu2(Aashu7)
  Aashu11=Aashu4(Aashu10)
  Aashu12=Aashu16(Aashu11)
  print(f"\nGenerated {len(Aashu11)} formats.")
  print(f"Saved to:\n{Aashu15}\n")
  for Aashu13 in Aashu12:
   print(f"✓ {os.path.basename(Aashu13)}")
 except Exception as Aashu14:
  print(f"\nError: {Aashu14}")

if __name__=='__main__':
 Aashu9()
