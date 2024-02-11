**1.PROGRAM**

N=int(input("enter the rows="))

for i in range(1,N+1):

    for j in range(i):

        print('1',end='')

    print(a)

 **OUTPUT:**

 enter the rows=5
 
 1
 
 11
 
 111

 1111
 
 11111

 **2.PROGRAM:**
 
 N=int(input("N="))
 
 for i in range(1,N):
 
    for j in range(1,N):
 
        table=i*j
 
        print(f"{i}*{j}=",table)
 
    print()
 
 **OUTPUT:**
 
 N=11

 1*1= 1

 
 1*2= 2
 
 1*3= 3
 
 1*4= 4
 
 1*5= 5
 
 1*6= 6
 
 1*7= 7
 
 1*8= 8
 
 1*9= 9
 
 1*10= 10

 2*1= 2
 
 2*2= 4
 
 2*3= 6
 
 2*4= 8
 
 2*5= 10
 
 2*6= 12
 
 2*7= 14
 
 2*8= 16
 
 2*9= 18
 
 2*10= 20

 
 3*1= 3
 
 3*2= 6
 
 3*3= 9
 
 3*4= 12
 
 3*5= 15
 
 3*6= 18
 
 3*7= 21
 
 3*8= 24
 
 3*9= 27
 
 3*10= 30

 4*1= 4
 
 4*2= 8
 
 4*3= 12
 
 4*4= 16
 
 4*5= 20
 
 4*6= 24
 
 4*7= 28
 
 4*8= 32
 
 4*9= 36
 
 4*10= 40

 5*1=10

 5*2= 10
 
 5*3= 15
 
 5*4= 20
 
 5*5= 25
 
 5*6= 30

 5*7= 35

 5*8= 40
 
 5*9= 45
 
 5*10= 50

 6*1= 6
 
 6*2= 12
 
 6*3= 18
 
 6*4= 24
 
 6*5= 30
 
 6*6= 36
 
 6*7= 42
 
 6*8= 48
 
 6*9= 54
 
 6*10= 60

 7*1= 7
 
 7*2= 14
 
 7*3= 21
 
 7*4= 28
 
 7*5= 35
 
 7*6= 42
 
 7*7= 49
 
 7*8= 56
 
 7*9= 63
 
 7*10= 70

 8*1= 8
 
 8*2= 16

 8*3= 24

 8*4= 32

 8*5= 40

 8*6= 48

 8*7= 56

 8*8= 64

 8*9= 72

 8*10= 80

 
 9*1= 9
 
 9*2= 18
 
 9*3= 27
 
 9*4= 36
 
 9*5= 45
 
 9*6= 54
 
 9*7= 63
 
 9*8= 72
 
 9*9= 81
 
 9*10= 90

 10*1= 10
 
 10*2= 20
 
 10*3= 30
 
 10*4= 40
 
 10*5= 50
 
 10*6= 60
 
 10*7= 70
 
 10*8= 80
 
 10*9= 90
 
 10*10= 100


**3.PROGRAM:**
 
 N=int(input("N="))
 
 for p in range(2,N+1):
 
    c=0
 
    for i in range(1,p+1):
 
        if(p%i==0):
 
            c=c+1
 
    if(c==2):
 
        print(p)

    
 **OUTPUT:**
 N=20

 2
 
 3
 
 5
 
 7
 
 11

 13
 
 17
 
 19

**4.PROGRAM:**

 N=int(input("N="))
 
 a=0
 
 b=1

 for i in range(1,N):
    
    c=a+b
    
    print(c)
    
    a=b
    
    b=c

 **OUTPUT:**

 N=10

 1

 2
 
 3
 
 5
 
 8
 
 13
 
 21
 
 34
 
 55


**5.PROGRAM:**

def generate_pascals_triangle(n):

    triangle = []

    for i in range(n):

        row = [1] * (i + 1)

        if i > 1:

            for j in range(1, i):

                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle


def print_pascals_triangle(triangle):

    for row in triangle:

        print(" ".join(map(str, row)).center(len(triangle[-1]) * 3))

def main():

    try:

        n = int(input("Enter the number of rows for Pascal's triangle: "))

        if n < 0:

            raise ValueError("Number of rows should be a non-negative integer.")

    except ValueError as e:

        print(f"Error: {e}")

        return

    pascals_triangle = generate_pascals_triangle(n)

    print_pascals_triangle(pascals_triangle)

 if __name__ == "__main__":

    main()

 **OUTPUT:**

 Enter the number of rows for Pascal's triangle: 10

              1               

             1 1              

            1 2 1             

           1 3 3 1            

          1 4 6 4 1           

        1 5 10 10 5 1         

       1 6 15 20 15 6 1       

     1 7 21 35 35 21 7 1      

    1 8 28 56 70 56 28 8 1    

 1 9 36 84 126 126 84 36 9 1  
