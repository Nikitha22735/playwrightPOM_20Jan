import allure
from functools import wraps

class BasePage:
    def __getattribute__(self, name):
        attr = super().__getattribute__(name)
        if callable(attr) and not name.startswith("__"):
            @wraps(attr)
            def wrapper(*args, **kwargs):
                step_name = f"{self.__class__.__name__}.{name}"
                with allure.step(step_name):
                    return attr(*args, **kwargs)
            return wrapper
        return attr