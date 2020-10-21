#
# copy-to-modify
#

def replace_item(items, index, new_value):
    items[index] = new_value
    return items

#

def replace_item(items, index, new_value):
    return items[:index] + [new_value] + items[index + 1:]


#
# replace loop with generator
#

def get_lengthsa(values):
    lengths = []
    for value in values:
        lengths.append(len(value))
    return lengths

#

def get_lengthsb(values):
    return (len(value) for value in values)


#
# class method moved to module level
#

class FileParser():
    def text_to_rows(self):
        return csv.reader(line for line in self.text.splitlines() if line)

#

def text_to_rows(text):
    return csv.reader(line for line in text.splitlines() if line)


#
# replace statement with expression
#

def decompress(content):
    archive = ZipFile(BytesIO(content))
    file = archive.namelist()[0]
    with open(file, 'rb') as fin:
        return fin.read()

#

def decompress(content):
    return first_file_from_archive(zipfile.ZipFile(io.BytesIO(content)))

def first_file_from_archive(archive):
    return archive.read(archive.namelist()[0])


#
# decompose function
#

def iterate_file(self):
    with open(self._filename, 'rb') as fin:
        content = fin.read()
        if self.decompress:
            content = self.decompress(content)
        content = content.decode('utf-8')
        for row in self._text_to_rows(content):
            yield row

#

def iterate_file(filename):
    with open(filename, 'rb') as fin:
        yield from execute_pipeline(build_pipeline(filename), fin)

def build_pipeline(filename):
    return ( <... generator that produces callables> )

def execute_pipeline(pipeline, fin):
    return functools.reduce(lambda content, stage: stage(content), pipeline, fin.read())


#
# replace object method with generic callback
#

class Thing():
    def

