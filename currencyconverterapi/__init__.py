from argparse import ArgumentParser
from os import environ
from os import remove as remove_file
from sys import stdout

from .client import CurrencyConverterApi


def main():
    KEY_FILE = f"{environ['HOME']}/.currencyconverterapi"
    parser = ArgumentParser(description="Simplest currency converter with pure python with CurrecnyConverterApi")
    parser.add_argument("arguments", nargs="+", help="Amount source destination (1 usd try)")
    parser.add_argument("-k", "--key", help="Free api key for currencyconverterapi.com")
    parser.add_argument("-s", dest="save", action="store_true", help="Save the key file ($HOME/.currencyconverterapi)")
    parser.add_argument("-r", dest="remove", action="store_true", help="Remove the key file ($HOME/.currencyconverterapi)")
    args = parser.parse_args()

    key = args.key
    remove = args.remove
    try:
        if key:
            if args.save:
                with open(KEY_FILE, "w") as file:
                    file.write(key)
        else:
            with open(KEY_FILE, "r") as file:
                key = file.read(key)
        if remove:
            remove_file(KEY_FILE)
    except:
        raise RuntimeError("Use `--key` command to pass API key or add -s command to save API key")

    arguments = args.arguments
    if len(arguments) != 3:
        raise ValueError("Valid format: amount source destination (1 usd try)")

    amount, source, destination = arguments
    converter = CurrencyConverterApi(key)
    value = converter.convert(float(amount), source, destination)
    stdout.write(str(value) + "\n")
    stdout.flush()


if __name__ == "__main__":
    main()
