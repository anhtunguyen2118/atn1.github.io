import pyautogui
import time
import cv2
import os

def find_and_click_image(image_path, interval=1):
    """
    Tìm kiếm hình ảnh trên màn hình và click vào đó khi phát hiện.
    Sau khi click, nhấn Enter rồi tìm nút "dấu X" để đóng.
    :param image_path: Đường dẫn đến file ảnh cần tìm.
    :param interval: Thời gian giữa các lần quét màn hình (giây).
    """
    while True:
        try:
            # Kiểm tra file ảnh có tồn tại không
            if not os.path.exists(image_path):
                print(f"Lỗi: File {image_path} không tồn tại!")
                time.sleep(interval)
                continue  # Bỏ qua vòng lặp hiện tại và tiếp tục quét

            # Kiểm tra file có đọc được không bằng OpenCV
            image = cv2.imread(image_path)
            if image is None:
                print(f"Lỗi: Không thể đọc file {image_path}. Kiểm tra định dạng ảnh!")
                time.sleep(interval)
                continue

            # Tìm vị trí của ảnh trên màn hình
            button_location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if button_location:
                # Click vào ảnh tìm thấy
                button_center = pyautogui.center(button_location)
                pyautogui.click(button_center)
                print(f"Đã click vào: {button_center}")
                time.sleep(0.2) 
                

                # Nhấn Enter
                pyautogui.press("enter")
                print("Đã nhấn Enter")
                time.sleep(4)  # Chờ sau khi nhấn Enter

                # Tìm và click vào nút "dấu X"
                close_button = pyautogui.locateOnScreen(r"C:\Users\anhtu\OneDrive\Desktop\auto\dauX.png", confidence=0.8)
                if close_button:
                    close_center = pyautogui.center(close_button)
                    pyautogui.click(close_center)
                    print(f"Đã click vào dấu X tại: {close_center}")
                 
                else:
                    print("Không tìm thấy dấu X, tiếp tục vòng lặp...")

            else:
                print("Chưa phát hiện hình ảnh, tiếp tục kiểm tra...")

            time.sleep(interval)

        except Exception as e:
            print(f"Lỗi xảy ra: {e}",end=' \r')
            

# Đường dẫn đến file ảnh
image_path = r"C:\Users\anhtu\OneDrive\Desktop\auto\toimuonthanhtoan.png"

# Gọi hàm với thời gian quét 1 giây
find_and_click_image(image_path, interval=1)
