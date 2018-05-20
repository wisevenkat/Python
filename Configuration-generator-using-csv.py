import csv
import jinja2
import os

template_file = "switch.j2"
dict_list = []
output_directory = "config"


# 1. read the contents from the CSV file configuration parameter convert to dictionary

print("Convert CSV file to dictionaries...")

reader = csv.DictReader(open('Parameter.csv', 'rt'))

for line in reader:
    dict_list.append(line)

# 2. next we need to create the central Jinja2 environment and we will load
# the Jinja2 template file

print("Creating Jinja2 environment...")
env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="."))
template = env.get_template(template_file)

# 3.we will make sure that the output directory exists

if not os.path.exists(output_directory):
       os.mkdir(output_directory)

# 4. now create the templates
print("Creating configuration file...")
for parameter in dict_list:
          result = template.render(parameter)
          f = open(os.path.join(output_directory, parameter['hostname'] + ".config"), "w")
          f.write(result)
          f.close()
          print("Configuration '%s' created..." % (parameter['hostname'] + ".config"))
          print("DONE")


