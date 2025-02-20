class SimpleVars():
    v = None
    def setload(self, value):
        self.v = value


def l_filter(arr=[], tof=None, key=None, index=False):
    found = None
    if key:
        for i,a in enumerate(arr):
            if a[key] == tof:
                if index:
                    return {"v": a, "i": i}
                else:
                    return {"v": a}
    else:
        for i,a in enumerate(arr):
            if a == tof:
                if index:
                    return {"v": a, "i": i}
                else:
                    return {"v": a}