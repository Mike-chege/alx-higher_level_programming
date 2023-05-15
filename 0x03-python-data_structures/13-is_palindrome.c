#include "lists.h"
#include <stdio.h>

void reverse_list(listint_t **head);
int list_equiv(listint_t *l1, listint_t *l2);

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 0 if not palindrome otherwise 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *first_1, *second_2, *prevf, *top_half, *second_half, *mid;

	if (!head || !(*head) || !((*head)->next))
		return (1);

	first_half = first_1 = second_2 = prevf = *head;
	second_half = mid = NULL;

	while (first_1 && second_2 && second_2->next)
	{
		prevf = first_1;
		first_1 = first_1->next;
		second_2 = second_2->next->next;
	}
	if (second_2 == NULL)
		second_half = first_1;
	else
	{
		mid = first_1;
		second_half = first_1->next;
	}
	prevf->next = NULL;
	reverse_list(&second_half);

	if (list_identical(top_half, second_half))
		return (1);
	else
		return (0);
}

/**
 * list_identical - checks if two linked lists contain identical data
 * @l1: list one to compare to list two
 * @l2: list two to compare to list one
 * Return: 1 if equivalent 0 if not equal
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
 * @head: double pointer to head of linked list
 * Return: void
 */
void reverse_list(listint_t **head)
{
	listint_t *next = NULL, *prev = NULL, *s_node;

	s_node = *head;
	while (s_node)
	{
		next = s_node->next;
		s_node->next = prev;
		prev = s_node;
		s_node = next;
	}
	*head = prev;
}
