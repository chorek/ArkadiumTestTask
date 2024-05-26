import importlib.util
import os

class button:
    def __init__(self, obj_name, obj):
        self.name = obj_name
        self.obj = obj

    def ATclick(self):
        self.obj.click()
        assert self.obj, "The " + self.name + " not clicked!"
        print("The " + self.name  + " clicked.")

class object:
    def __init__(self, obj_name, obj):
        self.name = obj_name
        self.obj = obj

    def ATclick(self):
        self.obj.click()
        assert self.obj, "The " + self.name + " not clicked!"
        print("The " + self.name  + " clicked.")

def scroll_to_element(element, driver):
    js_code = "arguments[0].scrollIntoView();"
    assert element.obj, "No element to scroll to!"
    driver.execute_script(js_code, element.obj)
    print("Scrolled to " + element.name + " successfully.")

def take_screenshot(test_name, file_name, driver):
    file_path = os.path.join(os.path.dirname(__file__), "..", "Results", test_name, file_name + ".png")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    driver.save_screenshot(file_path)
    print("Screenshot taken and saved to " + file_path)

class DynamicImporter:
    def __init__(self, directory):
        self.directory = directory
        self.modules = {}

    def import_modules(self):
        for filename in os.listdir(self.directory):
            if filename.endswith(".py"):
                module_name = filename[:-3]
                self.modules[module_name] = self._import_module(module_name)
                print(f"Module '{module_name}' imported successfully.")

    def _import_module(self, module_name):
        module_path = os.path.join(self.directory, f"{module_name}.py")

        spec = importlib.util.spec_from_file_location(module_name, module_path)

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        return module

    def get_class(self, module_name, class_name):
        module = self.modules.get(module_name)
        if not module:
            raise ImportError(f"Module '{module_name}' not found")

        cls = getattr(module, class_name, None)
        if not cls:
            raise ImportError(f"Class '{class_name}' not found in module '{module_name}'")

        return cls