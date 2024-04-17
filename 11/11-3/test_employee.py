from Employee import Employee


def test_give_default_raise():
    jober = Employee("Domantas", "Jokubaitis", 30000)
    jober.give_raise()
    assert jober.salary == 35000

def test_give_custom_raise():
    jober = Employee("Domantas", "Jokubaitis", 30000)
    jober.give_raise(10000)
    assert jober.salary == 40000