


print("Enter the interval (starting and ending number): ");
start = input();
if start == 'x':
    exit();
else:
    end = input();
    lower = int(start);
    upper = int(end);
    for num in range(lower, upper+1):
        tot = 0;
        temp = num;
        while temp != 0:
            dig = temp % 10;
            tot += dig ** 3;
            temp //= 10;
        if num == tot:
            print(num);
            