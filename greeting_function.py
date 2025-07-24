def greet(name, greeting="안녕하세요", extra_msg=""):
    msg = f"{greeting}, {name}님!"
    if extra_msg:
        msg += f" {extra_msg}"
    print(msg)

greet("김철수")
greet("John", greeting="Hello")
greet("이영희", extra_msg="좋은 하루 되세요!")