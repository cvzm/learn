package CodeWars;

/**
 * @description: 数字中的质因数
 * @author: C.v.
 * @date: 2018-12-09
 */
public class Primes_in_numbers_Cv {


    public static String factors(int n) {
        StringBuffer sb = new StringBuffer();
        rho(n, sb);
        addPrimes(0, sb);
        return sb.toString();
    }

    /**
     * Pollard Rho因数分解
     * @param n 待分解的数
     */
    private static void rho(int n, StringBuffer sb) {
        if (n < 2) return;
        for (int i=2; i<=Math.sqrt(n); i++) {
            while (n != i) {
                if (n%i != 0) break;//不能整除肯定不是因数
                addPrimes(i, sb);
                n = n/i;
            }
        }
        addPrimes(n, sb);
    }

    /**
     * 输出格式处理
     */
    private static int lastPrimes, count;

    private static void addPrimes(int k, StringBuffer sb) {
        if (lastPrimes == k) {
            count++;
            return;
        }
        if (lastPrimes != 0) sb.append(count == 1 ? "(" + lastPrimes+ ")" : "(" + lastPrimes + "**" + count + ")");

        lastPrimes = k;
        count = 1;
    }

    public static void main (String[] args) {
        int n = 7775460;
        System.out.println(factors(n));
        System.out.println(Math.sqrt(22));
    }
}
