'''
Project: gen-abq-S9R5
Creator: Nicholas Fantuzzi
Contact: @sniis84
Version: 1.0
Date: 5-Jul-2015

To test just place 'Job-1.inp' in the Abaqus working directory and
select 'Run Script...' from the menu. A new file will be created as 'Job-1-finale.inp'.
Running that file using Abaqus/CAE or command line will result in using S9R5 elements

'''

#!/usr/bin/python

#in_file = tuple(open("Job-1.inp","r"))
in_file = tuple(open("C:/Temp_Abaqus/Job-1.inp","r"))

#out_file = open('Job-1-out_file.inp','w')
out_file = open('C:/Temp_Abaqus/Job-1-finale.inp','w')

# find the node and element number -------------------
rigaInizioNodi = 0
rigaFineNodi = 0
rigaInizioElem = 0
rigaFineElem = 0
for i in range(len(in_file)):
    if '*Node' in in_file[i]:
        rigaInizioNodi = i + 1
    if '*Element' in in_file[i]:
    	rigaFineNodi = i - 1
    	rigaInizioElem = i + 1
    if '*Nset' in in_file[i]:
    	rigaFineElem = i - 1
    	break

# number of nodes and elements
noNodi = rigaFineNodi - rigaInizioNodi + 1
noElem = rigaFineElem - rigaInizioElem + 1

# set the initial number for the extra nodes
nodoZero = '100'
for i in range(len(str(noNodi))):
	nodoZero = nodoZero + '0'
nodoZero = int(nodoZero)
# -------------------------------------------------------------

nodi = [[0 for x in range(noNodi)] for x in range(4)] 

for i in range(len(in_file)):
# save nodal coordinates for later computation
	if '*Node' in in_file[i]:
		for j in range(noNodi):
			coord = in_file[i+1+j].replace("\r","").replace("\n","").replace(" ","").split(",")
			for k in range(4):
				nodi[k][j] = float(coord[k])

# -------------------------------------------------------------
# computation of the central node for the S9R5 element
	if '*Element' in in_file[i]:
		for j in range(noElem):
			Xcoord = 0.
			Ycoord = 0.
			Zcoord = 0.
			nodiElemento = in_file[i+1+j].replace("\r","").replace("\n","").replace(" ","").split(",")
			for k in range(8): # ciclo sui nodi dell'elemento
				Xcoord = Xcoord + nodi[1][int(nodiElemento[k+1])-1]
				Ycoord = Ycoord + nodi[2][int(nodiElemento[k+1])-1]
				Zcoord = Zcoord + nodi[3][int(nodiElemento[k+1])-1]
#
			Xcoord = Xcoord / 8.
			Ycoord = Ycoord / 8.
			Zcoord = Zcoord / 8.
			nuovoNodo = nodoZero + j + 1
			
			out_file.write("%i,\t %f,\t %f,\t %f\r\n" %(nuovoNodo, Xcoord, Ycoord, Zcoord) )
			out_file.write("\n")
		out_file.write("*Element, type=S9R5\r\n")
	else:
		if (i >= rigaInizioElem and i <= rigaFineElem):
			nuovoNodo = nodoZero + i - rigaInizioElem + 1
			out_file.write(in_file[i].replace("\r","").replace("\n","")+",\t%i\r\n" %(nuovoNodo))
		else:
			out_file.write(in_file[i])

out_file.close()

# -------------------------------------------------------------
