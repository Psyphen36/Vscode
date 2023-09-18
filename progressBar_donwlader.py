import requests
from tqdm import tqdm


url = 'https://download-cdn.jetbrains.com/idea/ideaIU-2023.1.4.tar.gz'
req = requests.get(url, stream=True)
total_expected_bytes = int(req.headers['Content-Length'])

bytes_received = 0
progress_bar = tqdm(total=total_expected_bytes, unit='iB', unit_scale=True)

with open('ideaIU.tar.gz', 'wb') as f:
    for chunk in req.iter_content(chunk_size=128):
        progress_bar.update(128)

        f.write(chunk)
        bytes_received += 128
progress_bar.close()
