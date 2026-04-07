/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeNodes(struct ListNode* head) {
    struct ListNode *write = head;
    struct ListNode *read = head->next;
    int temp_sum = 0;

    while (read) {
        if (read->val == 0) {
            write->val = temp_sum;
            temp_sum = 0;
            if (read->next) {
                write = write->next;
            }
        } else {
            temp_sum += read->val;
        }
        read = read->next;
    }
    write->next = NULL;

    return head;
}