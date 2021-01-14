# 암호, 해시 관련 모듈 Import
from Crypto.Cipher import AES
from Crypto.Hash import SHA256 as SHA
from os import path
KSIZE = 1024

class myAES():
	def __init__(self, keytext, ivtext):
		hash = SHA.new()
		hash.update(keytext.encode('utf-8'))
		key = hash.digest()	
		self.key = key[:16]
		
		hash.update(ivtext.encode('utf-8'))
		iv = hash.digest()
		self.iv = iv[:16]		
	
	def makeEncInfo(self, filename):
		fillersize = 0
		filesize = path.getsize(filename)
		if filesize%16 != 0:
			fillersize = 16-filesize%16
			
		filler = '0'*fillersize
		header = '%d' %(fillersize)
		gap = 16-len(header)
		header += '#'*gap		
		return header, filler

	def enc(self, filename):
		encfilename = filename + '.enc'
		header, filler = self.makeEncInfo(filename)
		aes = AES.new(self.key, AES.MODE_CBC, self.iv)
		
		h = open(filename, 'rb')
		hh = open(encfilename, 'wb+')
		
		enc = header.encode('utf-8')
		content = h.read(KSIZE)
		content = enc + content
		while content:
			if len(content) < KSIZE:
				content += filler.encode('utf-8')
			
			enc = aes.encrypt(content)			
			hh.write(enc)
			content = h.read(KSIZE)
				
		h.close()
		hh.close()		
	def dec(self, encfilename):
		filename = encfilename + '.dec'
		aes = AES.new(self.key, AES.MODE_CBC, self.iv)
				
		h = open(filename, 'wb+')
		hh = open(encfilename, 'rb')
		
		content = hh.read(16)
		dec = aes.decrypt(content)
		header = dec.decode()
		fillersize = int(header.split('#')[0])
		
		content = hh.read(KSIZE)		
		while content:
			dec = aes.decrypt(content)
			if len(dec) < KSIZE:
				if fillersize != 0:
					dec = dec[:-fillersize]
			h.write(dec)
			content = hh.read(KSIZE)
				
		h.close()
		hh.close()	
def main():
    # 3DES 암호키 생성을 위한 문자열
	keytext = 'samsjang'
    # 초기화 벡터를 위한 문자열
	ivtext = '1234'
    # 평문이 저장되어있는 파일명
	filename = 'plain.txt'
    # 인코딩 파일명
	encfilename = filename + '.enc'
	
    # mycipher 변수에 AES 암호화를 위한 구조를 선언
	myCipher = myAES(keytext, ivtext)
    # AES 암호화
	myCipher.enc(filename)
    # AES 복호화
	myCipher.dec(encfilename)	
	
if __name__ == '__main__':
	main()

## 소스코드 전체에 대한 요약
"""
파일에 저장되어있는 평문을 읽고, 이를 AES 암호화 알고리즘으로 암복호화하는 기능을 내장한 프로그램입니다.
"""

## main함수에 대한 설명
"""
3DES 암호키 생성을 위한 문자열, 초기화 벡터를 위한 문자열을 선언한 뒤 평문이 저장되어있는 파일을 읽어 암복호화하는 과정의 코드를 실행하는 함수입니다.
"""

## myAES 클래스에 대한 설명
"""
3DES를 위해 선언된 클래스입니다. 이 myAES 클래스에서는 암호화를 수행하는 enc()와 복호화를 수행하는 dec() 메소드가 정의되어있습니다.
"""

## myAES 클래스 생성자를 요약하여 설명
"""
__init()__은 클래스 생성자입니다. 인자 keytext는 3DES 암호키 생성을 위한 문자열이며, ivtext는 초기화 벡터를 위한 문자열입니다.
클래스 생성자에서 3DES 객체 생성 시 사용할 키와 초기화 벡터를 구합니다.
"""

## makeEncInfo(self, filename) 함수를 요약하여 설명
"""
makeEncInfo함수는 특정 파일의 파일사이즈를 구하기 위해 사용합니다.
만약 파일사이즈를 16으로 나누었을때 나머지가 0이 아니라면
16에서 파일 사이즈를 뺀 뒤 16으로 나누어 남은 나머지를 파일사이즈로 지정합니다.
"""

## keytext=‘chpark12’ , ivtext = ‘2345’로 코드를 수정하였을 때의 실행 결과
"""
plain.txt : it’s no use crying over spilt milk
plain.txt.enc : L����cr�����u|�l�I"{a7�9�`��H��|���<��3�=UHRZ�A�8�:�X̀
plain.txt.enc.dec : it’s no use crying over spilt milk
"""