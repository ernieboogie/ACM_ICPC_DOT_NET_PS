import math

number_of_place = input("")

number_of_people = raw_input("")
people_list = []
for elem in number_of_people.split(" "):
    people_list.append(int(elem))

director_info = raw_input("")
dir_info =[]
for elem in director_info.split(" "):
    dir_info.append(int(elem))

dir_prime = dir_info[0]
dir_sub = dir_info[1]

number_of_director = 0

for i in range(number_of_place):
    number_of_director = number_of_director + 1
    if people_list[i] > dir_prime:
        number_of_director = number_of_director + math.ceil((people_list[i] - dir_prime) / float(dir_sub))


print int(number_of_director)
