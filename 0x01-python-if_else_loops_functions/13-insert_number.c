#include "lists.h"
/**
 * insert_node - function that inserts a node in and index
 * @head: pointer to pointer to the head of the list
 * @number: index
 * Return: new list box
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *pos = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	if (pos == 0 || pos->n >= number)
	{
		new->next = pos;
		*head = new;
		return (new);
	}
	while (pos && pos->next && pos->next->n < number)
		pos = pos->next;

	new->next = pos->next;
	pos->next = new;
	return (new);
}
