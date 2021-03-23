my_sample_list = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

my_sample_list[1] = 'Steven'
my_sample_list[len(my_sample_list)-1] = 'Pepe'
my_sample_list[0] = my_sample_list[2] + my_sample_list[4]

for i in reversed(my_sample_list):
    print(i)