print('Nhap mot trong so cac thong tin duoi day de biet them ve toi')
print(' 1.Name')
print(' 2.Information')
print(' 3.Goal')
print(' 4.Knowledge')
print(' 5.Experience')
print(' 6.Skill')
print(' 7.Feeling')
print('Neu khong can tim hieu nua, hay nhap Quit')


def test(s):
    if(s=='Name'):
        print('NGUYEN HONG LINH')
    if(s=='Information'):
        print('Ngay sinh: 07/10/2000')
        print('Dien thoai: 0334189040')
        print('Mail: nguyenlinhtta@gmail.com')
        print('Gioi tinh: Nu')
        print('Dia chi: So nha 19 Viet Duc, Ngoa Long, Tu Liem, Ha Noi')
    if(s=='Goal'):
        print('-Hoan thanh tot nhiem vu duoc giao.')
        print('-Tham gia tich cuc cac hoat dong cua trung tam.')
        print('-Ho tro, giai dap moi thac mac, giup do het suc de hoc vien co the tiep thu tot dieu duoc hoc.')
        print('-Co the tro thanh mot thanh lau dai o MindX Technology & Startup School.')
    if(s=='Knowledge'):
        print('- Dai hoc Cong Nghe-Dai hoc Quoc gia Ha Noi')
        print('  Nganh: Cong nghe thong tin')
        print('- GPA ki I: 3.58')
        print('- Trong tat ca cac nam truoc day deu dat hoc sinh gioi')
    if(s=='Experience'):
        print('Chua co kinh nghiem trong nhung cong viec lien quan den giang day.')
    if(s=='Skill'):
        print('- Nam chac ngon ngu C va C++.')
        print('- Co kinh nghiem trong viec day cac ban on thi.')
        print('- Hoa dong, nhiet tinh trong moi viec, biet lang nghe moi nguoi.')
        print('- Thau hieu tam li tre con.')
        print('- Luon tim toi va tiep thu tot nhung cai moi.')
        print('- No luc het minh vi cong viec.')
    if(s=='Feeling'):
        print('Toi rat thich cong viec tro giang o trung tam MindX technology & Startup School. Trung tam la mot moi truong chuyen nghiep de moi nguoi the hien minh va la noi rat thich hop de toi theo duoi va song voi dam me.')
        print('Toi yeu lap trinh, vi vay toi muon giup cac ban hoc sinh tim thay su hap dan cua mon hoc nay, tiep can no de dang hon va truyen duoc ngon lua yeu lap trinh cho cac ban ay.')
        print('Hon nua, cong viec nay cung lien quan den nhung thu toi dang hoc, toi hi vong qua viec tro giang, duoc tiep xuc voi moi nguoi, tham gia cac su kien cua trung tam se giup toi nang cao trinh do va tam hieu biet cua minh. Toi se luon co gang tim toi, tiep thu, hoc hoi cai moi, nang cao kha nang lap trinh va trinh do tieng anh cua ban than de lam viec hieu qua hon.')
   
    
choise=['Name','Information','Goal','Skill','Experience','Knowledge','Feeling']
s=input('Thong tin ban muon biet:')
while s!='Quit':
    if s in choise:
        test(s)
    else:
        print('Ban da nhap sai')
    s=input('Thong tin ban muon biet:')
        
print('   (^.^) THANKYOU (.)')