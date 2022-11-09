# Write your solution here
layer = int(input("Give a number between 2 and 26: "))
table_size = layer + layer - 1
ts = table_size
center = (ts // 2)
counter=0
for row in range(ts):
        for col in range(ts):
                if row<=center and ts-counter>col:
                    outcome=65+center-min(row,col)
                elif row <=center and col>=ts-counter :
                    outcome=65+col-center   
                elif row>center and ts-counter>col:
                    outcome=65+center-min(row,col)  
                elif row >center and col<counter :   
                    outcome=65+row-center
                elif row >center and col>=counter :   
                    outcome=65+row-center+(col-counter)                   
                
                print(chr(outcome), end="")
        counter=counter+1        
               
        print()