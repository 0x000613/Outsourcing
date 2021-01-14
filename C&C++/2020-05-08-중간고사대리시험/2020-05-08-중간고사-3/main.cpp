// num을 20으로 고정선언
#define num 20
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
	printf("*** Sorting ****\n");
	// 길이가 20인 배열 생성
	int number[num]{ 42, 68, 35, 1, 70, 25, 79, 59, 63, 65, 6, 46, 82, 28, 62, 92, 96, 43, 28, 37 };

	// 정렬하기 전의 배열을 출력
	printf("** Given Data **\n   ");
	for (int i = 0; i < 20; i++) {
		// 배열의 아이템을 10개 기준으로 개행해주기 위한 조건문
		if (i == 10) { printf("\n   "); }
		printf("%d ", number[i]);
	}

	// 스왑을 하기위한 변수 선언
	int temp;
	// 버블 정렬 알고리즘을 이용한 오름차순 정렬
	for (int i = 0; i < num; i++) {
		for (int j = 0; j < num - i - 1; j++) {
			if (number[j] > number[j + 1]) {
				temp = number[j];
				number[j] = number[j + 1];
				number[j + 1] = temp;
			}
		}
	}
	printf("\n* Sorted Data**\n   ");
	// 버블 정렬 알고리즘을 이용해 정렬된 배열을 출력
	for (int i = 0; i < 20; i++) {
		// 정렬된 배열의 아이템을 10개 기준으로 개행해주기 위한 조건문
		if (i == 10) { printf("\n   "); }
		printf("%d ", number[i]);
	}

	// 최소값 중간값 최대값 평균 출력
	float ave;
	float sum = 0;
	for (int i = 0; i < 20; i++) {
		sum += number[i];
		ave = sum / 20;
	}
	printf("Min = %d, Max = %d, Med = %.2f, Ave = %.2f", number[0], number[19], ((float)number[9] + (float)number[10])/2, ave);
}