#include <stdio.h>
#include <time.h>
#include <string.h>
#include <stdlib.h>

/*---------------------------------------------------------------------------------------
* ���� : main.cpp
* ��� : �߰����
* ������ : �ڼ���
* ���߽��� : 2020-05-08
* �������� : 2020-05-08 (Pass)
---------------------------------------------------------------------------------------*/

//function pakage
int test_leap_year(int year);                //���� �Ǻ�
int date_sum(int y, int m, int d);        //�ش� ����� ���� ��¥���� ��¥ ���

int main()
{
	time_t t = time(NULL);
	struct tm tm = *localtime(&t);

	int y = tm.tm_year + 1900;
	int m = tm.tm_mon + 1;
	int d = tm.tm_mday;   // ���� ��¥

	int b_y, b_m, b_d;                                //�������
	int t_sum = 0;                                        //��ƿ³��� ��
	int test;                                                //��� �Ǻ�
	char born[30];
	char* reborn[3] = { NULL, };
	int i = 0;
	printf("* Days of Life **\nEnter the Day 1 (as yyyy/mm/dd) : ");
	// �¾ ��¥ �Է¹ޱ�
	scanf("%s", born);

	char* ptr = strtok(born, "/");

	while (ptr != NULL)
	{
		reborn[i] = ptr;
		i++;

		ptr = strtok(NULL, "/");
	}
	b_y = atoi(reborn[0]);
	b_m = atoi(reborn[1]);
	b_d = atoi(reborn[2]);
	//��ƿ� ���� �� ���
	for (i = b_y; i < y; i++)
	{
		t_sum += date_sum(i, 12, 31);
	}
	t_sum += date_sum(y, m, d);                        //������� ��¥ ����
	t_sum -= date_sum(b_y, b_m, b_d - 1);        //����1��1�Ϻ��� �¾ ������ ���� ����

	printf("\t--> The Day %d of Life\n", t_sum);
}

int test_leap_year(int year)
{
	if (year % 4 == 0) {
		if (year % 100 == 0) {
			if (year % 400 == 0)
				return 0;                        //����
			else
				return 1;
		}
		else
			return 0;                                //����
	}
	else
		return 1;                                        //���        
}

int date_sum(int y, int m, int d)
{
	int sum = 0;
	int i;
	int test = test_leap_year(y);

	for (i = 1; i < m; i++)
	{
		if (i == 1 || i == 3 || i == 5 || i == 7 || i == 8 || i == 10 || i == 12)
			sum += 31;
		else if (i == 2)
		{
			if (test == 1)                        //�ش� ������ ����� ���
				sum += 28;
			else
				sum += 29;                //�ش� ������ ������ ���
		}
		else
			sum += 30;
	}
	sum += d;                                                //���� ��¥ ����
	return sum;
}