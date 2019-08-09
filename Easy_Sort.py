def SelectionSortStep(array,i):
    # Сортировка выбором-реализация одного шага
    if type(array) is list and i!=None: 
        size=len(array)
        if i+1>size:
            return None
        elif i+1==size:
            return array
        else:
            min=array[i]
            index=i
            for j in range(i+1,size):
                if array[j]<min:
                    min=array[j]
                    index=j
            array[i],array[j]=array[j],array[i]
            return array
    else:
        return None

def BubbleSortStep(array,i):
    #Сортировка пузерьком, один цикл
    if type(array) is list and i!=None: 
        size=len(array)
        if i+1>size:
            return None
        elif i+1==size:
            return array
        else:
            index=i
            for j in range(i+1,size):
                if array[index]>array[j]:
                    array[index],array[j]=array[j],array[index]
                    index=j
                else:
                    return array

"""
a=[1,30,4,5,6,23,4,24]
print(SelectionSortStep(a,1))
print(BubbleSortStep(a,1))
"""