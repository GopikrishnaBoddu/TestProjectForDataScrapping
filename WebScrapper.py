import os


def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating directory")
        os.makedirs(directory)


# create queue and crawled files(if not present)
def create_data_files(projectName,baseUrl):
    queue = projectName + '/queue.txt'
    crawled = projectName + '/crawled.txt'

    if not os.path.isfile(queue):
        write_file(queue,baseUrl)
    if not os.path.isfile(crawled):
        write_file(crawled,'')

def write_file(path,data):
    f = open(path,"w")
    f.write(data)
    f.close()

#Add data on to an exisiting file

def append_to_file(path,data):
    f= open(path,"a")
    f.write(data + '\n')
    f.close()
# Delete the contents of a file

def delete_file_contents(path):
    with open(path,"r") as file:
        pass

#Read a file and convert eachline to set items
def file_to_set(filename):
    results = set()
    with open(filename,"r") as file:
        for line in file:
            results.add(line.replace("\n",''))
    return results
#Iterate through a set,each item will be a new line in the file
def set_to_file(links,file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file,link)







