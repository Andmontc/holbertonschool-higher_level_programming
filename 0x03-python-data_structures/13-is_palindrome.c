#include "lists.h"
/**
 * is_palindrome - function that checks a palindrome
 * @head: list
 * Return: 0 not 1 palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int i = 0, j;
	int arr[10000];

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (tmp)
	{
		arr[i] = tmp->n;
		i++;
		tmp = tmp->next;
	}
	for (j = 0; j <= (i - 1); j++, i--)
	{
		if (arr[i] != arr[j])
			return (1);
	}
	return (0);
}
