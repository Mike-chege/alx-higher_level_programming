#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

int is_palindrome(listint_t **head);
listint_t *reverse_listint(listint_t **head);

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: pointer to the head of the linked list.
 * Return: 0 if not palindrome otherwise 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *first, *second, *middle;
	size_t length = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	first = *head;
	while (first)
	{
		length++;
		first = first->next;
	}

	first = *head;
	for (i = 0; i < (length / 2) - 1; i++)
		first = first->next;

	if ((length % 2) == 0 && first->n != first->next->n)
		return (0);

	first = first->next->next;
	second = reverse_listint(&first);
	middle = second;

	first = *head;
	while (second)
	{
		if (first->n != second->n)
			return (0);
		first = first->next;
		second = first->next;
	}
	reverse_listint(&middle);

	return (1);
}


/**
 * reverse_listint - Reverses a singly-linked listint_t list
 * @head: pointer to the starting node of the list to reverse
 * Return: pointer to the head of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *s_node = *head, *next, *prev = NULL;

	while (node)
	{
		next = s_node->next;
		s_node->next = prev;
		prev = s_node;
		s_node = next;
	}

	*head = prev;
	return (*head);
}

