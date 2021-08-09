import java.util.HashMap;
import java.util.HashSet;
import java.util.Stack;

class SolutionpPalindrome{
    public int singleNumber(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }

        HashMap<Integer, Integer> hashMap = new HashMap<Integer, Integer>();

        // 把元素加入到Hashmap
        for (int i : nums) {
            // put 添加元素 nums里的元素为key，
            // getOrDefault查看i 是否存在，如果没有返回默认值0, 如何有Key返回对应的值
            hashMap.put(i, hashMap.getOrDefault(i, 0) + 1);
            System.out.printf("遍历的数字为： %d\n", i);
            System.out.printf("查看的结果为： %d\n", hashMap.getOrDefault(i, 0));
            System.out.println(hashMap);
        }

        System.out.println(hashMap.size());

        //  遍历
        for (int i : hashMap.keySet()) {
            // get 取出HashMap的值
            if (hashMap.get(i) == 1) {
                return i;
            }
        }
        return 0;
    }

    public int solutionHashSet(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }

        HashSet<Integer> hset = new HashSet<>();

        for (int i : nums) {
            if (hset.contains(i)) {
                hset.remove(i);
            } else {
                hset.add(i);
            }
        }
        return hset.iterator().next();
    }
    
    public int solutionStack(int[] nums){
        if (nums.length == 1) {
            return nums[0];
        }

        Stack<Integer> stackList = new Stack<>();
        for (Integer integer : nums) {
            if (stackList.isEmpty()) {
                stackList.push(integer);
                continue;
            }

            if (stackList.peek() != integer) {
                break;
            }

            stackList.pop();
        }

        return stackList.pop();
    }
    
    public static void main(String[] args) {
        int[] nums = { 1, 2, 3, 4, 5, 3, 4, 1, 2 };
        SolutionpPalindrome solutionpPalindrome = new SolutionpPalindrome();
        System.out.println(solutionpPalindrome.singleNumber(nums));
    }
}