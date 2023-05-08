#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list is circular
 * @list: A singly-linked list
 *
 * Return: - 0 if no cycle or 1 if there is one
 */
int check_cycle(listint_t *list)
{
	listint_t *check, *cycle;

	if (list == NULL || list->next == NULL)
		return (0);

	check = list->next;
	cycle = list->next->next;

	while (check && cycle && cycle->next)
	{
		if (check == cycle)
			return (1);

		check = check->next;
		cycle = cycle->next->next;
	}

	return (0);
}

