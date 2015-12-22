# map - tool to replace many lines in a pipe

### why

While using pipes, I need sometimes to modify the stdout. Sed is fine for
changing one line, gets difficult when you have lots of changes to make.

### how

Create a mapfile containing one Python dictionary. Keys being the lines to
replace and values the target output. Example:

```python
# mymap
{
    'wrong_line': 'now_better',
    'sth_else': 'changed'
}
```

Use on any stdin:
```bash
$ echo -e "just a line\nwrong_line\nsth_else\njust a line" | map mymap
just a line
now_better
changed
just a line
```

My real use case to explain in more detail, anonymized and reduced:
```bash
# looks like I comitted under three diffeerent signatures
$ hg log -M --template '{author}\n' | sort | uniq -c
      7 bb
     11 Bartek Brak <bartek.brak@gmail.com>
     81 Bartek <bartek@gmail.com>
$ cat mymap
{
    'bb': 'Bartek Brak <bartek.brak@gmail.com>',
    'Bartek <bartek@gmail.com>': 'Bartek Brak <bartek.brak@gmail.com>'
}
# obviously, with this volume, just three lines to one, this is not
# a problem, but I was working with 30+ messed signatures
$ hg log -M --template '{author}\n' | sort | map mymap | uniq -c
     99 Bartek Brak <bartek.brak@gmail.com>
```

### install
```bash
git clone git@github.com:bartekbrak/map.git
pip install ./map
# or, if you know user siteinstallation
pip install --user ./map
# or one day, from PyPI, just
pip install map  # without cloning
```

### todo
- handle regular expressions
