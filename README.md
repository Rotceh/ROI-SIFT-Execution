請依照下面順序來安裝
Step1.
	1.安裝Python2.7
	2.安裝NumPy 1.9.2 for Python 2.7
	3.安裝Sci-Py 0.15.1 for Pythom 2.7
	4.安裝dateutil 2.4.1
	5.安裝pyparsing-2.0.3
	6.需要類似MATLAB繪圖功能可選擇多安裝matplot 1.4.3(建議一起裝)  
	7.安裝OpenCV
	--------------------------------------------------------------
	其中dateutil資料夾放至 C:\Python27\Lib\site-packages
	並切換到該目錄底下
	→ python setup.py install
	即完成dateutil的安裝

	OpenCV 資料夾放至 C:\Python27\Lib\site-packages
	並將 opencv\build\python\2.7\x86 裡的cv2.pyd (x86 depends on your python is 32 bits if yours is 64 bits then copy \x64 cv2.pyd)
	複製一份至C:\Python27\Lib\site-packages 即完成

Step2.
	接著直譯soton-test-python-installation.py
	→ python soton-test-python-installation.py

	顯示結果:
	Testing numpy...      -> numpy OK
	Testing scipy...      -> scipy OK
	Testing matplotlib... -> pylab OK
	Testing sympy...      Could not import 'sympy' -> fail
	Testing pytest...     Could not import 'pytest' -> fail

	這樣即可,後面的sympy及pytest還用不到,就別理他



Note:pyparsing-2.0.3.tar.gz跟pyparsing-2.0.3.win32-py2.7.exe
選一個即可
.exe自動安裝第一個則要手動安裝在C:\Python27\Lib\site-packages
指令：python setup.py pyparsing-2.0.3 install

Note:Sublime Test 2
可以用package control install 安裝Jedi - Python autocompletion
輔助開發

> Here is some indented text
>> even more indented

## Titles
# Big title (h1)
## Middle title (h2)
### Smaller title (h3)
#### and so on (hX)
##### and so on (hX)
###### and so on (hX)

## Example lists (1)

 - bullets can be `-`, `+`, or `*`
 - bullet list 1
 - bullet list 2
    - sub item 1
    - sub item 2

        with indented text inside

 - bullet list 3
 + bullet list 4
 * bullet list 5

## Links


```python
import random

class CardGame(object):
    """ a sample python class """
    NB_CARDS = 32
    def __init__(self, cards=5):
        self.cards = random.sample(range(self.NB_CARDS), 5)
        print 'ready to play'
```