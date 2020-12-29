# Python Essential Libraries by Joe Marini course example
# Example file for using the File System walker

from fs.osfs import OSFS
from fs.zipfs import ZipFS

# create a basic file walker
#with OSFS(".") as myfs:
   # print("-- Files --")
    # TODO: use the files walker to process files
    #for path in myfs.walk.files(filter=["*.txt"]):
     #   print(path)

   # print("-- Directories --")
    # TODO: use the dirs walker for directories
   # for path in myfs.walk.dirs():
    #    print(path)
#
# TODO: use the info property to step through items
with OSFS(".") as myfs:
    for path,info in myfs.walk.info(namespaces=["details"]):
        print(path,info.is_dir, info.size)


# TODO: Use the walk object by itself:

# TODO: Use the walker with a ZIP
