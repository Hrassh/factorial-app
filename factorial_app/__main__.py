import sys

from .factorial import factorial


def main(argv=None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1:
        print("Використання: python -m factorial_app <n>", file=sys.stderr)
        return 2
    try:
        n = int(args[0])
    except ValueError:
        print(f"Помилка: '{args[0]}' не є цілим числом", file=sys.stderr)
        return 1
    try:
        print(factorial(n))
    except ValueError as e:
        print(f"Помилка: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
