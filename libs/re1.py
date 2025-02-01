from re import compile


text = '''
re.compile(pattern, flags=0)
Compile a regular expression pattern into a regular expression object, which can be used for matching using its match(), search() and other methods, described below.

The expression’s behaviour can be modified by specifying a flags value. Values can be any of the flags variables, combined using bitwise OR (the | operator).

The sequence
prog = re.compile(pattern)
result = prog.match(string)
is equivalent to
result = re.match(pattern, string)
but using re.compile() and saving the resulting regular expression object for reuse is more efficient when the expression will be used several times in a single program.

Note: The compiled versions of the most recent patterns passed to re.compile() and the module-level matching functions are cached, so programs that use only a few regular expressions at a time needn’t worry about compiling regular expressions.
'''

pat_match_search = compile(r'match\(\)|search\(\)')

results1 = pat_match_search.findall(text)
results2 = list(pat_match_search.finditer(text))


pat_func_names = compile(r'[a-zA-Z\.]+\(\)')

results3 = pat_func_names.findall(text)


pat_func_names_args = compile(r'[a-zA-Z\.]+\(.*?\)')

results4 = pat_func_names_args.findall(text)

