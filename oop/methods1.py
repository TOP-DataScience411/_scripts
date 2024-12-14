class AudioPlayer:
    
    def play(self, track_path, format='mp3'):
        breakpoint()
        print('... играет трек ...')


# >>> {
# ...     k: v
# ...     for k, v in AudioPlayer.__dict__.items()
# ...     if not k.startswith('__')
# ... }
# {'play': <function AudioPlayer.play at 0x000001C3361F39C0>}

sony_mxh400 = AudioPlayer()

# >>> AudioPlayer.play
# <function AudioPlayer.play at 0x000001C3361F39C0>
# >>> 
# >>> sony_mxh400.play
# <bound method AudioPlayer.play of <__main__.AudioPlayer object at 0x000001C335DBB950>>


# при вызове связанного метода от экземпляра происходит подмена вызова:
#   instance.method -> <bound method Class.function of instance>
#   instance.method(*args, **kwargs) -> Class.function(instance, *args, **kwargs)


# >>> sony_mxh400.play('path/to/track')
# 
# > methods1.py(5) play()
#   -> print('... играет трек ...')
# 
# (Pdb) locals()
# {'self': <__main__.AudioPlayer object at 0x000002087824BEF0>, 'track_path': 'path/to/track', 'format': 'mp3'}
# 
# (Pdb) self
# <__main__.AudioPlayer object at 0x000002087824BEF0>
# 
# (Pdb) sony_mxh400
# <__main__.AudioPlayer object at 0x000002087824BEF0>
# 
# (Pdb) self is sony_mxh400
# True

