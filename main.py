# 가계부 프로그램
import os

ver = '0.1'
year = '2017'
static_arr = ('지출','수입')
print('This Program used Unicode.')
print('Money Diary version : %s'%ver)

def mainfunc():
	while 1:
		print('원하는 작업을 선택하세요.')
		sel = input();
		if sel == '1':
			print('1.입출금 기록')
			inout()
		elif sel == '2':
			print('2.통계')
		elif sel == '3':
			print('3. 빠져나가기')
		os.system('clear') # windows = cls

def inout():
	print('==== 기록 모드 ====')
	print('파일을 불러옵니다...')
	file = open('money.dat','r')
	line_num=1
	line=file.readline()
	while line:
		print('%s'%(line),end='')
		line=file.readline()
	file.close()
	while 1:
		print('모두 출력하였습니다.')
		print('이어서 기록하시겠습니까? (Y or N)')
		sel1=input()
		if sel1 == 'Y' or 'y':
			print('[기록모드]')
			print('날짜 4자리 입력')
			date = input()
			print('1 : 지출, 2 : 수입 ')
			updown = input()
			print('메모')
			memo = input()
			print('금액')
			money = input()
			if updown == 1:
				print('%s%s / 지출 / %s / %d'%year%date%memo%money)
				DATA_STR="%s%s/지출/%s/%d"%year%date%memo%money
				print(DATA_STR)
			elif updown == 2:
				print('%s%s / 수입 / %s / %d'%year%date%memo%money)
				DATA_STR="%s%s/지출/%s/%d"%year%date%memo%money
			# 기록
			
			while 1:
				print('계속입력하려면 [엔터두번] 방금기록 취소 [u] 나가려면 [q]')
				sel2 = input()
				if sel2 == 'Q' or 'q':
					file = open('money.dat','a')
					file.write(DATA_STR)
					print('방금 전 내용을 저장하였습니다. 메인으로 돌아갑니다.')
				elif sel2 == 'U' or 'u':
					print('취소되었습니다. 메인으로 돌아갑니다.')
				else:
					print('방금 전 내용을 저장하였습니다. 엔터를 누르면 계속 기록합니다.')
					input()
					
		elif sel1 == 'N'or 'n':
			mainfunc()
			


mainfunc()

	
