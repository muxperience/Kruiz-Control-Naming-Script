from os import listdir
from os.path import isfile, join

def main():
    print(listdir)
    onlyfile = [f for f in listdir() if isfile(join(".", f))]
    #baboo is the filename 
    baboo = ""
    #if you've got bad folder hygiene, you can fix it by adding file types to not look at
    badTypes = ["py", "txt"]
    for f in onlyfile:
        #checks after the last "." to make sure the bad file types are not found
        if f.split(".")[-1] not in badTypes:
            print(f.split(".")[-1])
            f = '"play 50 nowait ' + f + '"'
            print(f)
            baboo = baboo + f + ' '

    t = open("opnames.txt", "w")
    t.write(baboo)
    t.close()
    print(baboo)
    #print(onlyfile)
if __name__ == "__main__":
    main()