import pickle

class Subscription:
    def __init__(self, sid: str, email: str, component: str):
        self.__sid = sid
        self.__email = email
        self.__component = component

    @property
    def sid(self):
        return self.__sid

    @property
    def email(self):
        return self.__email

    @property
    def component(self):
        return self.__component

    def __eq__(self, other):
        if isinstance(other, Subscription):
            return self.sid == other.sid and \
                     self.email == other.email and \
                     self.component == other.component
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Subscription):
            return self.sid != other.sid or \
                     self.email != other.email or \
                     self.component != other.component
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Subscription):
            return '/'.join([self.sid, self.component, self.email]) \
                   < '/'.join([other.sid, other.component, other.email])
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Subscription):
            return '/'.join([self.sid, self.component, self.email]) \
                   > '/'.join([other.sid, other.component, other.email])
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Subscription):
            return '/'.join([self.sid, self.component, self.email]) \
                   <= '/'.join([other.sid, other.component, other.email])
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Subscription):
            return '/'.join([self.sid, self.component, self.email]) \
                   >= '/'.join([other.sid, other.component, other.email])
        return NotImplemented

    def __hash__(self):
        return hash((self.sid, self.email, self.component))


# You can refinde, 
def loadData():
    # for reading also binary mode is important
    dbfile = open('examplePickle', 'rb')
    res = pickle.load(dbfile)
    for subs in res:
        print(subs.sid)
    dbfile.close()

if __name__ == "__main__":
    loadData()
