from PyPDF2 import PdfWriter
import os
path = "C:\\Users\\soham\\OneDrive\\Desktop\\study\\python\\J_python\\Spdf"
merger = PdfWriter()
pdf = [file for file in os.listdir(path) if file.endswith(".pdf")]
print(pdf)
input1 = open(path+"\\"+pdf[0], "rb")
input2 = open(path+"\\"+pdf[1], "rb")
input3 = open(path+"\\"+pdf[2], "rb")

# add the first 3 pages of input1 document to output
merger.append(fileobj=input1, pages=(0, 1))

# insert the first page of input2 into the output beginning after the second page
merger.merge(position=2, fileobj=input2, pages=(0, 1))

# append entire input3 document to the end of the output document
merger.append(input3)

# Write to an output PDF document
output = open(path+"\\"+"document-output.pdf", "wb")
merger.write(output)


# Close File Descriptors
merger.close()
output.close()