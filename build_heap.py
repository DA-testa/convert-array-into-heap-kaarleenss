# python3


def build_heap(data, n):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for j in range(n , 0, -1):
        # print(i)
        try:
            while(data[j - 1] <= data[(j // 2) - 1]):
                if j > 1:
                    data[(j // 2) - 1], data[j - 1] = data[j - 1], data[(j // 2) - 1]
                    swaps.append(((j // 2) - 1, j - 1))
                    j = n // 2
                else:
                    break
        except IndexError: 
            pass
        
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    burts = input()
    if burts == "I":
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))

    elif burts == "F":
        name = input()
        path = "./tests/" + name
        with open(path) as file:
            content = file.readlines()
        n = int(content[0].replace('\n', ''))
        data = map(int, content[1].replace('\n','').split(" "))
    


    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data, n)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
