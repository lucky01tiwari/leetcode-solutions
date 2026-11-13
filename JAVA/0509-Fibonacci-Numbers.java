package JAVA;

class Solution {
    public int fib(int n) {
        int sum =0;//n==2 
        if (n <= 1) return n;
        return fib(n - 1) + fib(n - 2);
    }
}