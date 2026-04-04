def is_number(s):
    if s is None:
        return False
    try:
        float(s)
        return True
    except (ValueError, TypeError):
        return False

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = []
            lines = file.readlines()
            keys = lines[0].split(',')

            for i in range(1, len(lines)):
                if lines[i].strip() == "":
                    continue
                data_row = [
                    float(cell.strip('\n')) if is_number(cell.strip('\n')) else cell.strip('\n')
                    for cell in lines[i].split(',')
                ]
                data.append(data_row)
            return data
    except FileNotFoundError:
        raise RuntimeError('File not found.')
    except Exception as e:
        raise RuntimeError(f"An error occurred: {e}")

def write_data_to_file(data, output_file = 'output.csv', seperator=','):
    with open(output_file, 'w') as file:
        for row in data:
            line = seperator.join(map(str, row))
            file.write(line + '\n')

data = read_file('Iris.csv')

for row in data[:10]:
    print(row)

write_data_to_file(data)