def chess(a,b):
    for i in range(1,a+1):
        for j in range(1,b+1):
            if  i % 2==0:
                if j % 2==0:
                    print("| black |",end=" ")
                else:
                    print("| white |",end=" ")
            else:
                if j % 2 == 0:
                    print("| white |",end=" ")
                else:
                    print("| black |",end=' ')
            


        print()
chess(a=8,b=8)