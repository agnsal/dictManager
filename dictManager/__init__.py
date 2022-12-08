
def checkHasSubDict(d):
    if isinstance(d, dict):
        for item in list(d.values()):
            if isinstance(item, dict):
                return True
    return False


def numb(d, k, separator):
    for i in range(0, len(d[k])):
        d[f"{k}{separator}{i}"] = d[k][i]
    del d[k]


def __cleanCollapsed(c, separator):
    outdated = []
    keys = c.keys()
    for k, v in c.items():
        if k not in outdated:
            for item in keys:
               if item not in outdated and k.startswith(f"{item}{separator}"):
                   outdated.append(item)
    for o in outdated:
        del c[o]


def __collapse(d, identifier='id', separator='.', res={}, currPath='', recursion=False):
    for k, v in d.items():
        if isinstance(v, dict):
            if not (identifier in v and k == v[identifier]):
                currPath = k if '' == currPath else f"{currPath}{separator}{k}"
                currVals = list(v.values())
                res[currPath] = currVals
                for i in range(0, len(currVals)):
                    __collapse(currVals[i], identifier, separator, res, f"{currPath}{separator}{i}", True)
                numb(res, currPath, separator)
            else:
                # currPath = k if '' == currPath else f"{currPath}{separator}{k}"
                __collapse(v, identifier, separator, res, k, True)
                # res[k] = v
        elif not recursion:
            res[k] = v
        else:
            res[f"{currPath}{separator}{k}"] = v
    return res


def collapse(d, identifier, separator='.'):
    res = __collapse(d, identifier, separator)
    __cleanCollapsed(res, separator)
    return res
