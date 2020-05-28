# Autogen
This is an automatic expression generator code using Wicks Thoerem for Quantum Chemical Theories.
# Input/Output
All input are written in input.py and all latex form outtput expressions are generated in the latex.output.txt

# Testing 
Make sure you have Python installed. 
You may test the code through the file test.py which executes through Python test.py. 
It is written to go through simple examples of commutator operaration. 
Please further test the working of the code by generating all CCSD amplitude expressions by running test_ccsd.py.
 
# Unique Features
1. It is a string based program which produces final terms in the same for as in diagram derivation (eg: <ij||ab>t_{ij}^{ab}). This program makes use of Wick's Theorem. 
2. The program can handle de-excitation operators in the commutator expressions, i.e, T^\dagger T contractions can be formed (these do not appear in coupled cluster theory).
3. The program can work with commutator expressions such as [[V,T1],D1] and computes them recursively, innermost commutator first. The program has been tested for expressions upto third commutator.
The features 2 and 3 make this program well suited for applications to unitart coupled cluster (UCC) formalisms along with various coupled cluster based methods. 
