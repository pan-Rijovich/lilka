#!/usr/bin/python
#
#       This simple class template engine could be used to generate code 
#   for keiraOS classes
#       It takes files from KEIRA_TEMPLATES_PATH for templates
#   and KEIRA_SOURCE_PATH for output files
#       KEIRA_TEMPLATES_PATH consists from directories, each one
#   of them called a Generator, which store template files to be used
#   to generate output source files.
#       Currently keira_gen supports $NAME$ and $DATE$ macro which will be replaced in 
#   output filename, and template file to produce source.
#   $NAME.lc$ and $NAME.uc$ versions could be used to generate lower cased or upper cased
#   values.
#       Output will be saved in "$KEIRA_TEMPLATES_PATH/Generator" "s/" directory


import os, sys, datetime

# Get templates path from env
templates_path = os.getenv("KEIRA_TEMPLATES_PATH")
source_path = os.getenv("KEIRA_SOURCE_PATH")

if templates_path == None:
    templates_path = "templates"
if source_path == None:
    source_path = ""
date = datetime.datetime.now().ctime()
name = ""
what_to = ""

def apply_macro(in_str:str) -> str:
    out_str = in_str.replace("$NAME.uc$", name.upper())
    out_str = out_str.replace("$NAME.lc$", name.lower())
    out_str = out_str.replace("$NAME$", name)
    out_str = out_str.replace("$DATE$", date)
    return out_str
    
def help():
    print("Usage: keira_gen <generator> <name>\n")
    print("Available generators:")
    what_could_gen = []
    for filename in template_filenames:
        if os.path.isdir(filename):
            what_could_gen.append(filename)
        print("\t{}".format(filename))

if not os.path.isdir(templates_path):
    print ("ERROR: Templates path reffers to non existing {} directory. Exiting...".format(templates_path))
if not os.path.isdir(source_path):
    print ("ERROR: Templates path reffers to non existing {} directory. Exiting...".format(source_path))


template_filenames = os.listdir(templates_path)

if len(sys.argv)< 3:
    print("ERROR: Wrong count of parameters specified.\n")
    help()

elif len(sys.argv) == 3:
    what_to = sys.argv[1]
    name = sys.argv[2]
    path_to_template = templates_path +"/"+what_to
    if not os.path.isdir(path_to_template):
        print("ERROR: Generator {} doesn't exist. ".format(what_to))
        help()
    else:
        for filename in os.listdir(path_to_template):
            new_filename = (source_path+"/"+ what_to+"s/"+apply_macro(filename))
            if (os.path.exists(new_filename)):
                print("ERROR: Can't generate source file cuz it allready exists")
                sys.exit()            
            template_file = open(path_to_template+"/"+filename)
            generated_file = open(new_filename, "w")
            template_file_lines = template_file.readlines()
            generated_file_lines = []

            for line in template_file_lines:
                generated_file_lines.append(apply_macro(line))
            generated_file.writelines(generated_file_lines)
            generated_file.close()
            template_file.close()

