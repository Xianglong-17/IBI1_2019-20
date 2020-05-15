import pandas as pd
import xml.dom.minidom
# Import neccessary libraries.
DOMTree=xml.dom.minidom.parse('go_obo.xml')
indexes=DOMTree.documentElement
terms=indexes.getElementsByTagName('term')
defs=[]
is_a=[]
dic={}
# Set up neccessary elements.
for term in terms:
    definitions=term.getElementsByTagName('def')
    IDs=term.getElementsByTagName('id')[0]
    is_as=term.getElementsByTagName('is_a')
    # Search the location of different words.
    for x in is_as:
        is_a.append(x.childNodes[0].data)
    dic[IDs.childNodes[0].data]=is_a[:]
    is_a.clear()
    for definition in definitions:
        defstr=definition.getElementsByTagName('defstr')[0]
        defs.append(defstr.childNodes[0].data)
    # After locating the words, get the information needed.
a=[]
for x in range(len(defs)):
    if 'autophagosome' in defs[x]:
        a.append(x)
        # Search the word "autophagosome".
ids=[]
names=[]
d=[]
for i in a:
    IDs=terms.item(i).getElementsByTagName('id')[0]
    ids.append(IDs.childNodes[0].data)
    NAMEs=terms.item(i).getElementsByTagName('name')[0]
    names.append(NAMEs.childNodes[0].data)
    d.append(defs[i])

childnode = []
for i in ids:
    m = []
    count = 0
    for j in dic:
        if i in dic[j]:
            count += 1
            m.append (j)
    n = m[:]
    inc = count
    while inc != 0 :
        m = []
        inc = 0
        for k in n:
            for j in dic:
                if k in dic[j]:
                    count += 1
                    inc += 1
                    m.append (j)
        n = m[:]
    childnode.append (count)
    # Check and count the childnode.
xfile=pd.DataFrame({'id':ids,'name':names,'definition':d,'childnodes':childnode})
xfile.to_excel('Autophagosome.xlsx',
               sheet_name='Autophagosome',
               columns=['id','name','definition','childnodes'])
# Produce the output.