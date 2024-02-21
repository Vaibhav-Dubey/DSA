// here we are trying to add two numbers without using the + operator, and this is problem number #371 on leetcode

Class Solution{
    public int getSum(int a, int b){
        while(b!=0){
            temp = (a&b)<<1;
            a=a^b;
            b=temp;
        }
        return a;
    }
}