import requests
import wget
img_url = ''
video_url = ''
img2_url = 'https://yandex.ru/images/search?text=картинки&img_url=https%3A%2F%2Fget.wallhere.com%2Fphoto%2F2700x1800-px-building-castle-forest-Hohenzollern-landscape-1077207.jpg&pos=0&rpt=simage&stype=image&lr=11435&parent-reqid=1641456040323817-17560851270109858969-vla1-5786-vla-l7-balancer-8080-BAL-9136&source=wiz'
video2_url = ''
def download_img(url=''):
    try:
        response = requests.get(url=url)

        with open('reg_img.jpg', 'wb') as file:
            file.write(response.content)

        return 'Img successfully downloaded!'

    except Exception as _ex:
        return 'Upps...Check the URL please!'


def download_video(url=''):
    try:
        # response = requests.get(url=url)

        # with open('reg_video.mp4', 'wb') as file:
            # file.write(response.content)

        response = requests.get(url=url, stream=True)

        with open('reg_video.mp4', 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024*1024):
                if chunk:
                    file.write(chunk)


        return 'Img successfully downloaded!'

    except Exception as _ex:
        return 'Upps...Check the URL please!'


def download_wget(url='', file_type='video'):
    try:
        if file_type == 'video':
            wget.download(url=url, out=f'wget_(file_type).mp4')
        else:
            wget.download(url=url, out=f'wget_(file_type).jpg')
    except Exception as _ex:
        return 'Upps... Check the URL please!'

def main():
    download_wget(url=img2_url, file_type='img')
    # print(download_img(url=img_url))
    # print(download_video(url=video_url))
    download_wget(url=video2_url, file_type='video')

if __name__ == '__main__':
    main()
