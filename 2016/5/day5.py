import hashlib


doorid = "uqwqemis"
index = 400000

password = ""
password2 = [""]*8


while '' in password2:
    hashstring = doorid + str(index)
    h = hashlib.md5()
    h.update(hashstring)
    h = h.hexdigest()
    if h[:5] == "00000":
        password += h[5]
        if not h[5].isalpha() and int(h[5])<8 and password2[int(h[5])] == "":
            password2[int(h[5])] = h[6]

        print "{} : {} : {} : {}".format(hashstring, h, password, "".join(password2))

    index += 1


print password
print password2
