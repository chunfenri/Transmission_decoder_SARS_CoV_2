def read_data(file_name):
    f = open(file_name, 'r')
    list0=f.read().split('>')
    #seperate dna sequence
    seq_name=[]
    #name of dna string
    sequence=[]
    #sequence of dna string
    for k in range(1,len(list0)):
        list00=list0[k].split('\n')
        seq_name.append(list00[0])
        sequence.append(''.join(list00[1:len(list00)]))
    return seq_name,sequence
file_name=input("filename:")
site_V=int(input("site# of G26144T(V_clade):"))-1
site_G=int(input("site# of A23403G(G_clade):"))-1
site_S=int(input("site# of T28144C(S_clade):"))-1
name,seq=read_data(file_name)
V_clade=[]
G_clade=[]
S_clade=[]
others=[]
for i in range(len(name)):
    state = 1
    if seq[i][site_V] == 'T' or seq[i][site_V] == 't' :
        V_clade.append(name[i])
        state = 0
    if seq[i][site_G] == 'G' or seq[i][site_G] == 'g' :
        G_clade.append(name[i])
        state = 0
    if seq[i][site_S] == 'C' or seq[i][site_S] == 'c' :
        S_clade.append(name[i])
        state = 0
    if state:
        others.append(name[i])

V = '\n'.join(V_clade)
G = '\n'.join(G_clade)
S = '\n'.join(S_clade)
o = '\n'.join(others)
fV = open('V_clade.txt','w')
fV.write(V)
fV.close()
fG = open('G_clade.txt','w')
fG.write(G)
fG.close()
fS = open('S_clade.txt','w')
fS.write(S)
fS.close()
fo = open('others.txt','w')
fo.write(o)
fo.close()
