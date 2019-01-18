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

def main():
    res = []
    res.append(Subscription("a", "a@ab.com", "compa"))
    res.append(Subscription("b", "b@ab.com", "compa"))
    res.append(Subscription("c", "b@ab.com", "compa"))

    dbfile = open('examplePickle', 'ab') 
    pickle.dump(res, dbfile)
    dbfile.close()



if __name__ == "__main__":
    main()
