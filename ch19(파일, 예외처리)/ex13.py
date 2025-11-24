infile = open("ai_image.jpg", "rb")
outfile = open("ai_image_copy.jpg", "wb")

while True:
    copy_buffer = infile.read(1024)
    if not copy_buffer:
        break
    outfile.write(copy_buffer)

infile.close()
outfile.close()