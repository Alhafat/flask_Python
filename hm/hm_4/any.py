import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse


def is_valid(url):
    """
    Проверяем, является ли url действительным URL
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_images(url):
    """
    Возвращает все URL‑адреса изображений по одному `url`
    """
    soup = bs(requests.get(url).content, "html.parser")
    urls = []
    for img in tqdm(soup.find_all("img"), "Получено изображение"):
        img_url = img.attrs.get("src")
        if not img_url:
            # если img не содержит атрибута src, просто пропускаем
            continue
        # сделаем URL абсолютным, присоединив имя домена к только что извлеченному URL
        img_url = urljoin(url, img_url)
        # удалим URL‑адреса типа '/hsts-pixel.gif?c=3.2.5'
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass
        # наконец, если URL действителен
        if is_valid(img_url):
            urls.append(img_url)
    return urls


def download(url, pathname):
    """
    Загружает файл по URL‑адресу и помещает его в папку `pathname`
    """
    # если путь не существует, создать dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # загружаем тело ответа по частям, а не сразу
    response = requests.get(url, stream=True)

    # получить общий размер файла
    file_size = int(response.headers.get("Content-Length", 0))

    # получаем имя файла
    filename = os.path.join(pathname, url.split("/")[-1])

    # индикатор выполнения, изменение единицы измерения на байты вместо итераций (по умолчанию tqdm)
    progress = tqdm(response.iter_content(1024), f"Загружен {filename}", total=file_size, unit="B", unit_scale=True,
                    unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress.iterable:
            # записываем прочитанные данные в файл
            f.write(data)
            # обновление индикатора выполнения вручную
            progress.update(len(data))


def main(url, path):
    # получить все изображения
    imgs = get_all_images(url)
    for img in imgs:
        # скачать для каждого img
        download(img, path)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Этот скрипт загружает все изображения с веб‑страницы.")
    parser.add_argument("url", help="URL‑адрес веб‑страницы, с которой вы хотите загрузить изображения.")
    parser.add_argument("-p", "--path",
                        help="Каталог, в котором вы хотите хранить изображения, по умолчанию - это домен переданного URL.")

    args = parser.parse_args()
    url = args.url
    path = args.path

    if not path:
        # если путь не указан, используйте доменное имя этого url в качестве имени папки
        path = urlparse(url).netloc

    main(url, path)