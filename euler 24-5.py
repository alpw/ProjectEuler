dosya = open("sayılarım","w")

nums = "0123456789"
value = ""

def popper(num):
    newStr = ""
    for i in nums:
        if i != num:
            newStr += i
    return num + newStr

def harici(ext):
    the = ""
    for i in nums:
        if i != ext:
            the += i
    return the
theList = []
ct = 0

for i in nums:
    kalan = nums[0:nums.index(i)] + nums[nums.index(i)+1::]
    kalan1 = kalan
    for l in kalan1:
        kalan1 = nums[0:nums.index(l)] + nums[nums.index(l)+1::]
        kalan2 = kalan1
        for k in kalan2:
            kalan2 = nums[0:nums.index(k)] + nums[nums.index(k) + 1::]
            kalan3 = kalan2
            for j in kalan3:
                kalan3 = nums[0:nums.index(j)] + nums[nums.index(j) + 1::]
                kalan4 = kalan3
                for h in kalan4:
                    kalan4 = nums[0:nums.index(j)] + nums[nums.index(j) + 1::]
                    kalan5 = kalan4
                    for g in kalan5:
                        kalan5 = nums[0:nums.index(g)] + nums[nums.index(g) + 1::]
                        kalan6 = kalan5
                        for f in kalan6:
                            kalan6 = nums[0:nums.index(f)] + nums[nums.index(f) + 1::]
                            kalan7 = kalan6
                            for d in kalan7:
                                kalan7 = nums[0:nums.index(d)] + nums[nums.index(d) + 1::]
                                kalan8 = kalan7
                                for s in kalan8:
                                    kalan8 = nums[0:nums.index(s)] + nums[nums.index(s) + 1::]
                                    kalan9 = kalan8
                                    for a in kalan9:
                                        alp = i+l+k+j+h+g+f+d+s+a
                                        print(alp)