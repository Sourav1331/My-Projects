import pikepdf

prev_pdf = pikepdf.open("s.pdf")
perm = pikepdf.Permissions(extract=False)
prev_pdf.save("secured.pdf", encryption=pikepdf.Encryption(user="safe", owner="sourav", allow=perm))
