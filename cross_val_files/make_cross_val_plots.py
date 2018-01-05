import numpy as np
import matplotlib.pyplot as plt
import pickle
import glob, os

# take all .dat files and put in a list of files
def create_list_of_files(base_path):

    os.chdir(base_path)
    input_file_list = []

    for cross_file in glob.glob("*.dat"):
        input_file_list.append(cross_file)
    
    return input_file_list

def make_cross_val_plot(file_name, neurons_range, mean_values, std_values, reference):

    plot_titles = {'fa': 'False Alarm', 'mse': 'Mean Squared Error', 'sp': 'SP index', 'det': 'Probability of Detection'}

    plt.figure(figsize=(10,8))    
    plt.title(plot_titles[reference], size= 15)
    plt.errorbar(neurons_range, mean_values, yerr= std_values, ecolor='r', fmt='o--', capsize=5)
    plt.xticks(np.arange(min(neurons_range), max(neurons_range)+1, 1.0), size= 15)
    plt.xlabel('Neurons', size= 15)
    plt.ylabel(plot_titles[reference], size= 15)
    plt.yticks(size= 15)
    plt.grid()
    plt.savefig(ref+'_'+file_name[file_name.find('et'):file_name.find('.dat')]+'.pdf')

base_files_path = '/home/micael/MyWorkspace/MyRinger_dev/cross_val_files/'

list_of_file_names = create_list_of_files(base_files_path)

operations_points = ['OperationPoint_Trigger_SP']
refs = ['fa', 'mse', 'sp', 'det']


for file_name in list_of_file_names:
    input_file = pickle.load(open(file_name,'rb'), encoding= 'latin1')
    neurons = list(input_file['OperationPoint_Trigger_SP'].keys())
    for operation in operations_points:
        for ref in refs:
            mean = []
            std = []
            for key in input_file[operation].keys():
                mean.append(input_file[operation][key][ref][0])
                std.append(input_file[operation][key][ref][1])
            make_cross_val_plot(file_name, neurons, mean, std, ref)


