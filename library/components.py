from selenium.webdriver.support.select import Select
import os, json

def find_element_and_select(driver, by, value, visible_text):
    dropdown = driver.find_element(by, value)
    select = Select(dropdown)
    select.select_by_visible_text(visible_text)

def load_file(filename):
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(current_dir)
    file_path = os.path.join(parent_dir, "testcases/resources", filename)

    with open(file_path) as f:
        data = json.load(f)
    return data

def save_json(data, filename):
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(current_dir)
    file_path = os.path.join(parent_dir, "testcases/resources", filename)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def scroll_to_element(driver, by, value):
    element = driver.find_element(by, value)
    driver.execute_script("arguments[0].scrollIntoView(true);", element)