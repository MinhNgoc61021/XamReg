# <del>ExamReg</del> XamReg
Đăng ký dự thi
## Công nghệ sử dụng
- Mẩu thiết kế kiến trúc áp dụng: MVVM
- Container: Docker

| Thành phần  | Miêu tả                                         |
| ----------- | ----------------------------------------------- |
| Client Side | VueJS, Vuex, Buefy, PrintJS, Webpack            |
| Server Side | Flask (Python)                                  |
| Database    | Postgres, SQLAlchemy ORM                        |
## Thành viên nhóm tham gia:
- [Nguyễn Ngọc Minh](https://www.facebook.com/minh.nguyen18121999) (MSSV: 17021300) (Bảo trì)
- [Phạm Công Nam](https://www.facebook.com/nam.pham120799) (MSSV: 17021304)
- [Nguyễn Nam](https://www.facebook.com/NguyenNam12399) (MSSV: 17021306)
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

## Cách cài đặt/Configuration cấu hình

### Theo từng bước
1. Cài đặt Docker Desktop 64 bit
2. Cài đặt Anaconda 2019.10 64 bit và Node.js 64 bit
2. Sau khi cài xong hết, chuyển sang Linux containers (nếu dùng Windows 64 bit)
3. Cài đặt Postgres DB phiên bản 11.6-3 64 bit, cổng mặc định 5432 (Xem cài đặt chi tiết Postgres và pgAdmin 4: [Youtube](https://www.youtube.com/watch?v=e1MwsT5FJRQ))
4. Cài đặt xong, bạn hãy tạo superuser cho Postgres mà bạn sử dụng
### Cài đặt trong api/db/entitydb.py 
Ở create_engine trong mục development hãy thay đổi theo dạng sau
```
postgresql://yourusername:yourpassword@postgres
```
#### Lưu ý:
 - Chuyển env sang development.
 - @postgres ở cuối thực tế sử dụng database image đc tạo ra từ docker-compose, username và password là của superuser bạn tạo ra.
 - Nếu muốn quản lý dữ liệu, bạn nên thay đổi môi trường trong pgAdmin 4 trong docker-compose.yml như sau
    ```
    environment:
          PGADMIN_DEFAULT_EMAIL: postgres@admin.com
          PGADMIN_DEFAULT_PASSWORD: yourpassword
    ```
 - Và tạo thêm một file docker-compose.override.yml ở gốc project với nội dung như trong thư mục docker-compose-config-txt/Minh_Ngoc       có nội dung như sau
   ```
    version: '3'
    # cmd: docker-compose build & docker-compose up (build & run docker)
    services:
      pgAdmin:
        ports:
          - "8070:80"
      postgres:
        ports:
          - "5432:5432"

      api:
        command: python run.py
        environment:
          - QUIZ_ENV=development
        ports:
          - "5000:5000"
      client:
        command: npm run dev
        ports:
          - "8080:8080"
    ```
## Để chạy
Tạo image bằng
```
docker-compose build
```
Và chạy container bằng
```
docker-compose up
```
Sau đó truy cập

 - Đối với Ubuntu/Linux
 ```
 http://0.0.0.0:8080
 ```
 - Đối với Windows
 ```
 http://localhost:8080
 ```
#### Lưu ý
- Flask chạy trên cổng 5000 còn Vue chạy trên cổng 8080.
- Để tạo tài khoản admin, trong init_admin ở run.py có sẵn user để tạo (bạn có thể thay đổi tùy ý).
    
    Truy cập
    ```
    http://localhost:5000/init_admin
    ```
    và sau đó bạn đăng nhập và sử dụng.
