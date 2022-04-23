from Car import Car


def test_car_accelerate():
    car = Car(5)
    car.speed()
    assert car.speed == 10
