#
# copy-to-modify
#

def replace_item(items, index, replace):
    items[index] = replace
    return items  # why even bother?

#

def replace_item(items, index, replace):
    return (
        replace if i == index else item
        for i, item in enumerate(items)
    )


#
# replace statement with expression
#

def decompress(content):
    archive = ZipFile(BytesIO(content))
    first_file = archive.namelist()[0]
    return archive.read(first_file)

#

def decompress(content):
    return first_file_from_archive(
        zipfile.ZipFile(io.BytesIO(content))
    )

def first_file_from_archive(archive):
    return archive.read(archive.namelist()[0])


#
# replace loop with generator
#

def get_lengths(values):
    lengths = []
    for value in values:
        lengths.append(len(value))
    return lengths

#

def get_lengths(values):
    return (len(value) for value in values)


#
# move class method to module
#

class FileParser():
    def text_to_rows(self):
        return csv.reader(
            line for line in self.text.splitlines() if line
        )

#

def text_to_rows(text):
    return csv.reader(
        line for line in text.splitlines() if line
    )


#
# decompose function
#

def iterate_file(filename):
    with open(filename, 'rb') as fin:
        content = fin.read()
        if filename.split('.')[-1] == 'zip':
            content = decompress(content)
        content = content.decode('utf-8')
        for row in text_to_rows(content):
            yield row

#

def iterate_file(filename):
    with open(filename, 'rb') as fin:
        yield from execute_pipeline(
            build_pipeline(filename),
            fin,
        )

def build_pipeline(filename):
    return ( <... generator that produces callables> )

def execute_pipeline(pipeline, fin):
    return functools.reduce(
        lambda content, stage: stage(content),
        pipeline,
        fin.read(),
    )


#
# deprecate class
#

class OldClass():
    pass

#

# sorry, the class serves no purpose now


#
# replace object method with generic callback
#

class Thing():
    def

