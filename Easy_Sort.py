def SelectionSortStep(array,i):
    # Сортировка выбором-реализация одного шага
    if type(array) is list and i!=None: 
        size=len(array)
        if i+1>size:
            return None
       # elif i+1==size:
       #     return array
        else:
            min=array[i]
            index=i
            for j in range(i+1,size):
                if array[j]<min:
                    min=array[j]
                    index=j
            array[i],array[index]=array[index],array[i]
            return array
    else:
        return None

def BubbleSortStep(array):
    #Сортировка пузерьком, один цикл
    if type(array) is list: 
        size=len(array)
        count=0
        for j in range(0,size-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                count+=1
            else:
                pass
        if count==0:
            return True
        else:
            return False
    else: 
        return False
    
"""
a=[1,30,4,5,6,23,40,24]
#print(SelectionSortStep(a,6))

print(BubbleSortStep(a))
print(BubbleSortStep(a))
"""