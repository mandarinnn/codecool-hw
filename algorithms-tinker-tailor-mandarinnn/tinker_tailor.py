
def tailor(n, k):
    tailor_list = []
    new = []
    a = 0
    for i in range(1, n + 1):
        tailor_list.append(i)

    for i in range(n):
        a = (a + (k - 1)) % n
        new.append(tailor_list.pop(a))
        n = n - 1
    return new


def main():
    print(tailor(5, 3))

if __name__ == '__main__':
    main()
