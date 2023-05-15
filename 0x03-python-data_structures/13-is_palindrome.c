#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

void reverse_list(listint_t **head);
int list_identical(listint_t *list1, listint_t *list2);

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 0 if not palindrome 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *first_1, *second_2, *prev_l, *first_top, *second_top, *middle;

	if (!head || !(*head) || !((*head)->next))
		return (1);

	first_top = first_1 = second_2 = prev_l = *head;
	second_top = middle = NULL;

	while (first_1 && second_2 && second_2->next)
	{
		prev_l = first_1;
		first_1 = first_1->next;
		second_2 = second_2->next->next;
	}
	if (second_2 == NULL)
		second_top = first_1;
	else
	{
		middle = first_1;
		second_top = first_1->next;
	}
	prev_l->next = NULL;
	reverse_list(&second_top);

	if (list_identical(first_top, second_top))
		return (1);
	else
		return (0);
}

/**
 * list_identical - checks if two linked lists contain identical elements
 * @list1: compares to list two
 * @list2: compares to list one
 * Return: 1 if identical, 0 if not dentical
 */
int list_identical(listint_t *list1, listint_t *list2)
{
	while (list1 || list2)
	{
		if (list1->n != list2->n || !list1 || !list2)
			return (0);
		if (list1)
			list1 = list1->next;
		if (list2)
			list2 = list2->next;
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
		new = next;
	}
	*head = prev;
}

