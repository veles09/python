import xml.dom.minidom as minidom

#-*- coding:utf-8 -*-
 
import os,xml.dom.minidom
 
from prim1 import author,publ
 
 
 
class library:
 
def __init__(self,datafile=’prim2.xml’,output=’prim2out.xml’):
 
self.__datafile=datafile
self.__output=output
self.__books=[]
self.__authors=[]
self.__publs=[]

def getdatafile(self):return self.__datafile
def appendauthor(self,value):self.__authors.append(value)
def appendpubl(self,value):self.__publs.append(value)
def readdata(self):
 
dom=xml.dom.minidom.parse(self.__datafile)
 
dom.normalize()
 
for node in dom.childNodes[0].childNodes:
 
if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName==’author’):
 
self.appendauthor(author())
 
for t in node.attributes.items():
 
if t[0]=="code":self.__authors[-1].setcode(int(t[1]))
 
if t[0]=="name":self.__authors[-1].setname(t[1])
 
if t[0]=="surname":self.__authors[-1].setsurname(t[1])
 
if t[0]=="secname":self.__authors[-1].setsecname(t[1])
 
if t[0]=="shortname":self.__authors[-1].setshortname(t[1])
 
if t[0]=="shortsecname":self.__authors[-1].setshortsecname(t[1])
 
if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName==’publ’):
 
self.appendpubl(publ())
 
for t in node.attributes.items():
 
if t[0]=="code":self.__publs[-1].setcode(int(t[1]))
 
if t[0]=="name":self.__publs[-1].setname(t[1])
 
if t[0]=="shortname":self.__publs[-1].setshortname(t[1])
 
if (node.nodeType==node.ELEMENT_NODE)and(node.nodeName==’book’):
 
self.appendbook(book())
 
for t in node.attributes.items():
 
if t[0]=="code":self.__books[-1].setcode(int(t[1]))
 
if t[0]=="name":self.__books[-1].setname(t[1])
 
if t[0]=="year":self.__books[-1].setyear(int(t[1]))
 
 
if t[0]=="pages":self.__books[-1].setpages(int(t[1]))
 
if t[0]=="publ":
 
l=[p for p in lib.__publs if p.getcode()==int(t[1])]
 
if l:self.__books[-1].setpubl(l[0])
 
for n in node.childNodes:
 
if (n.nodeType==n.ELEMENT_NODE)and(n.nodeName==’author’):
 
for t in n.attributes.items():
 
if t[0]=="code":
 
l=[a for a in lib.__authors if a.getcode()==int(t[1])]
 
if l:self.__books[-1].appendauthor(l[0])
 
def writedata(self):
 
dom=xml.dom.minidom.Document()
 
root=dom.createElement("library")
 
dom.appendChild(root)
 
for a in self.__authors:
 
aut=dom.createElement("author")
 
aut.setAttribute(’code’,str(a.getcode()))
 
aut.setAttribute(’surname’,a.getsurname())
 
aut.setAttribute(’name’,a.getname())
 
aut.setAttribute(’secname’,a.getsecname())
 
aut.setAttribute(’shortname’,a.getshortname())
 
aut.setAttribute(’shortsecname’,a.getshortsecname())
 
root.appendChild(aut)
 
for p in self.__publs:
 
pub=dom.createElement("publ")
 
pub.setAttribute(’code’,str(p.getcode()))
 
pub.setAttribute(’name’,p.getname())
 
pub.setAttribute(’shortname’,p.getshortname())
 
root.appendChild(pub)
 
for b in self.__books:
 
bk=dom.createElement("book")
 
bk.setAttribute(’code’,str(b.getcode()))
 
bk.setAttribute(’name’,b.getname())
 
bk.setAttribute(’year’,str(b.getyear()))
 
bk.setAttribute(’pages’,str(b.getpages()))
 
bk.setAttribute(’publ’,str(b.getpublcode()))
 
 
for a in b.getauthorcodelist():
 
aut=dom.createElement("author")
 
aut.setAttribute(’code’,str(a))
 
bk.appendChild(aut)
 
root.appendChild(bk)
 
f = open(self.__output,"w")
 
f.write(dom.toprettyxml(encoding=’utf-8’))
 
def getbibliostrs(self):return [b.getbibliostr() for b in self.__books]
lib=library()
 
lib.readdata()
 
for s in lib.getbibliostrs():
 
print s
 
lib.writedata()