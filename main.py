import os,sys,time
from cfonts import render
from curl_to_code.core import Aashu33 as Aashu2
from curl_to_code.generators import Aashu33 as Aashu3,Aashu34 as Aashu4
Aashu1=render
banner=render(' Aashu',font='block',colors=['red','white'],align='center',background='black')
Aashu13="Curl to Souce by Aashu"
def Aashu8():
 print('\x1b[1;39m━'*63);print(banner);print('\x1b[1;39m━'*63)
def Aashu7():
 while True:
  os.system('cls' if os.name=='nt' else 'clear');Aashu8();print()
  for Aashu5 in range(32,0,-1): print(f"{Aashu5:>2}. {Aashu3[Aashu5][0]}")
  print(' 0. Exit');Aashu6=input('\nSelect: ').strip()
  if Aashu6=='0': return
  if not Aashu6.isdigit() or int(Aashu6) not in Aashu3: continue
  Aashu5=int(Aashu6);Aashu9=input('\nPaste cURL: ').strip()
  try:Aashu10=Aashu2(Aashu9);Aashu11=Aashu4(Aashu10)[Aashu5];print('\n'+Aashu11);input('\nPress Enter...')
  except Exception as Aashu12: print(f'\nError: {Aashu12}');input('\nPress Enter...')
if __name__=='__main__': Aashu7()
