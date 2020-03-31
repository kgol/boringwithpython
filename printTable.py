def printTable(table):
    colWidths=[0]*len(table)
    for i in range(len(table)):
        longest = max(table[i], key=len)
        num = len(longest)
        colWidths[i]=num

    print(colWidths)
    print(len(table[0][0]))
    print(table[0][0].rjust(colWidths[0]) + ' '+ table[1][0]+ ' '+table[2][0])
    print(table[0][1].rjust(colWidths[0]) + ' '+ table[1][1]+ ' '+table[2][1])
    print(table[0][2].rjust(colWidths[0]) + ' '+ table[1][2]+ ' '+table[2][2])
    print(table[0][3].rjust(colWidths[0]) + ' '+ table[1][3]+ ' '+table[2][3])
    


   


table1 = [['applesdffsdfds','oragne','banana','dyupa'],['Alicedd','Bob','Carol','David'],['dogs','cats','cats','goose']]

printTable(table1)

