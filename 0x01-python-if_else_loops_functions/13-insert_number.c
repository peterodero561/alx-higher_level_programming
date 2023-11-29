#include "lists.h"

/**
 * insert_node - inserts node to a sorted linked list
 * @head: pointer to the head of the linked list
 * @number: value of the node to be inserted in the linked list
 *
 * Return: Address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	
	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
		{
			if (current->next->n > number)
			{
				new->next = current->next;
				current->next = new;
				return (new);
			}
			else
				current = current->next;
		}
		current->next = new;
	}
	return (new);
}
