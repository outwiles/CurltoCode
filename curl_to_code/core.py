import shlex,json,re

def Aashu33(Aashu1):
 Aashu2=shlex.split(Aashu1,posix=True);Aashu3='GET';Aashu4='';Aashu5={};Aashu6=None;Aashu7=[];Aashu8=0
 while Aashu8<len(Aashu2):
  Aashu9=Aashu2[Aashu8]
  if Aashu9 in ('curl','curl.exe'):
   Aashu8+=1;continue
  if Aashu9 in ('-X','--request') and Aashu8+1<len(Aashu2): Aashu3=Aashu2[Aashu8+1].upper();Aashu8+=2;continue
  if Aashu9 in ('-H','--header') and Aashu8+1<len(Aashu2):
   Aashu10=Aashu2[Aashu8+1];Aashu8+=2
   if ':' in Aashu10:
    Aashu11,Aashu12=Aashu10.split(':',1);Aashu5[Aashu11.strip()]=Aashu12.lstrip()
   continue
  if Aashu9 in ('-d','--data','--data-raw','--data-binary','--data-ascii','--data-urlencode') and Aashu8+1<len(Aashu2):
   Aashu6=Aashu2[Aashu8+1];Aashu8+=2
   if Aashu3=='GET': Aashu3='POST'
   continue
  if Aashu9 in ('-b','--cookie') and Aashu8+1<len(Aashu2): Aashu7.append(Aashu2[Aashu8+1]);Aashu8+=2;continue
  if Aashu9 in ('-F','--form') and Aashu8+1<len(Aashu2):
   Aashu7.append(Aashu2[Aashu8+1]);Aashu8+=2
   if Aashu3=='GET': Aashu3='POST'
   continue
  if Aashu9 in ('-u','--user') and Aashu8+1<len(Aashu2): Aashu10=Aashu2[Aashu8+1];Aashu8+=2;Aashu13=Aashu10.split(':',1);Aashu5['Authorization']='Basic '+__import__('base64').b64encode(Aashu10.encode()).decode();continue
  if Aashu9 in ('-G','--get'): Aashu3='GET';Aashu8+=1;continue
  if Aashu9 in ('--url','--url-query') and Aashu8+1<len(Aashu2): Aashu4=Aashu2[Aashu8+1];Aashu8+=2;continue
  if Aashu9.startswith('-'):
   Aashu8+=1;continue
  if not Aashu4 and re.match(r'^(https?|wss?)://',Aashu9): Aashu4=Aashu9
  Aashu8+=1
 if not Aashu4:
  raise ValueError('No URL found in cURL command')
 if Aashu7 and 'Cookie' not in Aashu5 and all('=' in Aashu14 for Aashu14 in Aashu7): Aashu5['Cookie']='; '.join(Aashu7)
 if Aashu6 is not None and Aashu3 in ('GET','HEAD') and '?' not in Aashu4 and Aashu6.startswith(('?', '&')): Aashu4+=Aashu6
 return {'method':Aashu3,'url':Aashu4,'headers':Aashu5,'body':Aashu6,'forms':Aashu7}

def Aashu32(Aashu1): return json.dumps(Aashu1,ensure_ascii=False,indent=2)
def Aashu31(Aashu1): return json.dumps(Aashu1,ensure_ascii=False)
def Aashu30(Aashu1): return json.dumps(Aashu1.get('headers',{}),ensure_ascii=False)
def Aashu29(Aashu1): return repr(Aashu1.get('url',''))
def Aashu28(Aashu1): return repr(Aashu1.get('body')) if Aashu1.get('body') is not None else 'None'
def Aashu27(Aashu1): return Aashu1.get('method','GET')
def Aashu26(Aashu1): return Aashu1.get('headers',{})
def Aashu25(Aashu1): return Aashu1.get('forms',[])
def Aashu24(Aashu1): return Aashu1.get('body') is not None
