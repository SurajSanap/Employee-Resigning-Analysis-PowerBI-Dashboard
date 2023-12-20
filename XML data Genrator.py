import xml.etree.ElementTree as ET
import random
from faker import Faker

fake = Faker()

departments = ['Marketing', 'IT', 'Finance', 'HR', 'Sales', 'Engineering']

reasons_list = [
    'Needing more of a challenge',
    'Looking for a higher salary',
    'Wanting a different work environment',
    'Feeling uninspired',
    'Wanting to feel valued'
]

def generate_reason():
    return {
        'category': 'Work',
        'details': random.choice(reasons_list)
    }

def generate_employee_data():
    return {
        'id': str(fake.unique.random_number(6)),
        'name': fake.name(),
        'department': random.choice(departments),
        'resignation_date': fake.date_this_decade(),
        'reason': generate_reason()
    }

def generate_xml_data(num_employees):
    root = ET.Element('resignation_data')
    for _ in range(num_employees):
        employee_data = generate_employee_data()
        employee_element = ET.SubElement(root, 'employee')

        for key, value in employee_data.items():
            if key == 'reason':
                reason_element = ET.SubElement(employee_element, key)
                sub_key = ET.SubElement(reason_element, 'category')
                sub_key.text = value['category']
                sub_value = ET.SubElement(reason_element, 'details')
                sub_value.text = value['details']
            else:
                element = ET.SubElement(employee_element, key)
                element.text = str(value)

    return root

def save_to_xml(element_tree, file_path):
    tree = ET.ElementTree(element_tree)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    num_employees = 300
    xml_data = generate_xml_data(num_employees)
    save_to_xml(xml_data, 'resignation3.xml')
