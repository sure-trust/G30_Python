**LOOPS**

**1.Triangle Pattern**

**Sol:**

  n=int(input("Enter size of pattern"))

 print("The pattern for give size ",n,"is : \n")

 for i in range(1,n+1):

    for j in range(1,i+1):

        print("*",end=" ")

    print()  

 **OUTPUT:**

 Enter size of pattern5

 The pattern for give size  5 is :

 1

 1 1

 1 1 1

 1 1 1 1

 1 1 1 1 1

 Enter size of pattern3

 The pattern for give size  3 is :

 1

 1 1

 1 1 1

 **2.Multiplication tables**

 **Sol:**

 for i in range(1,10+1):

    print("Multiplication table of ",i)

    for j in range(1,10+1):

        print(i," * ",j," = ",i*j)

    print()

**Output**

Multiplication table of  1

1  *  1  =  1

1  *  2  =  2

1  *  3  =  3

1  *  4  =  4

1  *  5  =  5

1  *  6  =  6

1  *  7  =  7

1  *  8  =  8

1  *  9  =  9

1  *  10  =  10

Multiplication table of  2

2  *  1  =  2

2  *  2  =  4

2  *  3  =  6

2  *  4  =  8

2  *  5  =  10

2  *  6  =  12

2  *  7  =  14

2  *  8  =  16

2  *  9  =  18

2  *  10  =  20

Multiplication table of  3

3  *  1  =  3

3  *  2  =  6

3  *  3  =  9

3  *  4  =  12

3  *  5  =  15

3  *  6  =  18

3  *  7  =  21

3  *  8  =  24

3  *  9  =  27

3  *  10  =  30

Multiplication table of  4

4  *  1  =  4

4  *  2  =  8

4  *  3  =  12

4  *  4  =  16

4  *  5  =  20

4  *  6  =  24

4  *  7  =  28

4  *  8  =  32

4  *  9  =  36

4  *  10  =  40

Multiplication table of  5

5  *  1  =  5

5  *  2  =  10

5  *  3  =  15

5  *  4  =  20

5  *  5  =  25

5  *  6  =  30

5  *  7  =  35

5  *  8  =  40

5  *  9  =  45

5  *  10  =  50

Multiplication table of  6

6  *  1  =  6

6  *  2  =  12

6  *  3  =  18

6  *  4  =  24

6  *  5  =  30

6  *  6  =  36

6  *  7  =  42

6  *  8  =  48

6  *  9  =  54

6  *  10  =  60

Multiplication table of  7

7  *  1  =  7

7  *  2  =  14

7  *  3  =  21

7  *  4  =  28

7  *  5  =  35

7  *  6  =  42

7  *  7  =  49

7  *  8  =  56

7  *  9  =  63

7  *  10  =  70

Multiplication table of  8

8  *  1  =  8

8  *  2  =  16

8  *  3  =  24

8  *  4  =  32

8  *  5  =  40

8  *  6  =  48

8  *  7  =  56

8  *  8  =  64

8  *  9  =  72

8  *  10  =  80

Multiplication table of  9

9  *  1  =  9

9  *  2  =  18

9  *  3  =  27

9  *  4  =  36

9  *  5  =  45

9  *  6  =  54

9  *  7  =  63

9  *  8  =  72

9  *  9  =  81

9  *  10  =  90

Multiplication table of  10

10  *  1  =  10

10  *  2  =  20

10  *  3  =  30

10  *  4  =  40

10  *  5  =  50

10  *  6  =  60

10  *  7  =  70

10  *  8  =  80

10  *  9  =  90

10  *  10  =  100

**3.Prime number within  a given range**

**Sol:**

 n=int(input("Enter a number for range to fing prime numbers : "))

 for i in range(1,n+1):

    c=0

    for j in range(1,i+1):

        if(i%j==0):

            c=c+1

    if(c==2):

        print(i,end=" ")

 **Output:**

 Enter a number for range to fing prime numbers : 20

 2 3 5 7 11 13 17 19

 Enter a number for range to fing prime numbers : 50

 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47

 **4.Fibonocii Series**

 **Sol:**

 n=int(input("Enter range for fibonocii series : "))
 
 a=0
 
 b=1
 
 print(a,b,end=" ")
 
 for i in range(1,n-2+1):
 
    temp=a+b
 
    a=b
 
    b=temp
 
    print(temp,end=" ")

 **Output:**

 Enter range for fibonocii series : 7
 
 0 1 1 2 3 5 8

 Enter range for fibonocii series : 13
 
 0 1 1 2 3 5 8 13 21 34 55 89 144
 
 **5.Pascal Triangle:**

 **Sol:**

 n=int(input("Enter size of pascal triangle : "))
 
 for i in range(1,n+1):
 
    for s in range(1,n-i+1):
 
        print(" ",end=" ")
 
    c=1
 
    for j in range(1,i+1):
 
        print(c,end=" ")
 
        c=c*(i-j)//j
 
    print()
        
 **Output**

 Enter size of pascal triangle : 5
 
        1
 
      1 1
 
    1 2 1
 
  1 3 3 1
 
 1 4 6 4 1

 Enter size of pascal triangle : 8
 
              1
 
            1 1
 
          1 2 1
 
        1 3 3 1
 
      1 4 6 4 1
 
    1 5 10 10 5 1
 
  1 6 15 20 15 6 1
 
 1 7 21 35 35 21 7 1






 