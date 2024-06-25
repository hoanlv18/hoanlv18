import pyautogui
import time
import webbrowser
import pyperclip

# Danh sách mã chứng khoán
stock_codes = ["ACB", "VJC", "VRE", "BSR", "VIB", "VEA", "PLX", "TPB", "STB", "HDB", "HVN", "BVH", "SHB", "PDR", "DGC", "VND", "MVN", "MSB", "SSI"]
script_code = """
const scroller = document.querySelector('div[data-test-id="virtuoso-scroller"]');

if (scroller) {
    // Thay đổi giá trị của thuộc tính `style`
    scroller.style.height = '1000000%';
}

setTimeout(() => {

const rows = document.querySelectorAll('div[data-test-id="virtuoso-item-list"] > div');

function formatNumber(value) {
    return value.replace(/,/g, '');
}

const data = Array.from(rows).map(row => {
    const cells = row.querySelectorAll('div.flex-row');
    const extractedValues = Array.from(cells).map(cell => {

        let content = cell.textContent.trim();

        if (/^[\d,]+$/.test(content)) {
            content = formatNumber(content);
        }
        return `"${content}"`;
    });
    return extractedValues;
});

const headers = ["TT1", "TT2", "Thời gian", "Giá", "Thay đổi", "Khớp", "M/B"];
const csvRows = [headers.map(header => `"${header}"`).join(",")];

data.forEach(row => {
    csvRows.push(row.join(","));
});

let csvOutput = csvRows.join("\\n");

const blob = new Blob([csvOutput], { type: 'text/csv' });
const url = URL.createObjectURL(blob);
const a = document.createElement('a');

const currentURL = window.location.href;

const parts = currentURL.split('/');
const stockCode = parts[parts.length - 1];

const today = new Date();
const day = String(today.getDate()).padStart(2, '0');
const month = String(today.getMonth() + 1).padStart(2, '0');
const year = today.getFullYear();
const formattedDate = `${day}${month}${year}`;


const result = `${formattedDate}_${stockCode}.csv`;
    
a.href = url;
a.download = result;
document.body.appendChild(a);
a.click();
document.body.removeChild(a);
URL.revokeObjectURL(url);
}, 3000);
"""

# Tạo danh sách URL
urls = [f"https://fireant.vn/ma-chung-khoan/{code}" for code in stock_codes]

# Đợi 3 giây để bạn có thể chuyển đến cửa sổ muốn click
#print("Bạn có 3 giây để chuyển đến cửa sổ mong muốn...")
#time.sleep(3)  # Điều chỉnh thời gian này nếu cần

#try:
#    while True:
#        x, y = pyautogui.position()
#        print(f"Vị trí chuột: ({x}, {y})", end="\r")
#        time.sleep(0.1)

#except KeyboardInterrupt:
#    print("\nĐã dừng script.")

# Lấy kích thước màn hình (chỉ để tham khảo)
#screen_width, screen_height = pyautogui.size()
#print(f"Kích thước màn hình: {screen_width}x{screen_height}")

# Lấy vị trí hiện tại của con trỏ chuột (chỉ để tham khảo)
#current_mouse_x, current_mouse_y = pyautogui.position()
#print(f"Vị trí con trỏ chuột hiện tại: ({current_mouse_x}, {current_mouse_y})")

try:
    # Vòng lặp qua từng URL
    for url in urls:
        # Di chuyển chuột tới vị trí (100, 200) và click chuột trái
        pyautogui.moveTo(377, 61)
        pyautogui.click()

        # Mở URL trong trình duyệt mặc định
        webbrowser.open(url)

        # Đợi một thời gian để trang web tải xong, bạn có thể điều chỉnh thời gian này
        time.sleep(2)  # Điều chỉnh thời gian này nếu cần

        # Di chuyển chuột tới tab sổ lệnh
        pyautogui.moveTo(741, 364)
        pyautogui.click()
   
        # Di chuyển chuột tới 1 vùng bất kì để bấm chuột phải
        pyautogui.moveTo(764, 658)
        pyautogui.click()
        time.sleep(0.5)
   
        # Bấm chuột phải
        pyautogui.rightClick()

        # Đợi một chút để menu chuột phải hiện ra
        time.sleep(0.5)

        # Di chuyển tới vị trí "Inspect" trong menu chuột phải (tọa độ này cần chính xác)
        pyautogui.moveTo(831, 640)  # Điều chỉnh tọa độ này theo vị trí của "Inspect"
        pyautogui.click()
       
        # Di chuyển chuột tới Console
        time.sleep(0.5)
        pyautogui.moveTo(712, 133)
        time.sleep(0.5)
        pyautogui.click()
        
        time.sleep(0.5)
        # Paste code vào console & bấm enter
        pyperclip.copy(script_code)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.2)
        pyautogui.press('enter')
        
        time.sleep(5)
        print("Đã mở URL & Thực hiện tác vụ xong")

except KeyboardInterrupt:
    print("Đã dừng script.")
finally:
    print("Đã thoát khỏi vòng lặp.")

print("Hoàn thành.")
