class JournalEntry:
    default_path = r'.\data\out\journal.log'
    
    def __init__(self, entry, path=None):
        if path is None:
            path = self.default_path
        
        self.path = path
        self.entry = entry


entry1 = JournalEntry('первая запись')
entry2 = JournalEntry('вторая запись', r'c:\users\username\journal.log')

# >>> {k: v for k, v in JournalEntry.__dict__.items() if not k.startswith('__')}
# {'default_path': '.\\data\\out\\journal.log'}
# >>>
# >>>
# >>> entry1.__dict__
# {'path': '.\\data\\out\\journal.log', 'entry': 'первая запись'}
# >>>
# >>> entry2.__dict__
# {'path': 'c:\\users\\username\\journal.log', 'entry': 'вторая запись'}
# >>>
# >>>
# >>> entry1.path
# '.\\data\\out\\journal.log'
# >>>
# >>> entry2.path
# 'c:\\users\\username\\journal.log'
# >>>
# >>>
# >>> entry1.default_path
# '.\\data\\out\\journal.log'
# >>>
# >>> entry2.default_path
# '.\\data\\out\\journal.log'
# >>>
# >>> entry1.default_path is entry2.default_path
# True


class JournalEntry2:
    path = r'.\data\out\journal.log'
    
    def __init__(self, entry, path=None):
        if path is None:
            path = self.path
        
        self.path = path
        self.entry = entry


entry3 = JournalEntry2('третья запись')
entry4 = JournalEntry2('четвёртая запись', r'c:\users\username\journal.log')


# >>> {k: v for k, v in JournalEntry.__dict__.items() if not k.startswith('__')}
# {'path': '.\\data\\out\\journal.log'}
# >>>
# >>>
# >>> entry1.__dict__
# {'path': '.\\data\\out\\journal.log', 'entry': 'первая запись'}
# >>>
# >>> entry2.__dict__
# {'path': 'c:\\users\\username\\journal.log', 'entry': 'вторая запись'}
# >>>
# >>>
# >>> entry1.path
# '.\\data\\out\\journal.log'
# >>>
# >>> entry2.path
# 'c:\\users\\username\\journal.log'
# >>>
# >>>
# >>> entry2.__class__.path
# '.\\data\\out\\journal.log'

