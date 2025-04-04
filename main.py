import eel
import sys

# Khởi tạo thư viện Eel, chỉ định thư mục chứa các tệp web
eel.init('web')

# Hàm nhận thời gian từ JavaScript
@eel.expose
def send_time_to_python(time_string):
    print(f"Current time from JS: {time_string}")


# Bắt đầu giao diện Eel với callback khi đóng cửa sổ
eel.start('index.html', size=(800, 600))