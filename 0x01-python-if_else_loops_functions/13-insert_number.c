#include "lists.h"
/**
 * insert_node - inserts a number into a list
 * @head: pointer to the list
 * @number: number to sum
 * Return: address
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *old_list, *new_list, *current_list;

	if (!head)
		return (NULL);

	new_list = malloc(sizeof(listint_t));
	if (!new_list)
		return (NULL);

	new_list->n = number;
	old_list = NULL;
	current_list = *head;

	while (current_list && current_list->n < number)
	{
		old_list = current_list;
		current_list = current_list->next;
	}

	new_list->next = current_list;

	if (old_list)
		old_list->next = new_list;
	else
		*head = new_list;

	return (new_list);
}
