def main():
    try:
      a=int(input("Enter your number: "))
      return print(a)

    except Exception as e:
      return print("An error occurred:", e)

    finally:
      print("i am inside of finally")

main()