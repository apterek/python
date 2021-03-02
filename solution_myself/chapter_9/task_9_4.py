ignore = ['duplex', 'alias', 'Current configuration ']


def ignore_command(command, ignore):
    ifgnore_status = False
    for word in ignore:
        if word in command:
            ifgnore_status = True
    return ifgnore_status

def convert_config_to_dict(config_filename):
    dict_config = {}

    with open(config_filename) as f:
        for line in f:
            line = line.rstrip()
            if line and not line.startswith('!') or ignore_command(line,ignore): # проверяем существует ли строка, 
                # не начинается ли она на ! или не содержаться в ней слова исключения
                if not line.startswith(' '):# можно проверить так # if line[0].isalnum(): - проверяет начинается ли строка с символа
                    row = line
                    dict_config[row] = []
                else:
                    dict_config[row].append(line.strip()) 
    return dict_config

print(convert_config_to_dict('config_r1.txt'))