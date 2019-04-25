

from subscription import Subscription
import json


def main():
    with open("/workspace/me/pickle/demo.json") as data_file:
        data = json.load(data_file)

    instance = object.__new__(Subscription)

    for item in data:
        instance.__dict__ = item
        print(instance.sid)

if __name__ == "__main__":
    main()
