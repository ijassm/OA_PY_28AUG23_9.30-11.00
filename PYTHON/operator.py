##Python divides the operators in the following groups:

##Arithmetic operators
##Assignment operators
##Comparison operators
##Logical operators
##Identity operators
##Membership operators
##Bitwise operators


##Arithmetic operators

"""
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	        x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y
"""

##x = 5
##y = 2

##print(x + y)
##print(x - y)
##print(x * y)
##print(x / y)
##print(x % y)
##print(x ** y)
##print(x // y)

##-------------------------------------##

##Assignment operators
"""
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3
"""

##x = 5

##x = x + 2

##x += 2

##print(x)

##-------------------------------------##

##Comparison operators

"""
----------------------------------------------------
Operator    Name	                    Example
----------------------------------------------------
==	    Equal	                    x == y	
!=	    Not equal	                    x != y	
>	    Greater than	            x > y	
<	    Less than	                    x < y	
>=	    Greater than or equal to        x >= y	
<=	    Less than or equal to	    x <= y
----------------------------------------------------
"""

##x = 2
##y = 4

##print(x == y)
##print(x != y)
##print(x > y)
##print(x < y)
##print(x >= 2)
##print(x >= 3)
##print(x <= 3)

##-------------------------------------##

##Logical operators

"""
-------------------------------------------------------------
Operator	Description	            Example
-------------------------------------------------------------
and 	  Returns True if both
          statements are true	        x < 5 and  x < 10	
or	  Returns True if one of
          the statements is true	x < 5 or x < 4	
not	  Reverse the result, returns
          False if the result is true	not(x < 5 and x < 10)
-------------------------------------------------------------
"""

##5
##4
##3
##2
##1
##0
##-1
##-2
##-3
##-4
##-5

##print(0 > -278978965 and 3 > 0)
##print(not(2 > -2 and not(-3 > 0)))
##
##print(2 > -2 or -3 > 0)

#Membership operator
#in not in

##a = "hello"

##print("oh" in a or "z" not in a)
##print(5675 or 876)



#Identity operator

##a = 45
##b = 45
##c = ["45", "47", "34"]
##d = c
##e = ["45", "47", "34"]

##d[2] = "24"

##print(d)
##print(c)
##print(e)

##print(id(a))
##print(id(b))
##print(id(c))
##print(id(d))

##print(bin(24))

##print(c is e)
##print(c == e)



