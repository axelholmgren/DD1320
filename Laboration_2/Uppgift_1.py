from array import array

arr = array("b")
for i in range(10):  # Lägger till 10 element i en array
    arr.append(i)

arr.insert(
    5, 10
)  # Lägger till värdet 10 på plats 5 och flyttar ned resten av arrayen med 1

arr.remove(10)  # Tar bort elementet med värdet 10

print(arr.pop(0))
# Tar bort elementet på ett givet index.
# Pop retunerar värdet som det bortagna elementet hade

print(arr)
