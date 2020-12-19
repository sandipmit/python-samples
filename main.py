# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import control_flow
import learning_function
import data_structure

def control_flow_examples():
    control_flow.update_list_during_iteration()
    #control_flow.test_range()
    #control_flow.test_break()

def function_examples():
    #learning_function.fib(100)
    #learning_function.default_args('Are feeling OK(Yes/No) ? ')
    #learning_function.lambda_sorting()

    #Testing increment function using lambda
    f = learning_function.lambda_make_increment(10);
    print(f(0))
    print(f(1))

def datastructure_examples():
    #data_structure.list_comprehension_transpose_matrix();
    #data_structure.del_stmt();
    #data_structure.set_operations()
    #data_structure.set_comprehension()
    #data_structure.dictionary_test()
    data_structure.sequence_comparision()

if __name__ == '__main__':
    #control_flow_examples()
    #function_examples()
    datastructure_examples()






