<template>
  <div class="container">
    <h1 class="title is-3">Trợ giúp</h1>
    <h2 class="subtitle is-6">Hướng dẫn sử dụng về phần mềm ExamReg cho sinh viên </h2>
    <hr>
    <!-- Đăng nhập-->
    <b-collapse :open="true" aria-id="contentIdForA11y1">
      <div class = "header1"
           slot="trigger"
           aria-controls="login-manual"><b>1. Đăng nhập</b></div>
      <div class="notification">
        <div class="content">
<!--                   add anh register-->
          <p>
            • Sinh viên sử dụng tài khoản được cấp bởi Quản trị viên (Administrator/Admin) để đăng nhập. <br>
          </p>
          <p><b-icon pack="fas" icon="exclamation-triangle" size="is-small"></b-icon><strong style="color: red"> Chú ý:</strong> Sinh viên được cấp tài khoản mặc định mật khẩu ban đầu sẽ là MSSV của sinh viên đó, khuyến cáo sinh viên thay đổi mật khẩu để bảo vệ quyền lợi và thông tin của mình.</p>
        </div>
      </div>
    </b-collapse>
    <!--        Đối với Sinh viên -->
    <b-collapse :open="false" aria-id="contentIdForA11y1">
            <div class = "header1"
                  slot="trigger"
                  aria-controls="student-manual"><b>2. Đối với sinh viên</b>
            </div>
            <div style="padding-left: 15px;">
              <b-collapse :open="false" aria-id="contentIdForA11y1">
                    <div class = "header1"
                        slot="trigger"
                        aria-controls="student-manual"><i>2.1. Thông tin chung</i>
                    </div>
                    <div class="notification">
                        <div class="content">
                            <p>
                              • Trang thông tin chung sẽ hiểm thị những thông tin của sinh viên như: <b>Tài khoản, Họ và tên, Ngày sinh, Khóa học,...</b>.
                            </p>
                        </div>
                    </div>
              </b-collapse>
              <b-collapse :open="false" aria-id="contentIdForA11y1">
                  <div class = "header1"
                       slot="trigger"
                       aria-controls="student-manual"><i>2.2. Đăng ký dự thi</i>
                  </div>
                  <div class="notification">
                    <div class="content">
                      • Sinh viên nhập tìm kiếm tên kỳ thi tại thanh tìm kiếm <b-input placeholder="Tìm kiếm và chọn tên kỳ thi" icon-pack="fas" icon="search"></b-input> và chọn kỳ thi để truy cập chọn ca thi mình muốn đăng ký.<br>
                      • Sinh viên nhập Mã môn thi tại thanh tìm kiếm <b-input placeholder="Tìm kiếm bằng mã môn thi" icon-pack="fas" icon="search"></b-input>và chọn môn để tìm kiếm thông tin về ca thi mà sinh viên mong muốn.<br>
                      • Nhấn vào nút  <b-button><b-icon size="is-small" icon="sync"/><span>Làm mới</span></b-button> để tải lại bảng.<br>
                      • Nhấn vào nút <b-icon pack="fas" icon="chevron-right" size="is-small"></b-icon> đầu mỗi hàng để xem thông tin chi tiết về <b>ca thi</b> và <b>phòng thi</b> của sinh viên:
                      <p style="padding-left: 30px;">
                        ◦ Danh sách môn thi (ca thi) sinh viên đủ điều kiện thi.<br>
                        <span style="padding-left: 15px;">
                         ◦ Nhấn vào nút <b-button type="is-success" icon-pack="fas" icon-left="plus-square">Đăng ký</b-button> để đăng ký phòng thi.

                        </span><br>
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
                       aria-controls="student-manual"><i>2.3. In phiếu đăng ký dự thi</i>
                  </div>
                  <div class="notification">
                    <div class="content">
                      • Nhấn vào nút <b-icon pack="fas" icon="trash" size="is-small"></b-icon> để hủy đăng ký ca thi<br>
                      • Nhấn vào nút  <b-button><b-icon size="is-small" icon="sync"/><span>Làm mới</span></b-button> để tải lại bảng.<br>
                      • Nhấn vào nút <b-button icon-left="file-pdf">In phiếu báo dự thi</b-button> để in phiếu báo dự thi.<br>
                    </div>
                  </div>
              </b-collapse>
            </div>
        </b-collapse>
  </div>
</template>

<script>
    export default {
        name: "student-manual"
    }
</script>

<style scoped>

</style>
