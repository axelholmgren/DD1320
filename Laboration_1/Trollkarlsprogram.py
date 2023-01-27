import sys

from linkedQFile import LinkedQ

usr_promt = sys.stdin.readline().split() # Användarinmatning som sparas till en lista separerad med mellanslag

q = LinkedQ() # Skapar en tom array

for i in usr_promt:
    q.enqueue(i) #Stoppar in alla  de valda korten i en kö

out = ''
 
while not q.isEmpty(): # kör så länge det finns något i kön
    q.enqueue(q.dequeue()) # Plockar ut det första i kön och läser värdet och lägger sist i kön
    out += str(q.dequeue()) + ' ' # Lägger till det nya första elementet till en out variabel
print(out) # 7 1 12 2 8 3 11 4 9 5 13 6 10