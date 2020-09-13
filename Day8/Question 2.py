try :
    file = open("Demo.txt","r")
    file.write("Hiii")
    file.close()
    print("Success")
except Exception as e:
    print(e)
finally:
    print("HEY I WILL EXECUTE WHT so ever it may be ")