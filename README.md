# gen-abq-S9R5
In numerical analysis finite element analysis are used a lot for structural design.
Abaqus CAE is one of the most used FEA softwares due to its generality and versatility.
Abaqus CAE is written in python and it can interact with python codes.
In fact, it is possible to run python scripts within the user interface.

Some finite elements within Abaqus are hidden and they must be activated manually.
One example is given by the S95R element which is a direct extension of the classic 8 node serendipity with an extra central node.
The present script takes an input file of an Abaqus model which uses S8R5 elements and transforms it in the same model with S9R5 elements instead.

Before running the script please ensure to have a 'Job-1.inp' in the abaqus working directory.
To run the script just select 'Run script...' from the Abaqus CAE.
The script will generate a new *.inp file automatically using S9R5 elements.
