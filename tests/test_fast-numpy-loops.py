import numpy as np
import fast_numpy_loops as fn

def test_enable():
    # enable/disable return the previous value
    old = fn.isenabled()
    fn.enable()
    assert fn.isenabled() == True
    fn.disable()
    assert fn.isenabled() == False

    # restore prior state
    if old:
        fn.enable()
    else:
        fn.disable()
    assert fn.isenabled() == old

def test_result(rng):
    print('numpy version', np.__version__)
    print(fn.cpustring())
  
    m = rng.integers(100, size=(10, 10), dtype=np.int32)
    o = np.empty_like(m)
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            o[i, j] = m[i, j] + m[i, j]
    assert np.all(np.add(m, m) == o)

def test_numpy():
    np.test()
