
def compare_lists(lst1: str, lst2: str) -> int:
    if len(lst1) != len(lst2):
        raise Exception("lists do not match!")

    lst1 = sorted([int(n) for n in lst1])
    lst2 = sorted([int(n) for n in lst2])

    distance = 0
    for i in range(len(lst1)):
        distance += abs(lst1[i] - lst2[i])
    return distance

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        testcases = f.readlines()
    LL, RR = [], []
    with open("output.txt", "w") as f:
        for case in testcases:
            case_input = case.strip("\n").split("   ")
            LL.append(int(case_input[0]))
            RR.append(int(case_input[1]))
    print(compare_lists(sorted(LL), sorted(RR)))
