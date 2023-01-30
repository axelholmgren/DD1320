from arrayQFile import ArrayQ

usr_promt = input('Skriv nummren på korten separerade med mellanslag').split() # Användarinmatning som sparas till en lista separerad med mellanslag

q = ArrayQ() # Skapar en tom array

count = 0
for i in usr_promt:
    q.enqueue(int(i)) #Stoppar in alla de valda korten i en kö
    count += 1 # tar reda på hur många element som finns i kön

out = ''
for j in range(count): #Loopar för antalet element
    q.enqueue(q.dequeue()) # Plockar ut det första i kön och läser värdet och lägger sist i kön
    out += str(q.dequeue()) + ' ' # Lägger till det nya första elementet till en out variabel
print(out) # 7 1 12 2 8 3 11 4 9 5 13 6 10