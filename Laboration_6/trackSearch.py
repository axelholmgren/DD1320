# from trackclassFile import Track
import timeit
from trackclassFile import Track
from hashtableFile import Hashdict


def readtrack(test_len):
    # Lägger till alla låtar i en lista och en hashtable och läser från filen
    with open(
        "/Users/axelholmgren/GitHub/DD1320/Laboration_6/unique_tracks.txt",
        "r",
        encoding="utf-8",
    ) as trackfile:
        tracklist = []
        counter = 0
        hashtable = Hashdict()
        for rad in trackfile:
            if counter == test_len:
                break
            trackparts = rad.split("<SEP>")
            tracklist.append(
                Track(
                    trackparts[0],
                    trackparts[1],
                    trackparts[2].strip(),
                    trackparts[3].strip(),
                )
            )
            hashtable.add(trackparts[3].strip())
            counter += 1
        return tracklist, hashtable


def linjärsök(tracklist, sökt):
    # sourcery skip: use-any, use-next
    for i in tracklist:
        if i.låttitel == sökt:
            return True
    return False


def binärsök(tracklist, sökt):
    # Funktion för binärsökningen. Tidkomplexitet O(log n)
    while len(tracklist) != 1:
        mid = len(tracklist) // 2
        if tracklist[mid].låttitel == sökt:
            return True
        elif tracklist[mid].låttitel < sökt:
            tracklist = tracklist[mid:]
        else:
            tracklist = tracklist[:mid]
    return False


def hashsök(hashtable, sökt):
    # Funktion för hashsökning. Tidskomplexitet 1
    try:
        if (
            hashtable.table[hash(sökt)] == sökt
        ):  # Kollar om det ligger något sparat på hash(låttitel) index
            return True
    except KeyError:
        return False


def bubble_sort(list):
    # Bubblesort funktion
    # Teoretisk tidskomplexitet: O(n^2)
    for i in range(len(list)):
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


# Funktion hämtad från DD1320 Föreläsnings 9: Sortering. Av Sten Andersson
def mergesort(data):
    # Teroetisk tidkomplexitet: O(log(n)*n)
    if len(data) > 1:  # Delar upp datan i tvåhalvor men endat om det är mer än ett element
        mitten = len(data) // 2
        vensterHalva = data[:mitten]
        hogerHalva = data[mitten:]

        mergesort(vensterHalva)
        mergesort(hogerHalva)

        i, j, k = 0, 0, 0

        while i < len(vensterHalva) and j < len(hogerHalva):  # Mergar vänster och höger
            if vensterHalva[i] < hogerHalva[j]:
                data[k] = vensterHalva[i]
                i = i + 1
            else:
                data[k] = hogerHalva[j]
                j = j + 1
            k = k + 1

        while i < len(vensterHalva):  # Lägger till de sista delarna från vänster
            data[k] = vensterHalva[i]
            i = i + 1
            k = k + 1

        while j < len(hogerHalva):  # Lägger till de sista delarna fårn höger
            data[k] = hogerHalva[j]
            j = j + 1
            k = k + 1


# print("linjärsök: " + str(linjärsök(tracklist, "Bad Romance")))
# print("binärsök:  " + str(binärsök(tracklist, "Eye Of The Tiger")))
# print("hashsök:  " + str(hashsök(hashtable, "Eye Of The Tiger")))


def time_sort():
    # Funktion för att ta tid på sorteringsalgoritmer
    tracklist, hashtable = readtrack(1000)
    bubbletid = timeit.timeit(stmt=lambda: bubble_sort(tracklist), number=100)
    mergetid = timeit.timeit(stmt=lambda: mergesort(tracklist), number=1)
    print("Mergesorteringen tog", round(mergetid, 4), "sekunder")
    print("Bubblesorteringen tog", round(bubbletid, 4), "sekunder")


def main():
    # Funkton för att ta tid på sökalgoritmer
    tracklist, hashtable = readtrack(250000)
    tracklist_sorted = tracklist.copy()
    tracklist_sorted.sort()
    linjtid = timeit.timeit(stmt=lambda: linjärsök(tracklist, tracklist[-1].låttitel), number=1000)
    bintid = timeit.timeit(stmt=lambda: binärsök(tracklist, tracklist[-1].låttitel), number=1000)
    hashtid = timeit.timeit(
        stmt=lambda: hashsök(hashtable, hashtable.table[hash(tracklist[-1].låttitel)]), number=1000
    )
    print("Linjärsökningen tog", round(linjtid, 4), "sekunder")
    print("Binärsökningen tog", round(bintid, 4), "sekunder")
    print("Hashsökningen tog", round(hashtid, 4), "sekunder")


# time_sort()
main()
