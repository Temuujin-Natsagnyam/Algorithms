def seperate(word):  # function that takes a word and makes it a list of all the characters inside the word
    result = []
    for l in word:
        result.append(l)
    return result
def main():
    b_num = input("Welcome to binary 2's complement converter!\n\nEnter binary number >>\t")

    if b_num.isnumeric() is False:                #catch exception
        print("Please enter numeric values 1 or 0!")

    str_num = seperate(b_num)

    flag = 0
    for place in range(len(str_num)):
        if str_num[place] == "0":
            str_num[place] = "1"
        elif str_num[place] == "1":
            str_num[place] = "0"
        else:
            flag = 1
            break

    if flag == 0:
        print("\nFirst step is to flip all the digits")
        print("Before:  "+b_num)
        print("After:   "+("".join(str_num)))
    else:
        print("Only enter 1 or 0")

    if str_num == seperate((len(str_num) * "1")):
        return "\nThe final step would be to add 1, but there's been an Overflow error! Not enough memory to fit correct value!"


    if str_num[len(str_num) - 1] == "1":
        y = len(str_num)-1
        carry = 0
        while y != carry-1:
            if str_num[y-carry] == "0":
                str_num[y-carry] = "1"
                break
            elif str_num[y-carry] == "1":
                str_num[y-carry] = "0"
            carry += 1

    elif str_num[len(str_num) - 1] == "0":
        str_num[len(str_num) - 1] = "1"

    return("\nThe final step is to add a 1 to it:\n\t"+("".join(str_num)))
print(main())
