Small Documentation 

Here is how it should work : 
----------------------------------------------------------------
    Hello, this is Spin Free GWT expression generator. 
    Currently it is designed to only work with 2 normal ordered strings. So Ignore the menu 
-------------------------------------------------------

            MENU 
1 - Single string EWT generator
2 - Two normal ordered strings EWT generator
3 - Commutator type two string EWT generator
2
Enter Operator 1 : Input the upper indices of E E(a,b,c)_(e,f,g) 
(i,j..-holes; u,v...-active; a,b...-excited;)
Example : uv
Operator string: u
input the lower indices of E E(a,b,c)_(e,f,g) 
(i,j..-holes; u,v...-active; a,b...-excited; )
Example : uv
Operator string: v
Enter Operator 2 : Input the upper indices of E E(a,b,c)_(e,f,g) 
(i,j..-holes; u,v...-active; a,b...-excited;)
Example : uv
Operator string: w
input the lower indices of E E(a,b,c)_(e,f,g) 
(i,j..-holes; u,v...-active; a,b...-excited;)
Example : uv
Operator string: x
[[g, e], [l]] [[1, 0.5], [1, 1.0]]

The last line is the output, but for a detailed expression, open tec.txt generated. 

Entered Information : 
1.	Enter 2 as it is only doing a contraction of 2 normal ordered operators only. 
2.	Enter the upper string (daggered part ) of the first operator. Eg uvw
3.	Enter lower string (undaggered part) of the first operators Eg xyz
4.	Repeat for second operator
5.	Repeat 
Indeces : 
U v w x y z o t : active 
A b c d e f g h : particles 
I j k l m n : holes

