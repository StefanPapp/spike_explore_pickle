from subscription import Subscription
import json

def main():
    res = []
    res.append(Subscription("a", "a@ab.com", "compa"))
    res.append(Subscription("b", "b@ab.com", "compa"))
    res.append(Subscription("c", "b@ab.com", "compa"))

    print(json.dumps(res[0].__dict__))




if __name__ == "__main__":
    main()
