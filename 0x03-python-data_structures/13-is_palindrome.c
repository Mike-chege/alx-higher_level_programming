#include "lists.h"
#include <stdio.h>

void reverse_list(listint_t **head);
int list_identical(listint_t *l1, listint_t *l2);

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 0 if not palindrome 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *skip_1, *skip_2, *prev_s1, *first_half, *second_half, *mid;

	if (!head || !(*head) || !((*head)->next))
		return (1);

	first_half = skip_1 = skip_2 = prev_s1 = *head;
	second_half = mid = NULL;

	while (skip_1 && skip_2 && skip_2->next)
	{
		prev_s1 = skip_1;
		skip_1 = skip_1->next;
		skip_2 = skip_2->next->next;
	}
	if (skip_2 == NULL)
		second_half = skip_1;
	else
	{
		mid = skip_1;
		second_half = skip_1->next;
	}
	prev_s1->next = NULL;
	reverse_list(&second_half);

	if (list_equiv(first_half, second_half))
		return (1);
	else
		return (0);
}

/**
 * list_identical - checks if two linked lists contain identical elements
 * @l1: list one to compare to list two
 * @l2: list two to compare to list one
 * Return: 1 if identical, 0 if not dentical
 */
int list_identical(listint_t *l1, listint_t *l2)
{
	while (l1 || l2)
	{
		if (l1->n != l2->n || !l1 || !l2)
			return (0);
		if (l1)
			l1 = l1->next;
		if (l2)
			l2 = l2->next;
	}
	return (1);
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to head of linked list
 * Return: Nothing
 */
void reverse_list(listint_t **head)
{
	listint_t *next = NULL, *prev = NULL, *new;

	new = *head;
	while (new)
	{
		next = new->next;
		new->next = prev;
		prev = new;
		new= next;
	}
	*head = prev;
}

