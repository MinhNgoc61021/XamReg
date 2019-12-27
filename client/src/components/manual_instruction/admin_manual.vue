
<template>
    <div class="container">
      <h1 class="title is-3">Trợ giúp</h1>
      <h2 class="subtitle is-6">Hướng dẫn sử dụng về phần mềm ExamReg cho quản trị viên (Admin) </h2>
      <hr>
        <!-- Đăng nhập-->
        <b-collapse :open="true" aria-id="contentIdForA11y1">
            <div class = "header1"
                slot="trigger"
                aria-controls="login-manual"><b>1. Đăng nhập</b></div>
            <div class="notification">
                <div class="content">
                    <p>
                      • Đối với Quản trị viên sẽ được cấp và thông báo tài khoản đăng nhập.
                    </p>
                </div>
            </div>
        </b-collapse>
        <!-- Đối với Quản trị viên (Admin) -->
        <b-collapse :open="false" aria-id="contentIdForA11y1">
            <div class = "header1"
                slot="trigger"
                aria-controls="admin-page-manual"><b>2. Đối với Quản trị viên (Admin)</b>
            </div>
            <div style="padding-left: 15px;">
              <b-collapse :open="false" aria-id="contentIdForA11y1">
                <div class = "header1"
                    slot="trigger"
                    aria-controls="student-management-manual"><i>2.1. Quản lí sinh viên</i>
                </div>
                <div style="padding-left: 15px;">
                  <b-collapse :open="false" aria-id="contentIdForA11y1">
                    <div class = "header1"
                        slot="trigger"
                        aria-controls="student-management-manual"><i>2.1.1. Import danh sách sinh viên tại tab Nhập bằng Excel</i></div>
                    <div class="notification">
                      <div class="content">
                        <!--add anh Import danh sách sinh viên-->
                                • Quản trị viên có thể upload 1 trong các <b>format file excel (.xlsx)</b>:
                                  <p style="padding-left: 30px;">
                                    ◦ <u>Loại 1</u>: File excel <b>Danh sách thông tin sinh viên</b> bao gồm các cột: <b> <br>Mã số sinh viên (VD: 17021000) <br>- Tên sinh viên (VD: Phạm Ngọc H) <br> Ngày sinh (VD: 2000/01/01) <br> Giới tính (VD: Nam) <br> Mã khóa học (VD: K61CACLC) của sinh viên.</b> <br>
                                    <img :src="'/static/img/manual_pics/Input_format/Excel_format_01.png'" style="margin: 10px;" alt="Loại 1"><br>
                                    ◦ <u>Loại 2</u>: File excel <b>Danh sách sinh viên đủ điều kiện và không đủ điều kiện tham gia kì thi học phần </b> bao gồm các cột:<br> <b>Mã số sinh viên <br> Mã số môn thi (VD: INT1005) <br> Tên môn học <br> Thông tin sinh viên (Đủ điều kiện/Không đủ điều kiện)</b>. <br>
                                    <img :src="'/static/img/manual_pics/Input_format/Excel_format_02.png'" style="margin: 10px;" alt="Loại 2"><br>
                                    ◦ <u>Loại 3</u>: File excel tổng hợp của của ca hai file trên bao gồm các cột: <br> <b>Mã số sinh viên <br> Tên sinh viên <br> Ngày sinh <br> Giới tính <br> Mã khóa học của sinh viên <br> Mã số môn thi <br> Tên môn học và thông tin sinh viên (Đủ điều kiện/Không đủ điều kiện)</b>. <br>
                                    <img :src="'/static/img/manual_pics/Input_format/Excel_format_03.png'" style="margin: 10px;" alt="Loại 3">
                                  </p>
                        <p><b-icon pack="fas" icon="exclamation-triangle" size="is-small"></b-icon><strong style="color: red"> Chú ý:</strong> Yêu cầu file excel phải nhập đúng thứ tự các cột như trên, đặc biệt file <b>Danh sách thông tin sinh viên</b> chỉ bao gồm danh sách các sinh viên đã có tài khoản trên hệ thống.</p>
                      </div>
                    </div>
                </b-collapse>

                  <b-collapse :open="false" aria-id="contentIdForA11y1">
                      <div class = "header1"
                          slot="trigger"
                          aria-controls="student-management-manual"><i>2.1.2. Thêm từng thông tin về sinh viên thông qua form</i>
                      </div>
                      <div class="notification">
                          <div class="content">
                             <!--add anh form thêm từng thông tin về sinh viên-->
                              <p>• Quản trị viên có thể nhập tài khoản sinh viên bằng form bao gồm: <br>
                                <b>Mã số sinh viên (VD: 17021000) <br>
                                    Tên sinh viên (VD: Phạm Ngọc H) <br>
                                    Ngày sinh (VD: 2000/01/01) <br>
                                    Giới tính (VD: Nam) <br>
                                    Mã khóa học (VD: K61CACLC) của sinh viên.</b> <br></p>
                          </div>
                      </div>
                  </b-collapse>

                  <b-collapse :open="false" aria-id="contentIdForA11y1">
                      <div class = "header1"
                          slot="trigger"
                          aria-controls="student-management-manual"><i>2.1.3. Xem danh sách sinh viên tại tab Xem & Chỉnh sửa danh sách sinh viên cung cấp các chức năng:</i>
                      </div>
                      <div class="notification">
                          <div class="content">
                             <!--add anh form thêm từng thông tin về sinh viên-->
                                    • Nhấn vào nút <b-icon pack="fas" icon="edit" size="is-small"></b-icon> để chỉnh sửa thông tin của sinh viên.<br>
                                    • Nhấn vào nút <b-icon pack="fas" icon="trash" size="is-small"></b-icon> để xóa thông tin của sinh viên đó khỏi bảng.<br>
                                    • Quản trị viên nhập Mã số sinh viên tại thanh tìm kiếm <b-input placeholder="Tìm kiếm bằng mã số sinh viên" icon-pack="fas" icon="search"></b-input> để tìm kiếm thông tin của sinh viên mong muốn.<br>
                                    • Nhấn vào thanh <b-button icon-right="chevron-down"><span>5 dòng/trang</span></b-button> để hiển thị số danh sách sinh viên tùy ý trên một trang.<br>
                                    • Nhấn vào nút  <b-button><b-icon size="is-small" icon="sync"/><span>Làm mới</span></b-button> để tải lại bảng.<br>
                                    • Nhấn vào nút <b-icon pack="fas" icon="chevron-right" size="is-small"></b-icon> đầu mỗi hàng để xem thông tin chi tiết về các môn học của sinh viên bao gồm:
                                    <p style="padding-left: 30px;">
                                          ◦ Danh sách môn thi sinh viên đủ điều kiện thi<br>
                                          ◦ Danh sách môn thi sinh viên không đủ điều kiện thi<br>
                                    </p>
                                    • Nhấn vào mũi tên <b-icon pack="fas" icon="arrow-up" size="is-small"></b-icon> hoặc <b-icon pack="fas" icon="arrow-down" size="is-small"></b-icon> tại tên cột để sắp xếp lại theo thứ tự tăng dần hoặc giảm dần.<br>
                          </div>
                      </div>
                  </b-collapse>
                </div>
            </b-collapse>

              <b-collapse :open="false" aria-id="contentIdForA11y1">
                <div class = "header1"
                        slot="trigger"
                        aria-controls="subject-management-manual"><i>2.2. Quản lí môn thi</i>
                </div>
                <div class="notification">
                    <div class="content">
    <!--                    add anh register-->
                        Quản trị viên xem danh sách các môn thi tại tab Quản lí môn thi: <br>
                          <p style="padding-left: 30px;">
                          • Nhấn vào nút <b-button icon-pack="fas" icon-left="plus-square"><span>Tạo môn</span></b-button> để nhập các thông tin về môn học muốn thêm vào danh sách.<br>
                          • Nhấn vào nút <b-icon pack="fas" icon="edit" size="is-small"></b-icon> để chỉnh sửa thông tin của môn học.<br>
                          • Nhấn vào nút <b-icon pack="fas" icon="trash" size="is-small"></b-icon> để xóa thông tin của môn học đó khỏi bảng.<br>
                          • Nhấn vào thanh <b-button icon-right="chevron-down"><span>5 dòng/trang</span></b-button> để hiển thị số danh sách môn học tùy ý trên một trang.<br>
                          • Nhấn vào nút <b-button><b-icon size="is-small" icon="sync"/><span>Làm mới</span></b-button> để tải lại bảng.<br>
                          • Nhấn vào mũi tên <b-icon pack="fas" icon="arrow-up" size="is-small"></b-icon> hoặc <b-icon pack="fas" icon="arrow-down" size="is-small"></b-icon> tại tên cột để sắp xếp lại theo thứ tự tăng dần hoặc giảm dần.<br>
                          • Quản trị viên nhập Mã số môn thi tại thanh tìm kiếm <b-input placeholder="Tìm kiếm bằng Mã số môn thi" icon-pack="fas" icon="search"></b-input> để tìm kiếm thông tin của môn học mong muốn.<br>
                          </p>
                    </div>
                </div>
              </b-collapse>

              <b-collapse :open="false" aria-id="contentIdForA11y1">
                <div class = "header1"
                        slot="trigger"
                        aria-controls="room-management-manual"><i>2.3. Quản lí phòng thi</i>
                </div>
                <div class="notification">
                    <div class="content">
    <!--                    add anh register-->
                        Quản trị viên xem danh sách các phòng thi tại tab Quản lí phòng thi: <br>
                          <p style="padding-left: 30px;">
                          • Nhấn vào nút <b-button icon-pack="fas" icon-left="plus-square"><span>Tạo phòng thi</span></b-button> để nhập các thông tin về môn học muốn thêm vào danh sách.<br>
                          • Nhấn vào nút <b-icon pack="fas" icon="edit" size="is-small"></b-icon> để chỉnh sửa thông tin của môn học.<br>
                          • Nhấn vào nút <b-icon pack="fas" icon="trash" size="is-small"></b-icon> để xóa thông tin của môn học đó khỏi bảng.<br>
                          • Nhấn vào thanh <b-button icon-right="chevron-down"><span>5 dòng/trang</span></b-button> để hiển thị số danh sách môn học tùy ý trên một trang.<br>
                          • Nhấn vào nút <b-button><b-icon size="is-small" icon="sync"/><span>Làm mới</span></b-button> để tải lại bảng.<br>
                          • Nhấn vào mũi tên <b-icon pack="fas" icon="arrow-up" size="is-small"></b-icon> hoặc <b-icon pack="fas" icon="arrow-down" size="is-small"></b-icon> tại tên cột để sắp xếp lại theo thứ tự tăng dần hoặc giảm dần.<br>
                          • Quản trị viên nhập Tên phòng thi tại thanh tìm kiếm <b-input placeholder="Tìm kiếm bằng tên phòng" icon-pack="fas" icon="search"></b-input> để tìm kiếm thông tin của môn học mong muốn.<br>
                          </p>
                    </div>
                </div>
              </b-collapse>

              <b-collapse :open="false" aria-id="contentIdForA11y1">
                <div class = "header1"
                        slot="trigger"
                        aria-controls="log-management-manual"><i>2.4. Quản lí lịch thi</i>
                </div>
                <div class="notification">
                    <div class="content">
                      Quản trị viên xem danh sách các phòng thi tại tab Quản lí lịch thi: <br>
                      <p>
                            <b-icon pack="fas" icon="exclamation-triangle" size="is-small"></b-icon>
                            <strong style="color: red">Chú ý</strong>:
                        Chức năng Quản lý lịch thi chỉ <b>tổng hợp</b> lại những dữ liệu về môn thi, phòng thi và sinh viên từ những chức năng khác,
                        mọi thay đổi về những dữ liệu nói trên cần được thực hiện ở những chức năng tương ứng.
                      </p>
                      <span style="padding-left: 30px;">
                      • Nhấn vào nút <b-button icon-pack="fas" icon-left="plus-square"><span>Tạo kỳ thi</span></b-button> để bắt đầu một kỳ thi mới (một kỳ thi gồm nhiều ca thi).<br>
                      • Nhấn vào tiêu đề của kỳ thi để xem thông tin chi tiết những ca thi
                      • Nhấn vào nút <b-icon pack="fas" icon="edit" size="is-small"></b-icon> để sửa trạng thái kỳ thi (sinh viên chỉ có thể đăng ký kỳ thi ở trạng thái "Mở đăng ký").<br>
                      • Nhấn vào nút <b-icon pack="fas" icon="trash" size="is-small"></b-icon> để xóa kỳ thi.<br>
                      • Nhấn vào nút <b-button><b-icon size="is-small" icon="sync"/><span>Làm mới</span></b-button> để tải lại trang.<br>
                      • Phòng thi có thể được chọn trực tiếp từ đề xuất của thanh tìm kiếm.
                      • Chọn tab "Xem & In danh sách sinh viên dự thi" để xem và in danh sách sinh viên. <br>
                        <p>
                            <b-icon pack="fas" icon="exclamation-triangle" size="is-small"></b-icon>
                            <strong style="color: red">Chú ý</strong>:
                        Chức năng "Xem & In danh sách sinh viên dự thi" xuất ra danh sách sinh viên theo <b> phòng thi</b>.
                          <img src="../../../static/img/manual_pics/print_student_list.png" alt="Chú ý"/>
                        </p>
                      • Định dạng của danh sách sinh viên như sau: <br>
                      <img :src="'/static/img/manual_pics/student_list.png'" alt=""/>
                      </span>
                </div>
                </div>
              </b-collapse>

              <b-collapse :open="false" aria-id="contentIdForA11y1">
                <div class = "header1"
                        slot="trigger"
                        aria-controls="log-management-manual"><i>2.5. Quản lí nhật ký</i>
                </div>
                <div class="notification">
                    <div class="content">
    <!--                    add anh register-->
                        Quản trị viên xem thông tin về các thao tác thực hiện tại trang chủ Quản trị viên: <br>
                          <p style="padding-left: 30px;">
                          • Nhấn vào thanh <b-button icon-right="chevron-down"><span>5 dòng/trang</span></b-button> để hiển thị số danh sách môn học tùy ý trên một trang.<br>
                          • Nhấn vào nút <b-button><b-icon size="is-small" icon="sync"/><span>Làm mới</span></b-button> để tải lại bảng.<br>
                          </p>
                    </div>
                </div>
              </b-collapse>
            </div>


        </b-collapse>

    </div>
</template>

<script>
    export default {
        name: "admin-manual"
    }
</script>

<style scoped>
.header1:hover {
  color: #3273dc;
}
</style>
