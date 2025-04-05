# t = float(input('Nhập điểm toán'))
# v = float(input('Nhập điểm văn'))
# a = float(input('Nhập điểm anh'))

l = float(input())
s = float(input())
khtn = float(input()) 

# an = float(input())
# mt = float(input())
# tdtt = float(input()) 

def eval(sub1, sub2, sub3): #sub1, sub2, sub3 gọi là tham số truyền vào hàm để tính
    avg = (sub1+sub2+sub3)/3
    if avg > 5:
        danh_gia = 'tren trung binh'
    else:
        danh_gia = 'duoi trung binh'
    return danh_gia

new = eval(l,s,khtn)
print(new)
