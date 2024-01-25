import requests
from tqdm import tqdm

def download_video_with_progress(url, save_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(save_path, 'wb') as file, tqdm(
        desc="تحميل الفيديو",
        total=total_size,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)

    print("تم تحميل الفيديو بنجاح.")

# استخدم الدالة مع الرابط المحدد والمسار الذي تريد حفظ الفيديو فيه
video_url = "رابط الفيديو"
save_path = "Courses/Lives"
download_video_with_progress(video_url, save_path)
