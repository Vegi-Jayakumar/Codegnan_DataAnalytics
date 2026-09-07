#Day - 4

'''
Operators:
-> Operators are the symbols that are used to perform operations on variables and values.
-> There are different types of operators in Python:
    1. Arithmetic Operators : Used to perform arithmetic operations like addition, subtraction, multiplication, division, etc.
        Eg: +, -, *, /, %, **, //
        + : Addition : Adding two or more values. It concatinates data types like strings, lists, tuples, etc.
            Eg: num_1 = 10
                num_2 = 20
                print(num_1 + num_2)  # Output: 30
        - : Subtraction : Subtracting one value from another
            Eg: num_1 = 10
                num_2 = 20
                print(num_1 - num_2)  # Output: -10
        * : Multiplication : Multiplying two or more values
            Eg: num_1 = 10
                num_2 = 20
                print(num_1 * num_2)  # Output: 200
        / : Division : Dividing one value by another
            Eg: num_1 = 10
                num_2 = 20
                print(num_1 / num_2)  # Output: 0.5
        % : Modulo : Returning the remainder of a division
            Eg: num_1 = 10
                num_2 = 20
                print(num_1 % num_2)  # Output: 10
        ** : Exponentiation : Raising a value to the power of another
            Eg: num_1 = 10
                num_2 = 20
                print(num_1 ** num_2)  # Output: 100000000000000000000
        // : Floor Division : Dividing one value by another and returning the integer part
            Eg: num_1 = 10
                num_2 = 20
                print(num_1 // num_2)  # Output: 0

    2. Comparison Operators : Used to compare two values.
        Eg: ==, !=, >, <, >=, <=
        == : Equal : Checks if two values are equal
            Eg: num_1 = 10
                num_2 = 20
                print(num_1 == num_2)  # Output: False
        != : Not Equal : Checks if two values are not equal
            Eg: num_1 = 10
                num_2 = 20
                print(num_1 != num_2)  # Output: True
        > : Greater Than : Checks if the first value is greater than the second value
            Eg: num_1 = 10
                num_2 = 20
                print(num_1 > num_2)  # Output: False
        < : Less Than : Checks if the first value is less than the second value
            Eg: num_1 = 10
                num_2 = 20
                print(num_1 < num_2)  # Output: True
        >= : Greater Than or Equal To : Checks if the first value is greater than or equal to the second value
            Eg: num_1 = 10
                num_2 = 20
                print(num_1 >= num_2)  # Output: False
        <= : Less Than or Equal To : Checks if the first value is less than or equal to the second value
            Eg: num_1 = 10
                num_2 = 20
                print(num_1 <= num_2)  # Output: True

    3. Logical Operators : Used to perform logical operations.
        Eg: and, or, not
        and : Returns True if both operands are true
            Eg: num_1 = 10
                num_2 = 20
                print(num_1 != num_2 and num_2 >= num_1)  # Output: True
        or : Returns True if at least one of the operands is true
            Eg: num_1 = 10
                num_2 = 20
                print(num_1 == num_2 or num_2 >= num_1)  # Output: True
        not : Returns the opposite of the operand
            Eg: num_1 = 10
                print(not (num_1 == 10))  # Output: False

    4. Assignment Operators : Used to assign values to variables.
        Eg: =, +=, -=, *=, /=, %=, **=, //=    
        = : Assignment : Assigns a value to a variable.
            Eg: a = 10
                print(a)  # Output: 10
        += : Addition Assignment : Adds a value to a variable and assigns the result to the variable.
            Eg: a = 10
                a += 2
                print(a)  # Output: 12
        -= : Subtraction Assignment : Subtracts a value from a variable and assigns the result to the variable.
            Eg: a = 10
                a -= 2
                print(a)  # Output: 8
        *= : Multiplication Assignment : Multiplies a value by a variable and assigns the result to the variable.
            Eg: a = 10
                a *= 2
                print(a)  # Output: 20
        /= : Division Assignment : Divides a value by a variable and assigns the result to the variable.
            Eg: a = 10
                a /= 2
                print(a)  # Output: 5.0
        %= : Modulo Assignment : Divides a value by a variable and assigns the remainder to the variable.
            Eg: a = 10
                a %= 2
                print(a)  # Output: 0
        **= : Exponentiation Assignment : Raises a value to the power of a variable and assigns the result to the variable.
            Eg: a = 10
                a **= 2
                print(a)  # Output: 100
        //= : Floor Division Assignment : Divides a value by a variable and assigns the integer part to the variable.
            Eg: a = 10
                a //= 2
                print(a)  # Output: 5
                
    5. Membership Operators : Used to check if a value is present in a sequence.
        Eg: in, not in
        in : Returns True if the value is present in the sequence.
            Eg: a = 10
                print(a in [1, 2, 3, 4, 5])  # Output: False
        not in : Returns True if the value is not present in the sequence.
            Eg: a = 10
                print(a not in [1, 2, 3, 4, 5])  # Output: True

    6. Identity Operators : Used to check if two variables refer to the same object.
        Eg: is, is not
        is : Returns True if the two variables refer to the same object.
            Eg: a = 10
                b = 10
                print(a is b)  # Output: False
                a = [1, 2, 3]
                b = [1, 2, 3]
                print(a is b)  # Output: False
        is not : Returns True if the two variables do not refer to the same object.
            Eg: a = 10
                b = 20
                print(a is not b)  # Output: True
                a = [1, 2, 3]
                b = [1, 2, 3]
                print(a is not b)  # Output: True

Concatenation:
-> Concatenation is the process of joining two or more sequences together.
-> It can be done using the + operator.
-> It can be done for strings, lists, tuples, etc.
-> For strings, it joins the strings together.
-> For lists, it joins the lists together.
-> For tuples, it joins the tuples together.
-> It does not work for different data types.
-> It does not work for sets.
-> Eg: 
    a = "Hello"
    b = "World"
    print(a + b)  # Output: HelloWorld
    c = [1, 2, 3]
    d = [4, 5, 6]
    print(c + d)  # Output: [1, 2, 3, 4, 5, 6]
    e = (1, 2, 3)
    f = (4, 5, 6)
    print(e + f)  # Output: (1, 2, 3, 4, 5, 6)
    
'''

#Arithmetic operators
num_1 = 10
num_2 = 20
print(num_1 + num_2) #Addition aperator

a_1 = 30
b_2 = 23
print(a_1 - b_2) #subtraction 

c_3 = 50
d_4 = 2
print(c_3 * d_4) #multiplication

e_5 = 100
f_6 = 20
print(e_5 / f_6) #division

g_7 = 40
h_8 = 13
print(g_7 % h_8) #modulo

i_9 = 4
j_10 = 2
print(i_9 ** j_10) #exponentiation

k_11 = 20
l_12 = 3
print(k_11 // l_12) #floor division

#comparison operators
m_1 = 10
n_2 = 30
print(m_1 == n_2)  #equal

o_3 = 50
p_4 = 20
print(o_3 != p_4)  #not equal

q_5 = 100
r_6 = 20
print(q_5 > r_6)  #greater than

s_7 = 40
t_8 = 13
print(s_7 < t_8)  #less than

u_9 = 100
v_10 = 20
print(u_9 >= v_10)  #greater than or equal to

w_11 = 40
x_12 = 40
print(w_11 <= x_12)  #less than or equal to

#Logical Operators
aa_1 = 10
ab_2 = 30
print(aa_1 != ab_2 and ab_2 >= aa_1)  #and

ac_3 = 50
ad_4 = 20
print(ac_3 == ad_4 or ad_4 >= ac_3)  #or

ae_5 = 100
print(not (ae_5 == 10))  #not

#Assignment Operators
af_1 = 10
print(af_1)  #Assignment

ag_2 = 13
ag_2 += 2
print(ag_2)  # Increment

ah_3 = 12
ah_3 -= 2
print(ah_3)  # Decrement

ai_4 = 25
ai_4 *= 4
print(ai_4)  # Multiply Assignment

aj_5 = 36
aj_5 /= 3
print(aj_5)  # Divide Assignment

ak_6 = 17
ak_6 %= 8
print(ak_6)  # Modulo Assignment

al_7 = 4
al_7 **= 3
print(al_7)  # Exponent Assignment

am_8 = 18
am_8 //= 5
print(am_8)  # Floor Division Assignment

an_9 = 5
an_9 *= 4
print(an_9)  # Multiplication Assignment

#Membership Operators
ao_1 = 8
print(ao_1 in [1, 2, 3, 4, 5])  #in

ap_2 = 12
print(ap_2 not in [1, 2, 3, 4, 5])  #not in

#Identity Operators
aq_1 = 32
ar_2 = 32
print(aq_1 is ar_2)  #is

as_3 = [1, 2, 3]
at_4 = [1, 2, 3]
print(as_3 is at_4)  #is

au_5 = 15
av_6 = 20
print(au_5 is not av_6)  #is not

aw_7 = [1, 2, 3]
ax_8 = [1, 2, 3]
print(aw_7 is not ax_8)  #is not