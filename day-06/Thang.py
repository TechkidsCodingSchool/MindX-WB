

################################################################################
# Show menu
def show_menu():
    print("                      NGUYỄN ĐỨC THẮNG                         ")
    print("          Trung tâm MindX Technology & Startup School          ")
    print("\n\n\n")
    print("THÔNG TIN:")
    print("1. Lí lịch cá nhân.")
    print("2. Mục tiêu nghề nghiệp.")
    print("3. Học vấn.")
    print("4. Kinh nghiệm.")
    print("5. Các kĩ năng.")
    print("6. Mong muốn.")
    print("7. Thoát CV.")


################################################################################
# Get_choice
def get_choice():
    x = 0
    print("     Nhập số thứ tự thông tin bạn muốn biết trong menu trên")
    list = [] 
    while(x<7):
        if(len(list)==6):
            print("              Thank you            ")
            print("       Nhấn phím 7 để thoát CV           ")
        x = (int)(input())
        if x in list:
            print("     Thông tin này đã hiển thị. Mời bạn nhập thông tin khác")
            continue
        else:
            if x==1:
                print(" 1. Lí lịch cá nhân.")
                print("- Ngày sinh: 20/05/2000")
                print("- Giới tính: Nam")
                print("- Điện thoại: 0866508500")
                print("- Email: ducthang.nguyen205@gmail.com")
                print("- Địa chỉ: Tòa nhà Gemek, Lê Trọng Tấn, Hoài Đức, Hà Nội")
                print("- Website: https://www.facebook.com/NTPNDT1920")
                list.append(x)
            if x==2:
                print(" 2. Mục tiêu nghề nghiệp.")
                print("- Trở thành trợ giảng viên của trung tâm MindX Technology & Startup School")
                print("- Gắn bó lâu dài với trung tâm.")    
                list.append(x)                                                                                                                                      																								 
            if x==3:
                print(" 3. Học vấn.")
                print("- Đại học Công Nghệ")
                print("- Khoa : Công nghệ thông tin.")
                print("- Ngành: công nghệ thông tin.")
                print("- GPA kì 1 : 3,75.")
                print("- Điểm trung bình lập trình : 9,6.") 
                list.append(x)                                                                                               
            if x==4:
                print(" 4. Kinh nghiệm")
                print("- Có niềm đam mê lớn đối với công nghệ thông tin.")
                print("- Tham gia giảng dạy gia sư cho học sinh bộ môn Toán - Tin.")    
                list.append(x)                                                                                                                                                                                                        
            if x==5:
                print(" 5. Các kĩ năng.")
                print(" *Lập trình:")
                print("    - Sử dụng thành thạo các ngôn ngữ lập trình C, C++.")
                print("    - Hiện tại đang học ngôn ngữ html và css.")
                print(" *Kĩ năng giao tiếp:")
                print("    - Giao tiếp tốt, hòa đồng, năng động,...")
                print("    - Có trách nhiệm trong công việc.")
                print("    - Luôn nâng cao năng lực và kinh nghiệm của bản thân.")
                print("    - Cố gắng hoàn thành nhiệm vụ được giao.")
                print("    - Ngoài ra còn có một số kĩ năng khác như:")
                print("      thuyết trình, làm việc nhóm, giải quyết vấn đề,...")
                list.append(x)
            if x==6:
                print(" 6. Mong muốn.\n")
                print("- Có được môi trường làm việc tốt để phát triển bản thân.")
                print("- Có thể giải đáp mọi thắc mắc của học viên tại trung tâm.")
                list.append(x)
            if(x<1 or x>7):	
                print("		Nhập lỗi. Vui lòng nhập lại!")
                continue
            if len(list) > 0 and len(list)<6:
                print("     Nhập số thứ tự thông tin bạn muốn biết tiếp theo")  



################################################################################
# Main
def main():
    try:
        show_menu()
        get_choice()
       
    except Exception as exception:
        print('Đã xảy ra lỗi')
        


################################################################################

# Check name of module
if __name__ == '__main__':
    main()