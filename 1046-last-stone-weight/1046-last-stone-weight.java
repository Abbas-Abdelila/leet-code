class Solution {
    public int lastStoneWeight(int[] stones) {
        
        PriorityQueue<Integer> pqueue = new PriorityQueue<>(Collections.reverseOrder());
        for(int num : stones) {
            pqueue.add(num);
        }
        
        while(pqueue.size()>1) {
            
            int x = pqueue.remove();
            int y = pqueue.remove();
            
            if(x==y) {
                continue;
            }
            else if( x!=y) {
                pqueue.add(x-y);
            }
                
        }
        
        if(pqueue.size()==0) 
            return 0;
        return pqueue.remove();

        
        
    }
}