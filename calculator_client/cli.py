from calculator_client import calculate, CalculationError


def main():
    expression = _input_from_initial_prompt()

    try:
        result = calculate(expression)
    except CalculationError as e:
        print("Calculation error: " + str(e), "\n")
    else:
        print(result, "\n")


def _input_from_initial_prompt():
    expression = input("Give me some simple equation and press enter,"
                    " only integers allowed: \n")
    return expression


if __name__ == "__main__":
    print("")
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("\rBye\n")