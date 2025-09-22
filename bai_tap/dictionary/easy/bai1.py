# **Bài 1: Tạo Dictionary và truy cập giá trị**

# - **Mô tả:** Tạo một dictionary lưu trữ thông tin của một người với các key `"ten"`, `"tuoi"`, `"thanh_pho"`. Sau đó, in ra tên và thành phố của người đó.
# - **Input:** Không có (tạo dictionary cố định trong code).
# - **Output:**
    
#     `Tên: [Tên người]
#     Thành phố: [Thành phố]`
    
# - **Ví dụ:**
    
#     **Python**
    
#     `# Input (trong code):
#     # thong_tin_nguoi = {"ten": "An", "tuoi": 25, "thanh_pho": "Hà Nội"}
    
#     # Output:
#     # Tên: An
#     # Thành phố: Hà Nội
info={
    'ten' : 'An',
    'tuoi' : 25,
    'thanh_pho' : 'Hà Nội'
}
print(info.get('ten') )
print(info.get('thanh_pho') )