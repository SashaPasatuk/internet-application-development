
from lab_pyton_oop.rectangle import rectangle
from lab_pyton_oop.circle import circle
from lab_pyton_oop.square import square

if __name__ == "__main__":
    r = rectangle("синего", 17, 17)
    c = circle("зеленого", 17)
    s = square("красного", 17)
    print(r.__repr__())
    print(c.__repr__())
    print(s.__repr__())
    