k=0

p=0

for i in range (3532000,3532161):

    for j in range (2,i):

        if i%j==0:

            if i==j:

                break

            else:

                k+=1

                break

    if k==0 and i!=1:

        p+=1        

        print (p, i)

    k=0