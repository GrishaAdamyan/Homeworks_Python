import os
def create_a_testing_work_environment(initial_directory_path):
    path = os.path.join(initial_directory_path, create_a_testing_work_environment.DFD['Dirname'][0])
    os.mkdir(path)
    for i in range(len(create_a_testing_work_environment.DFD['Dirname'])):
        if create_a_testing_work_environment.DFD['Files'][i]:
            for elem in create_a_testing_work_environment.DFD['Files'][i]:
                file = os.path.join(initial_directory_path, elem)
                with open(file, 'w'):
                    pass
        if create_a_testing_work_environment.DFD['Directories'][i]:
            for el in create_a_testing_work_environment.DFD['Directories'][i]:
                directory = os.path.join(initial_directory_path, el)
                os.mkdir(directory)
    
create_a_testing_work_environment.DFD = {
    'Dirname': ['test', 'test/dir_1', 'test/dir_1/dir_3', 'test/dir_1/dir_3/dir_4', 'test/dir_1/dir_3/dir_5',
                'test/dir_2', 'test/dir_2/dir_6', 'test/dir_2/dir_7'],
    'Files': [['test/file_1.txt', 'test/file_2.txt'], ['test/dir_1/file_3.txt', 'test/dir_1/file_4.txt'],
              ['test/dir_1/dir_3/file_5.txt', 'test/dir_1/dir_3/file_6.txt'], ['test/dir_1/dir_3/dir_4/file_7.txt'],
              None, ['test/dir_2/file_8.txt'], ['test/dir_2/dir_6/file_9.txt', 'test/dir_2/dir_6/file_10.txt'],
              ['test/dir_2/dir_7/file_11.txt']],
    'Directories': [['test/dir_1', 'test/dir_2'], ['test/dir_1/dir_3'], ['test/dir_1/dir_3/dir_4', 'test/dir_1/dir_3/dir_5'], 
                    None, None, ['test/dir_2/dir_6', 'test/dir_2/dir_7'], None, None]}

create_a_testing_work_environment('C:/Users/Public')