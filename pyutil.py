#coding=utf8
import os
import sys
import codecs
import chardet

py_abspath = os.path.dirname(sys.argv[0])   
if not os.path.isdir(py_abspath):
    py_abspath = sys.path[0]
if not os.path.isdir(py_abspath):
    py_abspath = os.path.dirname(__file__)

os.chdir(py_abspath)
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

def py_print(txt):
    encoding = 'utf-8'
    try:
        encoding = chardet.detect(txt).get('encoding')
        # print(encoding)
    except Exception as e:
        # print(e.message)
        pass
    try:
        txt = txt.decode(encoding,'ignore').encode('gbk','ignore')
    except Exception as e:
        print(e.message)
    print(txt)

def py_writefile(txt, pathfile, mode='w'):
    encoding = 'utf-8'
    try:
        encoding = chardet.detect(txt).get('encoding')
        # print(encoding)
    except:
        pass
    with codecs.open(pathfile, mode, 'utf-8') as fr:
        if encoding != 'utf-8':
            txt = txt.decode(encoding, 'ignore').encode('utf-8')
        fr.write(txt)

def py_readlines(pathfile):
    with codecs.open(pathfile, 'r', 'utf-8') as fr:
        lines = fr.readlines()
    return lines

def py_read(pathfile):
    with codecs.open(pathfile, 'rb', 'utf-8') as fr:
		html = fr.read()
    return html

def py_remove(pathfile):
    if os.path.isfile(pathfile) is True:
        os.remove(pathfile)

def py_makedirs(path):
    if os.path.exists(path) is True:
        os.makedirs(path)

if __name__ == '__main__':
    s = '哈哈哈'
    # s = s.encode('gbk')
    # print(type(s))
    # printutil(s)