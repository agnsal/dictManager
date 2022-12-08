
'''
Copyright 2022 Agnese Salutari.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License
'''

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


def toDot(d, separator='.', currPath='', res={}):
    if not isinstance(d, dict):
        res[currPath] = d
    else:
        for k, v in d.items():
            toDot(v, separator, k if '' == currPath else f"{currPath}{separator}{k}")
    return res
