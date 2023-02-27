'''
Following class implement a fils system that avoid to write the same content to different files such that the storage
will be saved and efficiently used.

'''


import hashlib

class FS(object):

    def __init__(self, folder):
        self.dir=folder
        self.content_cache={}
        self.file_cache={}


    def store(self, fname, content):
        c_hash=hashlib.md5(content.encode('UTF-8')).hexdigest()#without calling hexdigest(), different hashes returned.
        if c_hash in self.content_cache:
            self.content_cache[c_hash].append(fname)
            self.file_cache[fname]=c_hash
        else:
            with open(self.dir+'/'+fname, 'w') as f:
                f.write(content)
            self.content_cache[c_hash]=[fname]
            self.file_cache[fname]=c_hash


    def get(self,fname):
        print ("fname: ", fname, "file_cache= ", self.file_cache)
        if fname not in self.file_cache:
            return None
        c_hash=self.file_cache[fname]
        existing_fname=self.content_cache[c_hash][0]
        with open(self.dir+'/'+existing_fname, 'r') as f:
            content=f.read()
            return content


o=FS(".")
o.store("Tian321.txt", "This is a test file!")
o.store("Tian322.txt", "This is a test file!")
o.store("Tian323.txt", "This is a test file!")
o.store("Tian325.txt", "This is a test file!")
print ("get file content.",o.get("Tian320.txt"))

print ("get file content.",o.get("Tian325.txt"))


