import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#version = "125.0.6422.141"
chrome_option = webdriver.ChromeOptions()
chrome_option.binary_location = "C://ChromeDriver//chrome-win64//chrome.exe"
chrome_driver_path = "C://ChromeDriver//chromedriver-win64//chromedriver.exe"

service_options = webdriver.ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(options=chrome_option,service=service_options)

driver.get("https://fireant.vn/ma-chung-khoan/ACB")
time.sleep(1)
driver.get("https://fireant.vn/ma-chung-khoan/ACB")
time.sleep(1)
so_lenh = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[3]/main/div/div[3]/div[2]/div[1]/div[2]/div/div[1]/button[2]')
#print(so_lenh)
#so_lenh = driver.find_element(By.CLASS_NAME,'inline-flex')
time.sleep(1)
so_lenh.click()
time.sleep(1)
script = """
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
driver.execute_script(script)
time.sleep(5)