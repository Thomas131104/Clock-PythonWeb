# Phần 0: Giải thích các bước

- `HTML`: Tạo một giao diện đơn giản với một nút bấm. Khi nút được nhấn, JavaScript sẽ gọi một hàm Python qua Eel.

- `CSS`: Định dạng cho giao diện, giúp các phần tử trên trang trông dễ nhìn hơn.

- `JavaScript`: Gửi thông điệp từ frontend đến backend Python khi nút được nhấn và nhận phản hồi từ Python.

- `Python`: Xử lý thông điệp nhận được từ JavaScript và trả lời lại JavaScript.


# Phần 1: JavaScript

- `eel.<function_name>`: Gọi hàm Python từ JavaScript. Bạn có thể truyền các tham số và nhận phản hồi qua callback.

# Phần 2: Python

- `@eel.expose`: Dùng để "expose" (cho phép) hàm Python có thể gọi từ JavaScript. Hàm Python này sẽ nhận tham số từ JavaScript và có thể trả về giá trị cho JavaScript.