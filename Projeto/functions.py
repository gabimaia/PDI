import cv2
import os

# script adaptado de: https://stackoverflow.com/a/44659589
def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # inicia as dimensoes
    # pega o tamanho
    dim = None
    (h, w) = image.shape[:2]
    # compara com None
    if width is None and height is None:
        return image
    # ccheca
    if width is None:
        # calcula o raio e pega as dimensoes
        r = height / float(h)
        dim = (int(w * r), height)
    # se nao, retorna none
    else:
        # mesma coisa de cima
        r = width / float(w)
        dim = (width, int(h * r))

    # redimensiona
    resized = cv2.resize(image, dim, interpolation = inter)
    # retorna imagem redimensionada
    return resized



class CFEVideoConf(object):
    # redimensionamento do video capturado pela webcan
    STD_DIMENSIONS =  {
        "360p": (480, 360),
        "480p": (640, 480),
        "720p": (1280, 720),
        "1080p": (1920, 1080),
        "4k": (3840, 2160),
    }

    VIDEO_TYPE = {
        'avi': cv2.VideoWriter_fourcc(*'XVID'),
        'mp4': cv2.VideoWriter_fourcc(*'XVID'),
    }

    width           = 640
    height          = 480
    dims            = (640, 480)
    capture         = None
    video_type      = None
    def __init__(self, capture, filepath, res="480p", *args, **kwargs):
        self.capture = capture
        self.filepath = filepath
        self.width, self.height = self.get_dims(res=res)
        self.video_type = self.get_video_type()

    # seta a resolucao
    # adaptada de https://kirr.co/0l6qmh
    def change_res(self, width, height):
        self.capture.set(3, width)
        self.capture.set(4, height)

    def get_dims(self, res='480p'):
        width, height = self.STD_DIMENSIONS['480p']
        if res in self.STD_DIMENSIONS:
            width, height = self.STD_DIMENSIONS[res]
        self.change_res(width, height)
        self.dims = (width, height)
        return width, height

    def get_video_type(self):
        filename, ext = os.path.splitext(self.filepath)
        if ext in self.VIDEO_TYPE:
          return  self.VIDEO_TYPE[ext]
        return self.VIDEO_TYPE['avi']