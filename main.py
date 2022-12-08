from pprint import pprint

import dictManager


def test():
    d = {
        'tizio': {  # tizio:{ name: _, caio: [], ...}
            '0A': {
                'name': '0A',
                'caio': {
                    '1A': {'name': '1A', 'test': 'ciao'},
                    '1B': {'name': '1B', 'test': 1, 'x': 2},
                    '1C': {
                        'name': '1C',
                        'sempronio': {
                            '2A': {'name': '2A', 'y': 3},
                            '2B': {
                                'name': '2B',
                                'caio': {
                                    '1AR': {'name': '1AR', 'test': 'hello'},
                                    '1BR': {'name': '1BR', 'test': None},
                                    '1CR': {'name': '1CR'}
                                }
                            }
                        }
                    }
                }
            },
            '0B': {'name': '0B', 'test': 3},
            '0C': {'name': '0C', 'test': 1}
        },
        'test': 'lol',
        'test2': {
            'name': 'test2',
            'x': 'ok'
        }
    }
    identifier = 'name'
    res = dictManager.collapse(d, identifier)
    pprint(res)


if __name__ == '__main__':
    test()
