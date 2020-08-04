from typing import Any, Dict, List


def set_ls(ls: List[List]) -> List[List]:
    ls2: List[List] = []
    for x in ls:
        if x not in ls2:
            ls2.append(x)
    return ls2


class ComplDict(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dic: Dict[Any, Any] = dict()

    def __dict__(self):
        return self.dic

    def __iter__(self):
        return iter(self.dic)

    def __setitem__(self, key, value):
        if key in self:
            super().__delitem__(self.get(key))
        if value in self:
            raise Exception(f"Attempting to add too many connections to '{str(key)}'")
        super().__setitem__(key, value)
        super().__setitem__(value, key)

    def __getitem__(self, item):
        # return self.dic[item]
        return super().get(item)

    def __str__(self):
        s2 = set_ls([sorted((k, v)) for k, v in super().items()])
        return f'{{ {", ".join([f"{k}<->{v}" for k,v in s2])} }}'

    def __repr__(self):
        return str(self)

    def __len__(self):
        return dict.__len__(self) // 2


if __name__ == '__main__':
    d1 = ComplDict()
    d1['A'] = 'T'
    # d1['G'] = 'C'
    print(d1['A'])
    print(d1['T'])
    d1['A'] = 'G'
    print(d1['A'])
    print(d1['G'])
    d1['A'] = 'T'
    d1['G'] = 'C'
    print(d1)
    # print(dict(d1).keys())
