# Eel Clock App

Đây là một ứng dụng đồng hồ đơn giản được xây dựng bằng Python và JavaScript sử dụng thư viện **Eel**. Thư viện **Eel** giúp kết nối Python và JavaScript, cho phép Python gọi các hàm từ JavaScript và ngược lại.

### Mô tả

Ứng dụng đồng hồ sẽ hiển thị thời gian thực và cập nhật mỗi giây. Mỗi khi thời gian thay đổi, ứng dụng sẽ gửi thời gian hiện tại từ JavaScript đến Python và in ra console. Eel đảm nhận việc kết nối giữa giao diện web và mã Python.

### Cấu trúc thư mục

```
project_folder/
├── main.py
└── web/
      ├── index.html
      ├── script.js
      ├── style.css
```

- **main.py**: Tệp Python chính, khởi tạo thư viện Eel và xử lý các yêu cầu từ JavaScript.
- **web/index.html**: Tệp HTML hiển thị đồng hồ và kết nối với JavaScript.
- **web/script.js**: Tệp JavaScript xử lý việc cập nhật đồng hồ mỗi giây và gửi thời gian đến Python.
- **web/style.css**: Tệp CSS định dạng giao diện đồng hồ.

### Cách chạy ứng dụng

1. Cài đặt thư viện Eel (nếu chưa có):
   ```bash
   pip install eel
   ```

2. Chạy ứng dụng bằng cách thực thi tệp main.py:
   ```bash
   python main.py
   ```

3. Ứng dụng sẽ tự động mở cửa sổ trình duyệt hiển thị đồng hồ, và đồng hồ sẽ được cập nhật mỗi giây.

### Mô tả mã nguồn

#### main.py

- Tệp Python này khởi tạo thư viện Eel và xác định các hàm mà JavaScript có thể gọi.

```python
import eel

# Khởi tạo thư viện Eel, chỉ định thư mục chứa các tệp web
eel.init('web')

# Hàm nhận thời gian từ JavaScript
@eel.expose
def send_time_to_python(time_string):
    print(f"Current time from JS: {time_string}")

# Bắt đầu giao diện Eel
eel.start('index.html', size=(800, 600))
```

#### web/script.js

- Tệp JavaScript này cập nhật thời gian đồng hồ mỗi giây và gửi thời gian đến Python.

```javascript
Sao chép mã
function updateClock() {
    let now = new Date();
    let hours = now.getHours();
    let minutes = now.getMinutes();
    let seconds = now.getSeconds();

    hours = hours < 10 ? "0" + hours : hours;
    minutes = minutes < 10 ? "0" + minutes : minutes;
    seconds = seconds < 10 ? "0" + seconds : seconds;

    let timeString = hours + ":" + minutes + ":" + seconds;
    document.getElementById("clock").innerHTML = timeString;

    // Gọi hàm Python qua Eel
    eel.send_time_to_python(timeString);
}

// Cập nhật đồng hồ mỗi giây
setInterval(updateClock, 1000);
updateClock();
```

#### web/style.css

- Tệp CSS này định dạng cho giao diện người dùng, tạo kiểu cho đồng hồ và nền tối.

```css
body
{
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: black;
}

#clock
{
    font-size: 5rem;
    font-weight: 1000;
    color: white;
    padding: 30px 40px;
    border-radius: 5px solid rgb(255, 255, 255);
    border: 5px solid rgb(255, 255, 255);
}
```

#### web/index.html

- Tệp HTML này hiển thị đồng hồ và kết nối với các tệp CSS và JavaScript.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Đồng hồ</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div id="clock"></div>

    <script src="script.js"></script>
</body>
</html>
```

### Tính năng

- Hiển thị thời gian: Đồng hồ sẽ hiển thị thời gian thực và tự động cập nhật mỗi giây.

- Giao diện đẹp: Giao diện tối với chữ đồng hồ lớn và dễ nhìn.

- Kết nối giữa Python và JavaScript: Thư viện Eel giúp gọi các hàm Python từ JavaScript và ngược lại.

### Các bước phát triển

- Khởi tạo Eel: Đảm bảo rằng thư viện Eel được khởi tạo đúng và thư mục web được chỉ định đúng.

- Tạo giao diện người dùng: Thiết kế đồng hồ với HTML và CSS.

- Kết nối Python và JavaScript: Sử dụng Eel để gửi và nhận dữ liệu giữa Python và JavaScript.

### Cảm ơn

- Cảm ơn bạn đã xem qua dự án này. Nếu có bất kỳ câu hỏi nào, vui lòng mở issue hoặc liên hệ với tôi.
