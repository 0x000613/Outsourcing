import java.util.Scanner;
public class A1 {
    public void getInput() {
        Scanner scan = new Scanner(System.in);

        // 첫 번째 수 입력받기
        System.out.println("첫 번째 수 입력:");
        int start = scan.nextInt();
        
        // 두 번째 수 입력받기
        System.out.println("두 번째 수 입력:");
        int end = scan.nextInt();

        // nextInt 함수 사용 직후 nextLine 함수 사용시 공백으로 인한 에러 발생을 방지하기 위한 코드
        scan.nextLine();
        
        // 연산자 입력받기 (nextLine함수를 이용해 다음 입력을 저장함)
        // 연산자는 Char데이터형의 한 글자이기때문에 CharAt(0)을 이용해 가져옴
        System.out.println("연산자 입력:");
        char op = scan.nextLine().charAt(0);
        

        A2 am = new A2();

        // result 변수에 makeSum 함수의 return value를 저장
        int result = am.makeSum(start, end, op);

        // 입력받은 정보, 계산한 정보를 기반으로 시작값, 종료값, 합 출력
        System.out.println("시작값 : " + start);
        System.out.println("종료값 : " + end);
        System.out.println("합은 :" + result);
    }

    public class A2 {
        public int makeSum(int startValue, int endValue, char op) {
            // 시작값은 makeSum 함수에서 인자로 받은 startValue를 int형으로 사용
            int start = startValue;
            // 종료값은 makeSum 함수에서 인자로 받은 endValue를 int형으로 사용
            int end = endValue;
            // 결과값 초기화
            int sum = 0;

            // 연산자가 '*'일 경우
            if(op == '*'){sum = sum * end;}
            // 연산자가 '/'일 경우
            else if(op == '/'){sum = start / end;}
            // 연산자가 '+'일 경우
            else if(op == '+'){sum = start + end;}
            // 연산자가 '-'일 경우
            else if(op == '-'){sum = start - end;}
            
            // 계산한 sum 변수를 return
            return sum;
        }
    }

    public static void main(String[] args) {
        A1 ui = new A1();
        ui.getInput();
    }
}