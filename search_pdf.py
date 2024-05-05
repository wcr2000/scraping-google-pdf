from googlesearch import search
import requests
import re
import urllib.parse
import os


def search_google(query, num_results=10):
    search_results = search(query,sleep_interval=5, num_results=num_results)
    return search_results

def find_pdf_links(urls):
    pdf_links = []
    for url in urls:
        if url.endswith(".pdf"):
            pdf_links.append(url)
    return pdf_links

def download_pdf(url, folder_name):
    try:
        
        response = requests.get(url)
        pattern = r'/([^/]+)$'
        filename = re.search(pattern, url).group(1)
        filename = urllib.parse.unquote(filename)
        file_path = os.path.join(folder_name, filename)
        with open(file_path, 'wb') as f:
            f.write(response.content)
            print(f"Downloaded {file_path} {url} successfully.")
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

def read_name(name):
    # ใช้คำค้นหาที่คุณต้องการ
    query = name
    sirfile= '.pdf'
    # ค้นหาบน Google
    search_q=query+sirfile
    search_results = search_google(search_q)

    # ค้นหาลิงก์ของไฟล์ PDF
    pdf_links = find_pdf_links(search_results)


    # สร้างโฟลเดอร์ (ถ้ายังไม่มี)
    folder_name = 'data_catalog/'+query
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


    # ดาวน์โหลดไฟล์ PDF
    for pdf_link in enumerate(pdf_links):
        download_pdf(pdf_link[1], folder_name)
        print("\\-----------------------------------------------\\")
        # print(f"Downloaded name {name}")

name = input('ใส่ชื่อที่จะค้นหาและดาวน์โหลด : ')
read_name(name)