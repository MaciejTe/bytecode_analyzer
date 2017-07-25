import config as cfg
import os


def create_pyc_file(path):
    res = os.popen("python -m compileall {}".format(path))
    #print res, '***'

# def test(n):
#     [i for i in n]


if __name__ == '__main__':
    # create_pyc_file('examples/comprehension.py')
    import timeit

    t = timeit.Timer("soundex.soundex('Pilgrim')", "import soundex")
    print timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
