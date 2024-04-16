from city_name import city_adding

def test_city_adding():

    sentence = city_adding("Santiago", "Chile", 500000)
    assert sentence == "Santiago, Chile - 500000"

