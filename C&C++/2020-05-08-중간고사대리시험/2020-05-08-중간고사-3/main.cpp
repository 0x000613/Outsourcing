// num�� 20���� ��������
#define num 20
#include <stdio.h>
#include <math.h>

int main()
{
	/*---------------------------------------------------------------------------------------
	* ���� : main.cpp
	* ��� : �߰����
	* ������ : �ڼ���
	* ���߽��� : 2020-05-08
	* �������� : 2020-05-08 (Pass)
	---------------------------------------------------------------------------------------*/
	printf("*** Sorting ****\n");
	// ���̰� 20�� �迭 ����
	int number[num]{ 42, 68, 35, 1, 70, 25, 79, 59, 63, 65, 6, 46, 82, 28, 62, 92, 96, 43, 28, 37 };

	// �����ϱ� ���� �迭�� ���
	printf("** Given Data **\n   ");
	for (int i = 0; i < 20; i++) {
		// �迭�� �������� 10�� �������� �������ֱ� ���� ���ǹ�
		if (i == 10) { printf("\n   "); }
		printf("%d ", number[i]);
	}

	// ������ �ϱ����� ���� ����
	int temp;
	// ���� ���� �˰����� �̿��� �������� ����
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
	// ���� ���� �˰����� �̿��� ���ĵ� �迭�� ���
	for (int i = 0; i < 20; i++) {
		// ���ĵ� �迭�� �������� 10�� �������� �������ֱ� ���� ���ǹ�
		if (i == 10) { printf("\n   "); }
		printf("%d ", number[i]);
	}

	// �ּҰ� �߰��� �ִ밪 ��� ���
	float ave;
	float sum = 0;
	for (int i = 0; i < 20; i++) {
		sum += number[i];
		ave = sum / 20;
	}
	printf("Min = %d, Max = %d, Med = %.2f, Ave = %.2f", number[0], number[19], ((float)number[9] + (float)number[10])/2, ave);
}