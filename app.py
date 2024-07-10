import torch


def main():
    print("Hello Barboards!")
    print("Is cuda available?:", end="")
    if torch.cuda.is_available():
        print("Yes")
    else:
        print("No")
    print("Goodbye!")


if __name__ == '__main__':
    main()