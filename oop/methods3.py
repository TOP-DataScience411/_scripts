class Image:
    def __init__(self, pixels):
        pass
    
    @classmethod
    def open_png(cls, path_to_image):
        with open(path_to_image, 'rb') as filein:
            data = filein.read()
        # обработка bytes последовательности для декодирования формата PNG
        # ...
        return cls(data)
    
    @classmethod
    def open_jpg(cls, path_to_image):
        with open(path_to_image, 'rb') as filein:
            data = filein.read()
        # обработка bytes последовательности для декодирования формата JPG
        # ...
        return cls(data)


# при вызове классового метода от объекта класса происходит подмена вызова c передачей объекта класса в качестве аргумента:
#   Class.cls_method -> <bound method Class.cls_method of Class>
#   Class.cls_method(*args, **kwargs) -> Class.cls_method(Class, *args, **kwargs)

img1 = Image.open_png('methods1.py')

# при вызове классового метода от экземпляра происходит подмена вызова c передачей объекта класса в качестве аргумента:
#   instance.__class__ -> Class
#   instance.cls_method -> <bound method Class.cls_method of Class>
#   instance.cls_method(*args, **kwargs) -> Class.cls_method(Class, *args, **kwargs)

img2 = img1.open_jpg('methods2.py')

