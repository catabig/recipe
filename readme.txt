requirement: 
python 3.x
pynput (pip install pynput)
tqdm (pip install tqdm) 

*유의사항

- 윈도우 8, 10 의 경우 "모든 항목 더 크게 보기" 설정에 "메인 디스플레이 ~" 의 배율을 확인 한 후, windowconst 에 입력하면됨 (ex. 125% -> windowconst=1.25)
임시로 100% 로 설정한 뒤 windowconst=1 로 하는게 제일 오차 적을듯

- 좌표를 클릭해도 반응없으면(xinput, yinput 안뜨면) 관리자 권한으로 프로그램 실행시킬것

* 사용법
1. 모듈 설치
2. windowconst 값 확인 하고 수정
3. 프로그램 실행
4. 갈 레시피 위치(젤 마지막꺼) 우클릭, 확인 버튼 3개 우클릭
5. 반복회수 입력
6. fin