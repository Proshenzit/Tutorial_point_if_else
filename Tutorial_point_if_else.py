amaount   = 2500
print("amaount",amaount)
if amaount > 10000:
    discount = amaount*20/100
elif amaount > 5000:
    discount  = amaount*10/100
elif amaount>1000:
    discount = amaount*5/100
else:
    discount  = 0
print("payable amount ",amaount-discount)