
def checkHasSubDict(d):
    if isinstance(d, dict):
        for item in list(d.values()):
            if isinstance(item, dict):
                return True
    return False


def numb(d, k):
    for i in range(0, len(d[k])):
        d[f"{k}.{i}"] = d[k][i]
    del d[k]


def __cleanCollapsed(c):
    outdated = []
    keys = c.keys()
    for k, v in c.items():
        for item in keys:
           if item not in outdated and k.startswith(f"{item}."):
               outdated.append(item)
    for o in outdated:
        del c[o]


def __collapse(d, identifier='id', res={}, currPath='', recursion=False, separator='.'):
    for k, v in d.items():
        if isinstance(v, dict):
            if not (identifier in v and k == v[identifier]):
                currPath = k if '' == currPath else f"{currPath}{separator}{k}"
                currVals = list(v.values())
                res[currPath] = currVals
                for i in range(0, len(currVals)):
                    __collapse(currVals[i], identifier, res, f"{currPath}{separator}{i}", True, separator)
                numb(res, currPath)
            else:
                # currPath = k if '' == currPath else f"{currPath}{separator}{k}"
                __collapse(v, identifier, res, k, True, separator)
                # res[k] = v
        elif not recursion:
            res[k] = v
        else:
            res[f"{currPath}{separator}{k}"] = v
    return res


def collapse(d, identifier):
    res = __collapse(d, identifier)
    __cleanCollapsed(res)
    return res




# def __oldCollapse(d, identifier='id', res={}, currPath='', recursion=False):
#     for k, v in d.items():
#         if isinstance(v, dict):
#             if not (identifier in v and k == v[identifier]):
#                 currPath = k if '' == currPath else f"{currPath}.{k}"
#                 currVals = list(v.values())
#                 res[currPath] = currVals
#                 for i in range(0, len(currVals)):
#                     __collapse(currVals[i], identifier, res, f"{currPath}.{i}", True)
#                 numb(res, currPath)
#             else:
#                 currPath = k if '' == currPath else f"{currPath}.{k}"
#                 res[k] = v
#         elif not recursion:
#             res[k] = v
#         else:
#             res[currPath] = v
#     return res