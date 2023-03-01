from testhashtable import Hashtable
from sys import stdin


def test_sample_1():
    file = open("/Users/axelholmgren/GitHub/DD1320/Laboration_7/sampleoutput1.txt", "r")
    return file


def test_sample_2():
    file = open("/Users/axelholmgren/GitHub/DD1320/Laboration_7/sampleinput2.txt", "r")
    return file


def main():
    hashtable = Hashtable(150001)

    for line in test_sample_2():
        line = line.strip()
        key, *value = line.split()
        if key == "#":
            break
        elif len(value) != 0:
            hashtable.store(key, value[0])
        else:
            try:
                value = hashtable.search(key)
                print(value)
            except KeyError:
                print("None")
    for i in hashtable.table:
        if i != None:
            print(i.key)
    print(hashtable.crashlist)
    print(hashtable.crash)

    for line in stdin:
        line = line.strip()
        key, *value = line.split()
        if key == "#":
            break
        elif len(value) != 0:
            hashtable.store(key, value[0])
        else:
            try:
                value = hashtable.search(key)
                print(value)
            except KeyError:
                print("None")


if __name__ == "__main__":
    main()
