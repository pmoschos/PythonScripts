import csv

def read_csv(file_path):
    """
    Reads data from a CSV file.

    :param file_path: Path to the CSV file.
    :return: List of dictionaries, each representing a row in the CSV.
    """
    data = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def write_csv(file_path, data):
    """
    Writes data to a CSV file.

    :param file_path: Path to the CSV file.
    :param data: List of dictionaries to be written to the CSV.
    """
    if not data:
        return

    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def add_contact(data, name, email, phone):
    """
    Adds a new contact to the data.

    :param data: List of current contact records.
    :param name: Name of the contact.
    :param email: Email of the contact.
    :param phone: Phone number of the contact.
    :return: Updated list of contact records.
    """
    new_record = {'name': name, 'email': email, 'phone': phone}
    data.append(new_record)
    return data

# Example Usage
csv_file = 'contacts.csv'
contacts = read_csv(csv_file)

# Adding a new contact (set your contact details here and test the app)
contacts = add_contact(contacts, 'Maria D', 'mariad@gmail.com', '222-111-4444')

# Write the updated contacts back to the CSV
write_csv(csv_file, contacts)
