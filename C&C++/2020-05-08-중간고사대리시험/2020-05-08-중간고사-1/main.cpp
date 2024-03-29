#include <stdio.h>
#include <math.h>

int main()
{
	/*---------------------------------------------------------------------------------------
	* 파일 : main.cpp
	* 기능 : 중간고사
	* 개발자 : 박수하
	* 개발시작 : 2020-05-08
	* 개발종료 : 2020-05-08 (Pass)
	---------------------------------------------------------------------------------------*/
	// 사용자가 N을 입력하게끔 안내해주는 메시지
	printf("*** Diamond ****\n");
	printf("Enter N (1 ~ 9):  ");
	int N;
	// 사용자에게 N의 값을 입력받고 N을 1 증가시킴
	scanf("%d", &N); N++;
	// 상단의 역삼각형을 출력하는 반복문
	for (int i = 0; i < N; i++) {
		for (int j = N - 1; j > i; j--) {
			printf(" ");
		}

		for (int j = 0; j < 2 * i + 1; j++) {
			printf("*");
		}
		printf("\n");
	}
	// 하단의 역삼각형을 출력하기
	for (int i = 1; i < N; i++) {
		for (int j = 0; j < i; j++) {
			printf(" ");
		}

		for (int j = 2 * N - 1; j > 2 * i; j--) {
			printf("*");
		}
		printf("\n");
	}
}