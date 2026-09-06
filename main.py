import os,sys,time
from cfonts import render
from curl_to_code.core import Aashu33 as Aashu2
from curl_to_code.generators import Aashu33 as Aashu3,Aashu34 as Aashu4
Aashu1=render
banner=render(' Aashu',font='block',colors=['red','white'],align='center',background='black')
Aashu13="Curl to Souce by Aashu"
Aashu14={1:'py',2:'py',3:'py',4:'go',5:'rb',6:'php',7:'php',8:'cs',9:'java',10:'js',11:'js',12:'js',13:'ts',14:'py',15:'exs',16:'js',17:'java',18:'cs',19:'cpp',20:'c',21:'rs',22:'kt',23:'swift',24:'dart',25:'R',26:'lua',27:'pl',28:'ps1',29:'sh',30:'sh',31:'txt',32:'json'}
Aashu15=os.path.join(os.path.dirname(os.path.abspath(__file__)),'output')
def Aashu16(Aashu1):
 os.makedirs(Aashu15,exist_ok=True)
 for Aashu2,(Aashu3,Aashu4) in Aashu1.items():
  with open(os.path.join(Aashu15,f'{Aashu2:02d}_{Aashu3.replace(" ","_").replace(".","_").replace("::","_")}.{Aashu14[Aashu2]}'),'w',encoding='utf-8') as Aashu5:Aashu5.write(Aashu4)
def Aashu8():
 print('\x1b[1;39m━'*63);print(banner);print('\x1b[1;39m━'*63)
 for Aashu5 in range(len(Aashu13)+1):
  print("\033[1;32m\033[1;97m"+Aashu13[:Aashu5].center(63)+"\033[0m",end="\r");sys.stdout.flush();time.sleep(0.05)
 print();print('\x1b[1;39m━'*63)
def Aashu7():
 while True:
  os.system('cls' if os.name=='nt' else 'clear');Aashu8();print()
  for Aashu5 in range(32,0,-1): print(f"{Aashu5:>2}. {Aashu3[Aashu5][0]}")
  print(' 0. Exit');Aashu6=input('\nSelect: ').strip()
  if Aashu6=='0': return
  if not Aashu6.isdigit() or int(Aashu6) not in Aashu3: continue
  Aashu5=int(Aashu6);Aashu9=input('\nPaste cURL: ').strip()
  try:
   Aashu10=Aashu2(Aashu9);Aashu11=Aashu4(Aashu10);Aashu16(Aashu11);print('\n'+Aashu11[Aashu5]);print(f'\nSaved all 32 outputs to: {Aashu15}');input('\nPress Enter...')
  except Exception as Aashu12: print(f'\nError: {Aashu12}');input('\nPress Enter...')
if __name__=='__main__': Aashu7()
