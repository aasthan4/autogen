# Autogen
This is an automatic expression generator program using wick's thoerem for quantum chemical theories. It produces expressions for electronic structure theories in the same form as derived by diagrams. This program can be used for unitary coupled cluster formalism.
# Input/Output
All input are written in input.py and all latex form output expressions are generated in the latex_output.txt

# Install
Have Python 3.0 installed->write an input file and execute input.py file. 

# Testing
Test the code through the file test.py which executes by "Python test.py"
It is written to go through simple examples of commutator operaration. 
Please further test the working of the code by generating all CCSD amplitude expressions by running test_ccsd.py as "Python test_ccsd.py". Read the result at latex_output.txt.

# Definitions
X1-project the terms on a single excitation (\psi_i^a) on the left. For use in deriving amplitude terms.

X2-project the terms on a double excitation (\psi_{ij}^{ab}) on the left. For use in deriving amplitude terms.

T1-single excitation operator: t_i^a a^{\dagger}_a a_i

T2-double excitation operator: t_{ij}^{ab} a^{\dagger}_a a^{\dagger}_b a_j a_i
D1-single deexcitation operator: d_i^a a^{\dagger}_i a_a)

D2-double deexcitation operator: d_{ij}^{ab} a^{\dagger}_i a^{\dagger}_j a_b a_a

V2-fluctuation operator: 1/4 <pq||rs>a^{\dagger}_p a^{\dagger}_q a_s a_r

F1-fock operator: f_{pq} a^{\dagger}_p a_q

# Important Functions
Inside main_tools. To import, use: "from main_tools import comm as comm"... 

1. comm('V2','T1',1,0)- single commputator on operator V and T1 with a prefactor of 1.0.
2. prod('X1',comm('V2','T1',1.0))- product function takes simple product of the operators inside. This example is equivant to the operator product- X1VT1-X1T1V.

Inside library. To import, use: "from library import print_terms"...
1. print_terms(terms,'filename')- prints all terms in latex format in the file "latex_output.txt"
2. terms=full_con(terms)- selects the fully contracted terms only and leaved out all other terms in the list of terms provided. Useful to print only the fully contracted terms.
 
# Unique Features
1. String based program which produces terms in the same form as in the diagram derivation (eg: \sum_{ijab}<ij||ab>t_{ij}^{ab}). The algorithm makes use of Wick's Theorem. 
2. The program can handle de-excitation operators in the commutator expressions, i.e, T^\dagger T contractions can be formed (these do not appear in coupled cluster theory).
3. The program can work with commutator expressions such as [[V,T1],D1] and computes them recursively, innermost commutator first. The program has been tested for expressions upto third commutator.
The features 2 and 3 make this program well suited for applications to unitary coupled cluster (UCC) formalism along with various coupled cluster based methods. 
