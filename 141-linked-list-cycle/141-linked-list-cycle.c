/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    
     struct ListNode *s=head, *f=head;
        while(s!=NULL && f!=NULL){
            s=s->next;
            f=f->next;
            if(f!=NULL){
                f=f->next;
                if(s==f){
                    return true;
                }
            }
        }
        return false;
    }
    
