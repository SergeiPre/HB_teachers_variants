inp_file = open('input-201.txt', 'r')
data = inp_file.read().split()
inp_file.close()
tmp = set(inp_file)
result = [itm for itm in set(inp_file) if data.count(itm) & 1]
out_file = open('input-201.a.txt', 'w')
out_file.write(result[0])
out_file.close()

