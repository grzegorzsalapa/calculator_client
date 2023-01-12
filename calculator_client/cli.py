from calculator_client import calculate, CalculationError

if __name__ == "__main__":
    try:
        while True:
            exp_str = input("Give me some simple equation and press enter,"
                            " only integers allowed: \n")  # Initial prompt for the user

            try:
                result = calculate(exp_str)
            except CalculationError as e:
                print("Calculation error: " + str(e))
            else:
                print(result, "\n")

    except KeyboardInterrupt:
        print("\rBye")