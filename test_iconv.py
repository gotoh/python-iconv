import iconv
s=iconv.open("unicodelittle","iso-8859-1")
r=s.iconv(b"Hallo",11,return_unicode=1)
print(repr(r),len(r))

s=iconv.open("iso-8859-1","unicodelittle")
r=s.iconv("Hallo",110)
print(r)
