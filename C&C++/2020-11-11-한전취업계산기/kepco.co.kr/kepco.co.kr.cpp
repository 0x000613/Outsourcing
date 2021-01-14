#include <iostream>
#include <string>
#include <cstring>

using namespace std;

// 문자열 비교 함수
bool stringCompare(string p1, const char* p2)
{
	int length1 = strlen(p1.c_str());
	int length2 = strlen(p2);

	if (length1 != length2)
	{
		return false;
	}

	for (int i = 0; i != 0; i += 1)
	{
		if (p1.c_str()[i] != p2[i])
		{
			return false;
		}
	}

	return true;
}

string scoring(float limitPoint, float myPoint)
{
	if (myPoint >= limitPoint)
	{
		return "합격";
	}
	else if(myPoint < limitPoint)
	{
		return "불합격";
	}
}

int main()
{
	string region;
	string myStringPoint;
	int point = 0;
	int myPoint = 0;
	// 지원자격 조건문 시작 //
	string answer;
	string answerY("예");
	string answerN("아니오");

	cout << "반갑습니다. 한국전력공사 전기 직 서류점수 계산기 입니다." << endl;
	cout << "전기관련 학과입니까?(예/아니오): ";
	cin >> answer;

	if (answer == answerY)
	{
	success:
		system("cls");
		cout << "외국어 성적을 갖고 계십니까?(예/아니오): ";
		cin >> answer;
		if (answer == answerY)
		{
			system("cls");
			cout << "만 60세가 넘으셨습니까?(예/아니오): ";
			cin >> answer;
			if (answer == answerY)
			{
				goto fail;
			}
			else if (answer == answerN)
			{
				system("cls");
				cout << "병역의무를 불이행하셨습니까?(예/아니오): ";
				cin >> answer;
				if (answer == answerY)
				{
					goto fail;
				}
				else if (answer == answerN)
				{
					cout << "한국전력공사 전기직 지원가능 대상입니다." << endl;
				}
				else
				{
					goto error;
				}
			}
		}
		else if (answer == answerN)
		{
			goto fail;
		}
	}
	else if (answer == answerN)
	{
		system("cls");
		cout << "전기관련 산업기사 이상 자격증이 있으십니까?(예/아니오): ";
		cin >> answer;
		if (answer == answerY)
		{
			goto success;
		}
		else if (answer == answerN)
		{
		fail:
			cout << "한국전력공사 전기직 지원 자격이 아닙니다." << endl;
			return 0;
		}
	}
	else
	{
	error:
		cout << "잘못 입력하셨습니다. 프로그램을 다시 실행해주세요" << endl;
		return 0;
	}

	// 지원자격 조건문 종료 //
	// 외국어 성적 조건문 시작 //
	system("cls");
	string cf;
	cout << "[ TOEIC, TOEICSPEAKING, OPIC, TEPS, NEWTEPS ]\n취득하신 외국어 성적의 종류를 위 보기중 선택해 입력해주세요: ";
	cin >> cf;

	if (stringCompare(cf, "TOEIC"))
	{
		cout << "850점이 넘습니까?(예/아니오): ";
	}
	else if (stringCompare(cf, "TOEICSPEAKING"))
	{
		cout << "150점이 넘습니까?(예/아니오): ";
	}
	else if (stringCompare(cf, "OPIC"))
	{
		cout << "IM3 이상입니까?(예/아니오): ";
	}
	else if (stringCompare(cf, "TEPS"))
	{
		cout << "695점이 넘습니까?(예/아니오): ";
	}
	else if (stringCompare(cf, "NEWTEPS"))
	{
		cout << "383점이 넘습니까?(예/아니오): ";
	}
	cin >> answer;
	if (stringCompare(answer, "예"))
	{
		point += 100;
	}
	else if (stringCompare(answer, "아니오"))
	{
		cout << "점수를 입력해주세요: ";
		cin >> myPoint;
		if (stringCompare(cf, "TOEIC"))
		{
			point += (myPoint / 990) * 100;
		}
		else if (stringCompare(cf, "TOEICSPEAKING"))
		{
			cout << "점수를 입력해주세요: ";
			cin >> myPoint;
			switch (myPoint)
			{
			case 120:
				point += (703.5 / 900) * 100;
				break;
			case 130:
				point += (773.5 / 900) * 100;
				break;
			case 140:
				point += (831.3 / 900) * 100;
				break;
			case 150:
				point += (871.3 / 900) * 100;
				break;
			case 160:
				point += (907.3 / 900) * 100;
				break;
			case 170:
				point += (936.7 / 900) * 100;
				break;
			case 180:
				point += (958.9 / 900) * 100;
				break;
			case 190:
				point += (982 / 900) * 100;
				break;
			case 200:
				point += (990 / 900) * 100;
				break;
			}
		}
		else if (stringCompare(cf, "OPIC"))
		{
			cout << "점수를 입력해주세요: ";
			cin >> myStringPoint;
			if (stringCompare(myStringPoint, "IM3"))
			{
				point += (860.9 / 900) * 100;
			}
			else if (stringCompare(myStringPoint, "IM2"))
			{
				point += (765.8 / 900) * 100;
			}
		}
		else if (stringCompare(cf, "TEPS"))
		{
			cout << "점수를 입력해주세요: ";
			cin >> myPoint;
			if (myPoint >= 688 && myPoint <= 694) point += (845 / 900) * 100;
			else if (myPoint >= 681 && myPoint <= 687) point += (840 / 900) * 100;
			else if (myPoint >= 675 && myPoint <= 680) point += (835 / 900) * 100;
			else if (myPoint >= 669 && myPoint <= 674) point += (830 / 900) * 100;
			else if (myPoint >= 675 && myPoint <= 680) point += (825 / 900) * 100;
			else if (myPoint >= 663 && myPoint <= 668) point += (820 / 900) * 100;
			else if (myPoint >= 658 && myPoint <= 662) point += (815 / 900) * 100;
			else if (myPoint >= 652 && myPoint <= 657) point += (810 / 900) * 100;
			else if (myPoint >= 647 && myPoint <= 651) point += (805 / 900) * 100;
			else if (myPoint >= 642 && myPoint <= 646) point += (800 / 900) * 100;
			else if (myPoint >= 637 && myPoint <= 641) point += (795 / 900) * 100;
			else if (myPoint >= 632 && myPoint <= 636) point += (790 / 900) * 100;
			else if (myPoint >= 628 && myPoint <= 631) point += (785 / 900) * 100;
			else if (myPoint >= 623 && myPoint <= 627) point += (780 / 900) * 100;
			else if (myPoint >= 619 && myPoint <= 622) point += (775 / 900) * 100;
			else if (myPoint >= 615 && myPoint <= 618) point += (770 / 900) * 100;
			else if (myPoint >= 611 && myPoint <= 614) point += (765 / 900) * 100;
			else if (myPoint >= 606 && myPoint <= 610) point += (760 / 900) * 100;
			else if (myPoint >= 602 && myPoint <= 605) point += (755 / 900) * 100;
			else if (myPoint >= 598 && myPoint <= 601) point += (750 / 900) * 100;
			else if (myPoint >= 594 && myPoint <= 597) point += (745 / 900) * 100;
			else if (myPoint >= 590 && myPoint <= 593) point += (740 / 900) * 100;
			else if (myPoint >= 585 && myPoint <= 589) point += (735 / 900) * 100;
			else if (myPoint >= 581 && myPoint <= 584) point += (730 / 900) * 100;
			else if (myPoint >= 577 && myPoint <= 580) point += (725 / 900) * 100;
			else if (myPoint >= 573 && myPoint <= 576) point += (720 / 900) * 100;
			else if (myPoint >= 569 && myPoint <= 572) point += (715 / 900) * 100;
			else if (myPoint >= 562 && myPoint <= 568) point += (710 / 900) * 100;
			else if (myPoint >= 558 && myPoint <= 561) point += (705 / 900) * 100;
			else if (myPoint >= 555 && myPoint <= 557) point += (700 / 900) * 100;

		}
		else if (stringCompare(cf, "NEWTEPS"))
		{
			cout << "점수를 입력해주세요: ";
			cin >> myPoint;
			if (myPoint >= 379 && myPoint <= 382) point += (845 / 900) * 100;
			else if (myPoint >= 374 && myPoint <= 378) point += (840 / 900) * 100;
			else if (myPoint >= 371 && myPoint <= 373) point += (835 / 900) * 100;
			else if (myPoint >= 366 && myPoint <= 370) point += (830 / 900) * 100;
			else if (myPoint >= 362 && myPoint <= 365) point += (825 / 900) * 100;
			else if (myPoint >= 360 && myPoint <= 361) point += (820 / 900) * 100;
			else if (myPoint >= 356 && myPoint <= 359) point += (815 / 900) * 100;
			else if (myPoint >= 353 && myPoint <= 355) point += (810 / 900) * 100;
			else if (myPoint >= 351 && myPoint <= 352) point += (805 / 900) * 100;
			else if (myPoint >= 348 && myPoint <= 350) point += (800 / 900) * 100;
			else if (myPoint >= 344 && myPoint <= 347) point += (795 / 900) * 100;
			else if (myPoint >= 342 && myPoint <= 343) point += (790 / 900) * 100;
			else if (myPoint >= 340 && myPoint <= 341) point += (785 / 900) * 100;
			else if (myPoint >= 336 && myPoint <= 339) point += (780 / 900) * 100;
			else if (myPoint >= 334 && myPoint <= 335) point += (775 / 900) * 100;
			else if (myPoint >= 332 && myPoint <= 333) point += (770 / 900) * 100;
			else if (myPoint >= 330 && myPoint <= 331) point += (765 / 900) * 100;
			else if (myPoint >= 328 && myPoint <= 329) point += (760 / 900) * 100;
			else if (myPoint >= 325 && myPoint <= 327) point += (755 / 900) * 100;
			else if (myPoint >= 322 && myPoint <= 324) point += (750 / 900) * 100;
			else if (myPoint >= 320 && myPoint <= 321) point += (745 / 900) * 100;
			else if (myPoint >= 317 && myPoint <= 319) point += (740 / 900) * 100;
			else if (myPoint >= 315 && myPoint <= 316) point += (735 / 900) * 100;
			else if (myPoint >= 312 && myPoint <= 314) point += (730 / 900) * 100;
			else if (myPoint >= 310 && myPoint <= 311) point += (725 / 900) * 100;
			else if (myPoint >= 308 && myPoint <= 309) point += (720 / 900) * 100;
			else if (myPoint >= 306 && myPoint <= 307) point += (715 / 900) * 100;
			else if (myPoint >= 304 && myPoint <= 305) point += (710 / 900) * 100;
			else if (myPoint >= 302 && myPoint <= 303) point += (705 / 900) * 100;
			else if (myPoint >= 300 && myPoint <= 301) point += (700 / 900) * 100;
		}
	}
	// 외국어 성적 조건문 종료 //
	// 자격증 가점 조건문 시작 //
	system("cls");
	cout << "[ 한국사, 국어능력, IT분야, 외국어, 없음 ]\n위 보기중 취득하신 자격증의 종류를 입력해주세요: ";
	cin >> cf;
	if (stringCompare(cf, "한국사"))
	{
		cout << "한국사능력검정시험 3급 이상입니까?(예/아니오): ";
		cin >> answer;
		if (stringCompare(answer, "예"))
		{
			point += 5;
		}
	}
	else if (stringCompare(cf, "국어능력"))
	{
		cout << "국어능력인증3급, KBS한국어능력 3+급, 한국실용 글쓰기 준2급 이상입니까?(예/아니오): ";
		cin >> answer;
		if (stringCompare(answer, "예"))
		{
			point += 5;
		}

	}
	else if (stringCompare(cf, "IT분야"))
	{
		cout << "정보처리기사, 정보처리산업기사, 사무자동화 산업기사, 컴퓨터활용능력 1급 이상입니까?(예/아니오): ";
		cin >> answer;
		if (stringCompare(answer, "예"))
		{
			point += 5;
		}

	}
	else if (stringCompare(cf, "외국어"))
	{
		cout << "TOEIC SPEAKING 7등급, OPIC IH등급, FLEX 1C등급 이상입니까?(예/아니오): ";
		cin >> answer;

		if (stringCompare(answer, "예"))
		{
			point += 5;
		}
	}

	system("cls");
	cout << "전기분야 기사자격증을 갖고 계십니까?(예/아니오): ";
	cin >> answer;
	if (stringCompare(answer, "예"))
	{
		cout << "[ 전기기사, 전기공사기사, 전자기사, 품질경영기사, 산업안전기사, 소방설비(전기)기사, 없음 ]\n위 보기중 취득하신 자격증의 종류를 입력해주세요: ";
		cin >> cf;
		if (stringCompare(cf, "전기기사") || stringCompare(cf, "전기공사기사"))
		{
			point += 10;
		}
		else if (stringCompare(cf, "전자기사") || stringCompare(cf, "품질경영기사") || stringCompare(cf, "산업안전기사") || stringCompare(cf, "소방설비(전기)기사"))
		{
			point += 8;
		}
	}
	else if (stringCompare(answer, "아니오"))
	{
		cout << "전기분야 산업기사자격증을 갖고 계십니까?(예/아니오): ";
		cin >> answer;
		if (stringCompare(answer, "예"))
		{
			cout << "[ 전기산업기사, 전기공사산업기사, 전자산업기사, 품질경영산업기사, 산업안전산업기사, 소방설비(전기)산업기사, 없음 ]\n위 보기중 취득하신 자격증을 입력해주세요: ";
			cin >> cf;

			if (stringCompare(cf, "전기산업기사") || stringCompare(cf, "전기공사산업기사"))
			{
				point += 5;
			}
			else if (stringCompare(cf, "전자산업기사") || stringCompare(cf, "품질경영산업기사") || stringCompare(cf, "산업안전산업기사") || stringCompare(cf, "소방설비(전기)산업기사"))
			{
				point += 3;
			}
		}
	}

	system("cls");
	cout << "[ 비수도권및본사이전지역인재, 취업지원대상자, 장애인, 한전체험형청년인턴, KEPCO일렉트론경진대회수상자]\n[한전발명특허대전입상자, KEPCO대학생서포터즈우수활동자, 한전시간선택제근로자, 정규직전환대상직무기간제근로자, 없음 ]\n위 보기중 해당사항이 있으면 입력해주세요: ";
	cin >> cf;
	if (stringCompare(cf, "비수도권및본사이전지역인재"))
	{
		cout << "이전지역입니까?(예/아니오): ";
		cin >> answer;
		if (stringCompare(answer, "예"))
		{
			point += 10;
		}
		else if (stringCompare(answer, "아니오"))
		{
			point += 5;
		}
	}
	else if (stringCompare(cf, "취업지원대상자") || stringCompare(cf, "장애인") || stringCompare(cf, "한전체험형청년인턴"))
	{
		point += 5;
	}
	else if (stringCompare(cf, "KEPCO일렉트론경진대회수상자") || stringCompare(cf, "한전발명특허대전입상자") || stringCompare(cf, "KEPCO대학생서포터즈우수활동자") || stringCompare(cf, "한전시간선택제근로자") || stringCompare(cf, "정규직전환대상직무기간제근로자"))
	{
		point += 10;
	}
	system("cls");
	string pointString = to_string(point);
	cout << "나의 최종 점수:" + pointString  + "점"<< endl;
	cout << "전국권<합격기준: 115.8>: " + scoring(115.8, point);
	cout << "경기북부<합격기준: 115>: " + scoring(115, point);
	cout << "대구<합격기준: 119.8>: " + scoring(119.8, point);
	cout << "대세충<합격기준: 115>: " + scoring(115, point);
	cout << "경북<합격기준: 114>: " + scoring(114, point);
	cout << "광주전남<합격기준: 105>: " + scoring(105, point);
	cout << "전북<합격기준: 110.88>: " + scoring(110.88, point);
	cout << "제주<합격기준: 118>: " + scoring(118, point);
	cout << "강원<합격기준: 112>: " + scoring(112, point);
	cout << "충북<합격기준: 111.6>: " + scoring(111.6, point);
	cout << "경남<합격기준: 118>: " + scoring(118, point);
}