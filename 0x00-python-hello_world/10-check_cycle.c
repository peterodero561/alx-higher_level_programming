#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a given linked list
 * @list: head of the linked list
 *
 * Return: 0 if there is no cycle && 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *current, *fast;

	current = list;
	fast = list;
	while (current != NULL && fast != NULL && fast->next != NULL)
	{
		current = current->next;
		fast = fast->next->next;
		if (current == fast)
			return (1);
	}
	return (0);
}
