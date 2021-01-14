#include <stdio.h>
#pragma warning(disable:4996)

int main() {
	/*---------------------------------------------------------------------------------------
	* 파일 : main.cpp
	* 기능 : 중간고사
	* 개발자 : 박수하
	* 개발시작 : 2020-05-08
	* 개발종료 : 2020-05-08 (Pass)
	---------------------------------------------------------------------------------------*/
	int a;
	scanf(" %d", &a);
	int arr[100] = { 0, };
	int arrs[100] = { 0, };
	arr[0] = 1;
	int count = 1;

	for (int k = 0; k < a; k++) {
		int i = 0, j = 1;
		int kc = 0;

		while (1) {
			printf("%d", arr[i]);
			arrs[kc] = arr[i];
			kc++;
			if (k == 0) {
				break;
			}

			while (1) {
				if (arr[i] == arr[j]) {
					count++;
					i++; j++;
				}
				else {
					printf("%d", count);
					arrs[kc] = count;
					kc++;
					count = 1;
					i++; j++;
					break;
				}
			}
			if (arr[i] == 0) {
				break;
			}
		}
		printf("\n");
		for (int c = 0; c < 100; c++) {
			arr[c] = arrs[c];
		}
	}
	return 0;
}