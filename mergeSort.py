#Sorts integers provided via a file named 'data.txt' via merge sort and exports the 
# sorted list to a file named 'merge.txt'
#Author: Shawn McMannis
#Last mod date: 4/5/19

#sorts a list of integers using merge sort
def mergeSort(toSort):

    if len(toSort) > 1:
        mid = len(toSort)//2 #find the middle index of the list
        left = toSort[:mid]
        right = toSort[mid:]

        #recursively call mergesort on the two halves
        mergeSort(left)
        mergeSort(right)

        #merge the two lists into one sorted list
        #loop control variables
        i = j = k = 0

        #merge the lists
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                toSort[k] = left[i]
                i+=1
            else:
                toSort[k] = right[j]
                j+=1
            k+=1

        #add any remaining list elements
        while i < len(left):
            toSort[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            toSort[k] = right[j]
            j+=1
            k+=1


#main
toSort = []

#open the export file
exportFile = open("merge.txt", "w")

#open import file 'data.txt'
with open("data.txt", "r") as importFile:
    for line in importFile:

        #save the value string as a list, delimited by ' '
        toSort = line.split()

        #convert string values to integers
        for i in range(0, len(toSort)):
            toSort[i] = int(toSort[i])

        #remove the first integer value from the list
        del toSort[0]

        #sort the list with merge sort
        mergeSort(toSort)

        #save the sorted list to 'merge.txt'
        for num in toSort:
            exportFile.write(str(num))
            exportFile.write(" ")
        exportFile.write("\n")

#close export file
exportFile.close()