class Calculator:
    def _init_(self):
        pass

    def run(self):
        while True:
            user_input = input("Enter 'ON' to start or 'OFF' to exit: ").strip().upper()

            if user_input == "ON":
                try:
                    a = float(input("Enter first number: "))
                    operation = input("Select operator (+ - x / %): ").strip()
                    b = float(input("Enter second number: "))

                    self.a = a
                    self.b = b

                    if operation == "+":
                        print("Result:", self.add())
                    elif operation == "-":
                        print("Result:", self.subtraction())
                    elif operation == "x":
                        print("Result:", self.multiplication())
                    elif operation == "/":
                        print("Result:", self.division())
                    elif operation == "%":
                        print("Result:", self.percentage())
                    else:
                        print("Invalid operator.")
                except ValueError:
                    print("Invalid number input. Try again.")

            elif user_input == "OFF":
                print("Calculator turned OFF.")
                break
            else:
                print("Invalid input. Please enter 'ON' or 'OFF'.")

    def add(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        if self.b == 0:
            return "Error! Division by zero."
        return self.a / self.b

    def percentage(self):
        if self.b == 0:
            return "Error! Division by zero."
        return (self.a * 100) / self.b


Calculator().run()
