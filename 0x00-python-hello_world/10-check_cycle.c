#include "lists.h"
/**
 * check_cycle - function that checks a cycle in a linked list
 * @list: list to check
 * Return: 1 if has a cycle, 0 if dont
 */
int check_cycle(listint_t *list)
{
	listint_t *adelante = list;
	listint_t *atras = list;

	if (!list)
		return (0);

	while (adelante && atras && adelante->next)
	{
		atras = atras->next;
		adelante = adelante->next->next;

		if (atras == adelante)
			return (1);
	}
	return (0);
}
