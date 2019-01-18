import pickle

# will crash in a Attribute error as Subscription is not defined
def loadData():
    # for reading also binary mode is important
    dbfile = open('examplePickle', 'rb')
    res = pickle.load(dbfile)
    for subs in res:
        print(subs.sid)
    dbfile.close()

if __name__ == "__main__":
    loadData()
