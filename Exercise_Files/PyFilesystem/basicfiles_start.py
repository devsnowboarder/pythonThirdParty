# Python Essential Libraries by Joe Marini course example
# Example file for using PyFilesystem

# import the PyFilesystem library
from fs.osfs import OSFS
from fs.zipfs import ZipFS

# TODO: open a local filesystem for the current directory


with OSFS(".") as myfs:
    if(not myfs.exists("testdir")):
        myfs.makedir("testdir")

    with myfs.open("testdir/samplefile.txt",mode='w') as f:
      f.write("This is some text Warrirs are winners ")
    with myfs.open("testdir/samplefile.txt", mode='r') as f:
     content = f.read()
     print(content)

    info = myfs.getinfo("testdir/samplefile.txt",namespaces=['details'])
    print(info.name)
    print(info.is_dir)
    print(info.size)
    print(info.type)
    print(info.modified)


# TODO: try opening and reading a ZIP archive
with ZipFS("FileExamples.zip") as thezip:
    if ( thezip.exists("FileExamples/File1.txt")):
        with thezip.open("FileExamples/File1.txt") as f:
            content = f.read()
            print(content)

