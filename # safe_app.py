# safe_app.py
# A simple, safe program with no external dependencies.

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    :param numbers: list of int or float
    :return: float
    :raises ValueError: if the list is empty
    :raises TypeError: if any item is not a number
    """
    if not numbers:
        raise ValueError("List of numbers cannot be empty.")

    total = 0.0
    count = 0

    for n in numbers:
        if not isinstance(n, (int, float)):
            raise TypeError("All items must be int or float, got: "
                            f"{type(n).__name__}")
        total += n
        count += 1

    return total / count


def main():
    values = [10, 20, 30, 40]
    avg = calculate_average(values)
    print(f"Input values: {values}")
    print(f"Average: {avg}")


if __name__ == "__main__":
    main()
