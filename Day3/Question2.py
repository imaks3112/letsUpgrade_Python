def main():
    for no in range(2, 201):
        half = int(no / 2)
        if half == 1:
            print(' Prime', no)
        else:
            flag = 0
            for j in range(2, half+1):
                if no % j != 0:
                    flag = no
                    continue
                else:
                    flag = 0
                    break
            if flag != 0:
                print('Prime', flag)


if __name__ == "__main__":
    main()