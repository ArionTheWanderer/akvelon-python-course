import pickle


def write_to_file(filename):
    with open(f'{filename}.txt', 'w') as f:
        i = 0
        user_input = input()
        while user_input != 'quit':
            if i != 0:
                f.write(f'\n')
            f.write(user_input)
            i += 1
            user_input = input()
    with open('metadata.pkl', 'wb') as f:
        metadata = [filename, i]
        pickle.dump(metadata, f)
    with open('metadata.pkl', 'rb') as f:
        loaded_metadata = pickle.load(f)
    with open(f'{filename}.txt', 'r') as f:
        loaded_data = ''
        for line in f:
            loaded_data += line
    print(f'Loaded metadata: {loaded_metadata}')
    print(f'File: \n{loaded_data}')
