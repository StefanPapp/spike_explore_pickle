from subscription import Subscription
import json

def main():
    res = []
    res.append(Subscription("a", "a@ab.com", "compa"))
    res.append(Subscription("b", "b@ab.com", "compa"))
    res.append(Subscription("c", "b@ab.com", "compa"))
    ret = "["

    for sub in res:
        ret = ret + json.dumps(sub.__dict__) + ","

    ret = ret + "]"

    with open("demo.json", "wt") as text_file:
        text_file.write(ret)

    print(ret)

if __name__ == "__main__":
    main()
