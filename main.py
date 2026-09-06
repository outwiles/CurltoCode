import os
from cfonts import render
from curl_to_code.core import Aashu33 as Aashu2
from curl_to_code.generators import Aashu33 as Aashu3,Aashu34 as Aashu4

banner=render(' Aashu',font='block',colors=['red','white'],align='center',background='black')
Aashu14={1:'py',2:'py',3:'py',4:'go',5:'rb',6:'php',7:'php',8:'cs',9:'java',10:'js',11:'js',12:'js',13:'ts',14:'py',15:'exs',16:'js',17:'java',18:'cs',19:'cpp',20:'c',21:'rs',22:'kt',23:'swift',24:'dart',25:'R',26:'lua',27:'pl',28:'ps1',29:'sh',30:'sh',31:'txt',32:'json'}
Aashu15=os.path.join(os.path.dirname(os.path.abspath(__file__)),'output')

def Aashu16(Aashu1):
 os.makedirs(Aashu15,exist_ok=True)
 Aashu5=[]
 for Aashu2,Aashu3 in Aashu1.items():
  Aashu4=Aashu3[0]
  Aashu6=Aashu4.replace(" ","_").replace(".","_").replace("::","_")
  Aashu7=os.path.join(Aashu15,f'{Aashu2:02d}_{Aashu6}.{Aashu14[Aashu2]}')
  with open(Aashu7,'w',encoding='utf-8') as Aashu8:
   Aashu8.write(Aashu3)
  Aashu5.append(Aashu7)
 return Aashu5

def Aashu9():
 print('\x1b[1;39m━'*63)
 print(banner)
 print('\x1b[1;39m━'*63)
 print()
 print("Enter your curl url")
 print("|-> ",end="",flush=True)
 Aashu5=input().strip()
 if not Aashu5:
  print("\nNo cURL provided.")
  return
 try:
  Aashu6=Aashu2(Aashu5)
  Aashu7=Aashu4(Aashu6)
  Aashu8=Aashu16(Aashu7)
  print(f"\nGenerated {len(Aashu7)} formats.")
  print(f"Saved to: {Aashu15}\n")
  for Aashu10 in Aashu8:
   print(f"✓ {os.path.basename(Aashu10)}")
 except Exception as Aashu11:
  print(f"\nError: {Aashu11}")

if __name__=='__main__':
 Aashu9()
