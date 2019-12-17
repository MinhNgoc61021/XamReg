<template>
    <section>
<!--1/ Đăng nhập-->
        <b-collapse :open="false" aria-id="contentIdForA11y1">
            <div class = "header1"
                slot="trigger"
                aria-controls="login-manual"><b>1/ Đăng nhập</b></div>
            <div class="notification">
                <div class="content">
<!--                    add anh register-->
                    <p>
                      • Đối với sinh viên, sử dụng tài khoản được cấp bởi Quản trị viên (Administrator/Admin) để đăng nhập. <br>
                      • Đối với Quản trị viên sẽ được cấp và thông báo tài khoản đăng nhập
                    </p>
                </div>
            </div>
        </b-collapse>
<!--        Trang chủ của Quản trị viên -->
        <b-collapse :open="false" aria-id="contentIdForA11y1">
            <div class = "header1"
                slot="trigger"
                aria-controls="admin-page-manual"><b>2/ Trang chủ của Quản trị viên</b></div>

            <b-collapse :open="false" aria-id="contentIdForA11y1">
                <div class = "header1"
                    slot="trigger"
                    aria-controls="student-management-manual"><i>2.1/ Quản lí sinh viên</i></div>
                <b-collapse :open="false" aria-id="contentIdForA11y1">
                    <div class = "header1"
                        slot="trigger"
                        aria-controls="student-management-manual"><i>2.1.1/ Import danh sách sinh viên tại tab Nhập bằng Excel</i></div>
                    <div class="notification">
                      <div class="content">
                        <!--add anh Import danh sách sinh viên-->
                                • Quản trị viên có thể upload <b>file excel (.xlsx)</b>:
                                  <p style="padding-left: 30px;">
                                    ◦ File excel <b>Danh sách thông tin sinh viên</b> bao gồm các cột: Mã số sinh viên, tên sinh viên, ngày sinh, giới tính và mã khóa học của sinh viên. <br>
                                    ◦ File excel <b>Danh sách sinh viên đủ điều kiện và không đủ điều kiện tham gia kì thi học phần </b> bao gồm các cột: Mã số sinh viên, mã số môn học, tên môn học và thông tin sinh viên (Đủ điều kiện/Không đủ điều kiện) <br>
                                    ◦ File excel tổng hợp của hai file trên bao gồm các cột: Mã số sinh viên, tên sinh viên, ngày sinh, giới tính, mã khóa học của sinh viên, mã số môn học, tên môn học và thông tin sinh viên (Đủ điều kiện/Không đủ điều kiện) <br>
                                  </p>
                        <p><b-icon pack="fas" icon="exclamation-triangle" size="is-small"></b-icon><strong style="color: red">Chú ý</strong>: Yêu cầu file excel phải nhập đúng thứ tự các cột như trên, đặc biệt file <b>Danh sách thông tin sinh viên</b> chỉ bao gồm danh sách các sinh viên đã có tài khoản trên hệ thống.</p>
                      </div>
                    </div>
                </b-collapse>

                <b-collapse :open="false" aria-id="contentIdForA11y1">
                    <div class = "header1"
                        slot="trigger"
                        aria-controls="student-management-manual"><i>2.1.2/ Thêm từng thông tin về sinh viên thông qua form</i></div>
                    <div class="notification">
                        <div class="content">
                           <!--add anh form thêm từng thông tin về sinh viên-->
                            <p></p>
                        </div>
                    </div>
                </b-collapse>

                <b-collapse :open="false" aria-id="contentIdForA11y1">
                    <div class = "header1"
                        slot="trigger"
                        aria-controls="student-management-manual"><i>2.1.3/ Xem danh sách sinh viên tại tab Xem & Chỉnh sửa danh sách sinh viên cung cấp các chức năng:</i></div>
                    <div class="notification">
                        <div class="content">
                           <!--add anh form thêm từng thông tin về sinh viên-->
                                  • Nhấn vào nút <b-icon pack="fas" icon="edit" size="is-small"></b-icon> để chỉnh sửa thông tin của sinh viên.<br>
                                  • Nhấn vào nút <b-icon pack="fas" icon="trash" size="is-small"></b-icon> để xóa thông tin của sinh viên đó khỏi bảng.<br>
                                  • Quản trị viên nhập Mã số sinh viên tại thanh tìm kiếm <b-input placeholder="Tìm kiếm bằng mã số sinh viên"></b-input> để tìm kiếm thông tin của sinh viên mong muốn.<br>
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
            </b-collapse>

          <b-collapse :open="false" aria-id="contentIdForA11y1">
            <div class = "header1"
                    slot="trigger"
                    aria-controls="subject-management-manual"><i>2.2/ Quản lí môn thi</i></div>
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
                      • Quản trị viên nhập Mã số môn học tại thanh tìm kiếm <b-input placeholder="Tìm kiếm bằng Mã số môn học"></b-input> để tìm kiếm thông tin của môn học mong muốn.<br>
                      </p>
                </div>
            </div>
          </b-collapse>

          <b-collapse :open="false" aria-id="contentIdForA11y1">
            <div class = "header1"
                    slot="trigger"
                    aria-controls="room-management-manual"><i>2.3/ Quản lí phòng thi</i></div>
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
                      • Quản trị viên nhập Tên phòng thi tại thanh tìm kiếm <b-input placeholder="Tìm kiếm bằng tên phòng"></b-input> để tìm kiếm thông tin của môn học mong muốn.<br>
                      </p>
                </div>
            </div>
          </b-collapse>

          <b-collapse :open="false" aria-id="contentIdForA11y1">
            <div class = "header1"
                    slot="trigger"
                    aria-controls="log-management-manual"><i>2.4/ Quản lí nhật ký</i></div>
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
        </b-collapse>


    </section>
</template>

<script>
    export default {
        name: "manual"
    }
</script>

<style scoped>
.header1:hover {
  color: midnightblue;
}
</style>
