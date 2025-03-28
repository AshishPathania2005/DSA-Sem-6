import java.util.*;

public class MaxTotalEnergy {
    static final int MOD = 1000000007;
    
    public static int maxEnergy(int N, int K, int[] E, int[] P) {
        Arrays.sort(P); // Sort P to ensure optimal selection
        int totalEnergy = 0;
        
        for (int i = 0; i < K / 2; i++) {
            int start = P[i];
            int end = P[K - i - 1];
            
            if (start > end) {
                int temp = start;
                start = end;
                end = temp;
            }
            
            int sum = 0;
            for (int j = start; j <= end; j++) {
                sum = (sum + E[j]) % MOD;
            }
            
            totalEnergy = (totalEnergy + sum) % MOD;
        }
        
        return totalEnergy;
    }

    public static void main(String[] args) {
        int N = 5, K = 4;
        int[] E = {2, 5, 10, 9, 3};
        int[] P = {2, 3, 0, 1};
        
        System.out.println(maxEnergy(N, K, E, P)); // Output: 41
    }
}
