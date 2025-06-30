// Time Complexity : O(n log k)
//  Space Complexity : Auxiliary O(k) : for the heap
//Did this code successfully run on Leetcode : Yes
//Any problem you faced while coding this : No
// Three line explanation of solution in plain english:
//1. We use a max heap to keep track of the k smallest elements.
//2. We iterate through all elements in the matrix, adding each element to the heap.
//3. If the heap size exceeds k, we remove the largest element to maintain the k smallest elements.


class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        // Create a max heap (priority queue with reverse order)
        // This will store the k smallest elements encountered so far
        PriorityQueue<Integer> heapQ = new PriorityQueue<Integer>(Collections.reverseOrder());

        int n = matrix.length;

        // Iterate through every element in the matrix
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                int ele = matrix[r][c];

                // Add the current element to the max heap
                heapQ.add(ele);

                // If the heap size exceeds k, remove the largest element
                // This ensures that the heap only contains the k smallest elements
                while (heapQ.size() > k) {
                    heapQ.poll();  // Remove the largest element in the max heap
                }
            }
        }

        // Optional: Print the heap contents (for debugging)
        System.out.println(heapQ);

        // The root of the max heap is the kth smallest element
        return heapQ.peek();
    }
}
