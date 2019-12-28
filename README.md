# ̶<del>ExamReg</del> XamReg
Đăng ký dự thi
## Công nghệ sử dụng
- Mẩu thiết kế kiến trúc áp dụng: MVVM
- Container: Docker

| Thành phần  | Miêu tả                                         |
| ----------- | ----------------------------------------------- |
| Client Side | VueJS, Vuex, Buefy, PrintJS, Webpack            |
| Server Side | Flask (Python)                                  |
| Database    | MySQL, SQLAlchemy ORM, phpMyAdmin               |
## Thành viên nhóm tham gia:
- Nguyễn Ngọc Minh
- Phạm Công Nam
- Nguyễn Nam
## Thực hiện
- Thực hiện theo nhóm (team) 3 sinh viên.
- Trình bày sản phẩm tại buổi thi vấn đáp.
## Tiêu chí chấm điểm
TT. Tiêu chí chấm điểm Hệ số
1. Chức năng và các features đã cài đặt 0.35
2. Thiết kế: Logic, dễ sử dụng, đẹp 0.15
3. Xử lý nhập liệu: Kiểm tra hợp thức, tự động điền, gợi ý, chuyển đổi, ... 0.05
4. Xử lý phiên, xác thực, an ninh 0.05
5. Viết lại và/hoặc định tuyến URL 0.1
6. Hiệu năng: sử dụng ajax để tải bộ phận, không tải lại, dữ liệu JSON... 0.1
7. Phong cách lập trình: Sử dụng mẫu thiết kế, tách biệt mã tạo giao diện và mã xử lý nghiệp vụ, tổ chức thư viện, lớp và kế thừa lớp, mô hình MVC, trình bày mã, chú thích mã, ... 0.1
8. Thao tác CSDL theo lập trình hướng đối và độc lập CSDL 0.1

## Mô tả chung
Trường đại học ABC (ABCUni) tổ chức thi kết thúc học phần bằng hình thức thi trắc nghiệm trên máy tính. Để tạo điều kiện tốt nhất cho thí sinh, ABCUni cho phép sinh viên tự đăng ký dự thi. Theo đó, ABCUni sẽ lập lịch cho các kỳ thi và ca thi trước, sinh viên đã học học phần nào sẽ được quyền đăng ký dự thi học phần đó tại ca thi phù hợp. Mỗi kỳ thi có nhiều ca thi. Mỗi ca thi có nhiều phòng thi. Mỗi phòng thi có số lượng máy tính xác định. Số lượng thí sinh có thể thi cùng ca thi bị giới hạn, không được vượt quá tổng số máy tính của các phòng thi trong ca thi. Khi ca thi đã đủ số lượng thí sinh đăng ký thì các thí sinh khác không thể đăng ký vào ca thi nữa.

Sinh viên đăng nhập vào phần mềm ExamReg mà ở đó đã có thông tin cá nhân sinh viên (do quản trị viên đưa vào CSDL trên cơ sở danh sách lớp học phần được các đơn vị đào tạo gửi) và CHỌN lịch thi của học phần sinh viên cần đăng ký dự thi. Trong lịch thi đó có thông tin điểm thi, các ca thi, các phòng thi của ca thi, số chỗ thi và có chức năng cho sinh viên chọn ca thi họ muốn dự thi. Sau khi sinh viên chọn xong thì lịch thi sinh viên đăng ký được xuất ra ở dạng báo cáo có tên gọi là PHIẾU BÁO DỰ THI và sinh viên download được/in được. Bản in, bản download đều có giá trị là minh chứng cho việc sinh viên đăng ký dự thi thành công. SV sử dụng phiếu báo dự thi này để đi thi.

## Quy trình nghiệp vụ
Hệ thống có 2 vai trò sử dụng: quản trị viên, sinh viên.
- Quản trị viên quản lý danh sách môn thi/học phần
- Quản trị viên quản lý danh sách sinh viên, cấp tài khoản cho sinh viên (từ Excel).
- Quản trị viên nhập danh sách sinh viên đã học từng môn thi (đủ điều kiện dự thi) (từ Excel).
- Quản trị viên nhập danh sách sinh viên không đủ điều kiện dự thi (từ Excel).
- Quản trị viên tạo kỳ thi, thêm các ca thi cho kỳ thi, thêm các phòng thi (phòng máy) cho ca thi, lập lịch (ngày thi, giờ bắt đầu, giờ kết thúc) cho các ca thi, xác định môn thi cho từng ca thi.
- Sinh viên đăng ký ca thi mà sinh viên đủ điều kiện dự thi và đang còn chỗ trống (chưa đủ số lượng đăng ký theo số máy).
- Sinh viên download/in phiếu báo dự thi sau khi đăng ký thành công.
- Quản trị viên in danh sách thí sinh dự thi theo từng phòng thi của các ca thi.
