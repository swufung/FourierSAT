FourierSAT is a versatile SAT/MaxSAT solver for hybrid Boolean constraints. 

The types of constraints include CNF (-or), XOR, cardinality constraints, and NAE (not all equal).

Paper: FourierSAT: A Fourier Expansion-Based Algebraic Framework for Solving Hybrid Boolean Constraints
https://arxiv.org/abs/1912.01032
(AAAI-2020)

If you have questions or thoughts regarding the tool or this work, please contact zhiwei@rice.edu.

----------------------------------------------------------------------------------------------------------------------
Required environment
-----------------------------------------
 python with Scipy

Basic usage
---------------
python usage:

	python FourierSAT/FourierSAT.py [DIMACS filepath] --options

*Optional parameters:

--timelimit: the time limit (in seconds) for this run. Default: 60

--tolerance: the number of clauses that a solution can violate. Default: 0

--cpus: the number of CPU cores available (the more, the better). Default: 8

--verbose: set it to 1 to output more information

For example, in FourierSAT_Github_AIJ/, run:

	python FourierSAT.py sample.cnf --timelimit 10

Input: Extended DIMACS Format
-------------------------
FourierSAT accepts an extended DIMACS format that can handle CNF, XOR, cardinality constraints, and Not-all-equal clauses. MaxSAT instances (.wcnf) and cardinality constraints encoded in pseudo-Boolean format (.opb) are also accepted.

CNF: "[literals] 0"

	eg: clause x_1 or \neg x_2: "1 -2 0"
     
XOR: "x [literals] 0"

     eg: clause x_1 xor \neg x_2: "x 1 -2 0"
     
Cardinality constraints: 
      
    eg: "+1 x_1 +1 x_2 +1 x_4 + 1 x_5 >= 2 ;" (note the ";")
      
Not all equal: "n [literals] 0"

      eg: NAE(x_1,x_2,\neg x_3): "n 1 2 -3 0"

Output
-------
	-s "solved"/"not-solved in timelimit seconds"+[minimum number of violated clauses]   
	-v [solutions]/[the assignment with minimum number of violated clauses found]    
	-o [the cost of the best solution found so far (the number of violated constraints)] (Only for MaxSAT mode)
