import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.*;

public class 이친수_2193 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        long[] pNum = new long[N+1];

        pNum[0]=0;
        pNum[1]=1;

        for(int i = 2; i <= N; i++){
            pNum[i] = pNum[i-1] + pNum[i-2];
        }

        System.out.println(pNum[N]);
    }
}
