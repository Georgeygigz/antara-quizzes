import hashlib


output_file = open('files/output_file.txt','w')

read_line_hash_value = set()

# the time complexity of implementation below is n(Linear)
with open('files/source_file.txt',"r") as source_file:
    for out_put_line in source_file:
        line_hash_value = hashlib.md5(out_put_line.rstrip().encode('utf-8')).hexdigest()
        if line_hash_value not in read_line_hash_value:
            output_file.write(out_put_line)
            read_line_hash_value.add(line_hash_value)
