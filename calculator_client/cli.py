from calculator_client import RemoteCalculator, CalculationError



def main():
    try:
        server_address = _ask_for_server_address()
        rc = RemoteCalculator(server_address)
        rc.connect()
        while True:
            expression = _ask_for_expression()

            try:
                result = rc.calculate(expression)

            except CalculationError as e:
                print(str(e), "\n")

            else:
                print(result, "\n")

    except KeyboardInterrupt:
        print("\rBye")
    except ConnectionError as e:
        print(str(e), "\nClosing program.\n")


def _ask_for_server_address():
    server_address = input("\nProvide calculation server address:\n")
    print('')
    return server_address


def _ask_for_expression():
    expression = input("Provide simple math expression and press enter, "
                       "only integers allowed:\n")
    return expression


if __name__ == "__main__":
    main()
