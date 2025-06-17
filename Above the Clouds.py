def can_split_into_abc(n, s):
    for i in range(1, n - 1):
        a = s[:i]
        b = s[i]
        c = s[i + 1:]
        if b in (a + c):
            return "Yes"
    return "No"

def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        s = input()
        results.append(can_split_into_abc(n, s))
    print("\n".join(results))

if __name__ == "__main__":
    main()
