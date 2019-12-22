<template>
    <div class="container">
      <h1 class="title is-3">Trợ giúp</h1>
      <h2 class="subtitle is-6">Hướng dẫn sử dụng về phần mềm ExamReg cho quản trị viên (Admin) và sinh viên</h2>
      <hr>
<!--1/ Đăng nhập-->
        <b-collapse :open="true" aria-id="contentIdForA11y1">
            <div class = "header1"
                slot="trigger"
                aria-controls="login-manual"><b>1. Đăng nhập</b></div>
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
<!--        Đối với Quản trị viên (Admin) -->
        <b-collapse :open="false" aria-id="contentIdForA11y1">
            <div class = "header1"
                slot="trigger"
                aria-controls="admin-page-manual"><b>2. Đối với Quản trị viên (Admin)</b>
            </div>
            <b-collapse :open="false" aria-id="contentIdForA11y1">
                <div class = "header1"
                    slot="trigger"
                    aria-controls="student-management-manual"><i>2.1. Quản lí sinh viên</i>
                </div>
                <b-collapse :open="false" aria-id="contentIdForA11y1">
                    <div class = "header1"
                        slot="trigger"
                        aria-controls="student-management-manual"><i>2.1.1. Import danh sách sinh viên tại tab Nhập bằng Excel</i></div>
                    <div class="notification">
                      <div class="content">
                        <!--add anh Import danh sách sinh viên-->
                                • Quản trị viên có thể upload <b>file excel (.xlsx)</b>:
                                  <p style="padding-left: 30px;">
                                    ◦ File excel <b>Danh sách thông tin sinh viên</b> bao gồm các cột: <b>Mã số sinh viên (VD: 17021000), tên sinh viên, ngày sinh, giới tính và mã khóa học của sinh viên.</b> <br>
                                    ◦ File excel <b>Danh sách sinh viên đủ điều kiện và không đủ điều kiện tham gia kì thi học phần </b> bao gồm các cột: <b>Mã số sinh viên, mã số môn học (VD: INT1005), tên môn học và thông tin sinh viên (Đủ điều kiện/Không đủ điều kiện)</b>. <br>
                                    ◦ File excel tổng hợp của của ca hai file trên bao gồm các cột: <b>Mã số sinh viên, tên sinh viên, ngày sinh, giới tính, mã khóa học (VD: K62CACLC2) của sinh viên, mã số môn học, tên môn học và thông tin sinh viên (Đủ điều kiện/Không đủ điều kiện)</b>. <br>
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
                            <p></p>
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
                        • Quản trị viên nhập Mã số môn học tại thanh tìm kiếm <b-input placeholder="Tìm kiếm bằng Mã số môn học"></b-input> để tìm kiếm thông tin của môn học mong muốn.<br>
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
                        • Quản trị viên nhập Tên phòng thi tại thanh tìm kiếm <b-input placeholder="Tìm kiếm bằng tên phòng"></b-input> để tìm kiếm thông tin của môn học mong muốn.<br>
                        </p>
                  </div>
              </div>
            </b-collapse>

            <b-collapse :open="false" aria-id="contentIdForA11y1">
              <div class = "header1"
                      slot="trigger"
                      aria-controls="log-management-manual"><i>2.4. Quản lí nhật ký</i>
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
        </b-collapse>
<!--        Đối với Sinh viên -->
        <b-collapse :open="false" aria-id="contentIdForA11y1">
            <div class = "header1"
                  slot="trigger"
                  aria-controls="student-manual"><b>3. Đối với sinh viên</b>
            </div>
            <b-collapse :open="false" aria-id="contentIdForA11y1">
                  <div class = "header1"
                      slot="trigger"
                      aria-controls="student-manual"><i>3.1. Thông tin chung</i>
                  </div>
                  <div class="notification">
                      <div class="content">
                          <p>
                            • Trang thông tin chung sẽ hiểm thị những thông tin của sinh viên như: Tài khoản, Họ và tên, Ngày sinh, Khóa học, Giới tính.
                          </p>
                      </div>
                  </div>
            </b-collapse>
            <b-collapse :open="false" aria-id="contentIdForA11y1">
                <div class = "header1"
                     slot="trigger"
                     aria-controls="student-manual"><i>3.2. Đăng ký dự thi</i>
                </div>
                <div class="notification">
                  <div class="content">
                    • Sinh viên nhập Mã môn thi tại thanh tìm kiếm <b-input placeholder="Tìm kiếm bằng mã môn học"></b-input> để tìm kiếm thông tin về ca thi mà sinh viên mong muốn.<br>
                    • Nhấn vào nút  <b-button><b-icon size="is-small" icon="sync"/><span>Làm mới</span></b-button> để tải lại bảng.<br>
                    • Nhấn vào nút <b-icon pack="fas" icon="chevron-right" size="is-small"></b-icon> đầu mỗi hàng để xem thông tin chi tiết về <b>ca thi</b> và <b>phòng thi</b> của sinh viên:
                    <p style="padding-left: 30px;">
                      ◦ Danh sách môn thi (ca thi) sinh viên đủ điều kiện thi.<br>
                      ◦ Danh sách các phòng thi mà sinh viên có thể đăng ký.<br>
                    </p>
                    • Nhấn vào mũi tên <b-icon pack="fas" icon="arrow-up" size="is-small"></b-icon> hoặc <b-icon pack="fas" icon="arrow-down" size="is-small"></b-icon> tại tên cột để sắp xếp lại theo thứ tự tăng dần hoặc giảm dần.<br>
                    <p><b-icon pack="fas" icon="exclamation-triangle" size="is-small"></b-icon><strong style="color: red"> Chú ý:</strong> Sẽ có trường hợp sinh viên bị thiếu môn: có thể do hệ thống chưa cập nhật thêm hoặc do sinh viên không đủ điều kiện thi những môn thi đó.</p>
                  </div>
                </div>
            </b-collapse>
            <b-collapse :open="false" aria-id="contentIdForA11y1">
                <div class = "header1"
                     slot="trigger"
                     aria-controls="student-manual"><i>3.3. In phiếu đăng ký dự thi</i>
                </div>
                <div class="notification">
                  <div class="content">
                    • Nhấn vào nút <b-icon pack="fas" icon="trash" size="is-small"></b-icon> để hủy đăng ký ca thi<br>
                    • Nhấn vào nút  <b-button><b-icon size="is-small" icon="sync"/><span>Làm mới</span></b-button> để tải lại bảng.<br>
                    • Nhấn vào nút <b-button icon-left="file-pdf">In phiếu báo dự thi</b-button> để in phiếu báo dự thi.<br>
                  </div>
                </div>
            </b-collapse>
        </b-collapse>
    </div>
</template>

<script>
    export default {
        name: "manual"
    }
</script>

<style scoped>
.header1:hover {
  color: #3273dc;
}
</style>
