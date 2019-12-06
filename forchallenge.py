ipAddress = '12.9.34.6.12.90'
cleanedNumber = ''
segments = []

for char in ipAddress:
    if char == '.' and cleanedNumber != '':
        segments.append(cleanedNumber)
        cleanedNumber = ''
    elif char != '.':
        cleanedNumber += char

if cleanedNumber != '':
    segments.append(cleanedNumber)

print("There are {0} segments in the input".format(len(segments)))

if segments:
    print("The length of the segments are: ")
    for segment in segments:
        print(len(segment), end='\t')
