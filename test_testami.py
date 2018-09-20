def funzione(x):
    return x + 2

# The test function that Travis CI will read
def test_funzione():
    assert funzione(3) == 5
    #change to: assert funzione(4) == 5
