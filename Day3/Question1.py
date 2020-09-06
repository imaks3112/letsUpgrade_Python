def main():
    altitude = int(input("Enter your value: "))
    print(type(altitude))
    if altitude <= 1000:
        print('Land the plane')
    elif altitude > 1000 and altitude <= 5000:
        print('Bring it to 1000ft')
    elif altitude > 5000:
        print('Go around and try again later')


if __name__ == "__main__":
    main()
